import httpx
from modules.db_target_helper import dbTargetHelper
import pandas as pd
import ast

def get_data_from_source_to_target(variables,start_date,end_date) -> None:
    '''Function that uses the created FastAPI to get data from the source db, aggregates and saves it to target'''
    # Initialize dbtarget class
    dbHelper = dbTargetHelper()
    # Set Request Parameters
    url = 'http://fastapihost:80/get-source-data'
    data = {
        'variables':variables,
        'start_date':start_date,
        'end_date':end_date
    }
    response = httpx.post(url, json=data)
    print(response.status_code)
    if response.status_code == 200:
        # Convert response to dataframe and aggregate according to target
        try:
            df = pd.DataFrame.from_dict(ast.literal_eval(response.text), orient='columns').reset_index()
            df.ts = pd.to_datetime(df.ts)
            aggregation_df = dbHelper.get_aggregation_methods()
            
            agg_methods = {
                x:aggregation_df.name.values.tolist() for x in variables.split(',')
            }
            print(agg_methods)
            print(df.head())
            df = df.groupby(pd.Grouper(key='ts',freq='10T')).agg(agg_methods)
            df.columns = ['_'.join(col) for col in df.columns.values]
            df = df.reset_index().melt(id_vars=['ts'], var_name='vars_agg', value_name='value')

            #Get FK references from target db
            variables_df = dbHelper.get_signals()
            variables_df=variables_df.rename(columns={'id':'signal_id'})
            variables_df['key']=1
            aggregation_df=aggregation_df.rename(columns={'id':'agg_id'})
            aggregation_df['key']= 1
            var_agg_df = pd.merge(variables_df,aggregation_df,how='outer',on='key')
            var_agg_df['vars_agg'] = var_agg_df['name_x'] + '_' + var_agg_df['name_y']
            df = df.merge(var_agg_df[['vars_agg','signal_id','agg_id']],on='vars_agg',how='left')
        
            df[['ts','signal_id','agg_id','value']].to_sql('data',dbHelper.engine,if_exists='append',index=False)
            print(f'Data succesfully added to target DB!')
            print(df)
        except Exception  as e: 
            print(e)
            print(f'No data within {start_date} and {end_date}')
    else: 
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.text}")

if __name__ == '__main__':
    get_data_from_source_to_target('wind_speed,power,ambient_temperature','2024-05-01 00:00','2024-05-10 23:59')


import httpx
from modules.db_target_helper import dbTargetHelper
import pandas as pd
import ast

def get_data_from_source_to_target(variables,start_date,end_date):
    # Initialize dbtarget class
    dbHelper = dbTargetHelper()
    # Set Reqyest Parameters
    url = 'http://localhost:80/get-source-data'
    data = {
        'variables':variables,
        'start_date':start_date,
        'end_date':end_date
    }
    response = httpx.post(url, json=data)
    print(f"Status code: {response.status_code}")
    print(f"Response content: {response.text}")

    # Convert response to dataframe and aggregate according to target
    df = pd.DataFrame.from_dict(ast.literal_eval(response.text), orient='columns')
    df.ts = pd.to_datetime(df.ts)
    agg_methods = {
        x:['mean','min','max'] for x in variables.split(',')
    }
    df = df.groupby(pd.Grouper(key='ts',freq='10T')).agg(agg_methods)
    df.columns = ['_'.join(col) for col in df.columns.values]
    df = df.reset_index().melt(id_vars=['ts'], var_name='vars_agg', value_name='value')

    #Get FK references from target db
    variables_df = dbHelper.get_signals()
    variables_df=variables_df.rename(columns={'id':'signal_id'})
    variables_df['key']=1
    aggregation_df = dbHelper.get_aggregation_methods()
    aggregation_df=aggregation_df.rename(columns={'id':'agg_id'})
    aggregation_df['key']= 1
    var_agg_df = pd.merge(variables_df,aggregation_df,how='outer',on='key')
    var_agg_df['vars_agg'] = var_agg_df['name_x'] + '_' + var_agg_df['name_y']
    df = df.merge(var_agg_df[['vars_agg','signal_id','agg_id']],on='vars_agg',how='left')
    
    # Send Data to 'data' table into target db
    df[['ts','signal_id','agg_id','value']].to_sql('data',dbHelper.engine,if_exists='append',index=False)
    print(df)

if __name__ == '__main__':
    get_data_from_source_to_target('wind_speed','2024-05-01 00:00','2024-05-05 23:59')


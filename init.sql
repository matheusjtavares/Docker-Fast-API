CREATE TABLE IF NOT EXISTS data (
  input_data_id BIGSERIAL PRIMARY KEY, 
  TS TIMESTAMP not null,
  wind_speed FLOAT not null,
  power FLOAT not null,
  ambient_temperature FLOAT not null
);

INSERT INTO data (TS,wind_speed,power,ambient_temperature)
SELECT time,random()*20,random()*2000,random()*50 FROM 
    generate_series('2024-05-01',
    '2024-05-10 23:59:59', INTERVAL '1 minute') as time;

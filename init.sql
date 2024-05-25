CREATE TABLE IF NOT EXISTS input_data (
  input_data_id BIGSERIAL PRIMARY KEY, 
  TS TIMESTAMP not null,
  wind_speed FLOAT not null,
  power FLOAT not null,
  ambient_temperature FLOAT not null
);

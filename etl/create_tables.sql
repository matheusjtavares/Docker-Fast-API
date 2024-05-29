CREATE TABLE IF NOT EXISTS signal (
  id SERIAL PRIMARY KEY, 
  name str not null);
INSERT INTO signal (name)
VALUES ('wind_speed','ambient_temperature','power');

CREATE TABLE IF NOT EXISTS aggregations (
  id SERIAL PRIMARY KEY, 
  name str not null);

INSERT INTO aggregations (name)
VALUES ('mean','min','max','std');

CREATE TABLE IF NOT EXISTS data (
  id BIGSERIAL PRIMARY KEY,
  ts TIMESTAMP not null,
  signal_id INT ,
  agg_id INT,
  value FLOAT,

  CONSTRAINT fk_signal_id
    FOREIGN KEY (signal_id)
    REFERENCES signal(id)
    ON DELETE CASCADE,
  CONSTRAINT fk_agg_id
    FOREIGN KEY (agg_id)
    REFERENCES aggregations(id)
    ON DELETE CASCADE
)
  
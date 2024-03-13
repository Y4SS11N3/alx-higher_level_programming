-- Creates the table unique_id with id as INT unique and with a default value of 1, and name as VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);

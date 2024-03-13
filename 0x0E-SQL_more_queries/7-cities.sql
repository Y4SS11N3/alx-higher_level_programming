-- Creates the table cities in the database hbtn_0d_usa with a foreign key to states
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);

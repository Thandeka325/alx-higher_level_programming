-- Script creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa).
-- If the database hbtn_0d_usa, and states exists script does not fail.

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL  PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

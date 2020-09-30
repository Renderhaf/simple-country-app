CREATE DATABASE IF NOT EXISTS database1;
USE database1;
CREATE USER 'api'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL ON *.* TO 'api'@'localhost' WITH GRANT OPTION;
CREATE TABLE countries (name VARCHAR(75), capital VARCHAR(75), population INT(255), area FLOAT(16));
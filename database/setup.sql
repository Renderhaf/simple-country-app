CREATE DATABASE IF NOT EXISTS database1;
USE database1;
CREATE USER 'api'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL ON *.* TO 'api'@'localhost' WITH GRANT OPTION;
-- prepare Mysql server
-- create a new database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a new user hbnhb_dev identified by password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges to hbnb_dev_db database and all tables
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant select permission to performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

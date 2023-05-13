-- setup my sql server
-- create new database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user hbnb_test identified by password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges to database hbnb_test_db and all tables
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant select permission to performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

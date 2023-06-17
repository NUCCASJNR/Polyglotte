-- Write a script that prepares a MySQL server for the project:

-- A database blog_dev_db
-- A new user blog_dev (in localhost)
-- The password of blog_dev should be set to blog_dev_pwd
-- blog_dev should have all privileges on the database blog_dev_db (and only this database)
-- blog_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database blog_dev_db or the user blog_dev already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS blog_dev_db;
CREATE USER IF NOT EXISTS blog_dev@'localhost' IDENTIFIED BY 'blog_dev_pwd';
GRANT ALL PRIVILEGES ON blog_dev_db.* TO blog_dev@'localhost';
GRANT SELECT ON performance_schema.* TO blog_dev@'localhost';

-- Script to create MySQL user user_0d_1 with all privileges
-- This script creates the user if it doesn't exist and grants all privileges

-- Create user user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

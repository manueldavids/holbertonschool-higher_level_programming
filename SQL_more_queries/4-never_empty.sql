-- Script to create table id_not_null with default value for id
-- This script creates the table if it doesn't exist

-- Create table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

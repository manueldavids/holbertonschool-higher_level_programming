-- Script to create table force_name with id and name columns
-- This script creates the table if it doesn't exist

-- Create table force_name if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

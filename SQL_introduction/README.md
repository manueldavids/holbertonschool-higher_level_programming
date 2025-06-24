# SQL Introduction

This repository contains SQL scripts and exercises for learning MySQL database management.

## Description

This project covers fundamental SQL concepts and operations including:
- Database listing and management
- Table creation and manipulation
- Data insertion, selection, and modification
- Basic SQL queries and commands

## Requirements

- MySQL Server
- MySQL client
- Ubuntu 20.04 LTS (recommended)

## Installation

1. Install MySQL Server:
```bash
sudo apt update
sudo apt install mysql-server
```

2. Secure your MySQL installation:
```bash
sudo mysql_secure_installation
```

3. Access MySQL as root:
```bash
sudo mysql -u root -p
```

## Usage

### Running SQL Scripts

To execute a SQL script, use the following command format:
```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p
```

Example:
```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

### Scripts

- **0-list_databases.sql**: Lists all databases in the MySQL server

## Expected Output

### 0-list_databases.sql
```
Database
information_schema
mysql
performance_schema
sys
```

## Author

This project is part of the Holberton School curriculum.

## License

This project is open source and available under the [MIT License](LICENSE). 
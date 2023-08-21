-- Converts hbtn_0c_0 database, first_table and field name 
-- to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the database
USE hbtn_0c_0;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the specific field in the table to UTF8
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

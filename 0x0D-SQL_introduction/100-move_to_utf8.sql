-- Script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).
-- Converts Database hbtn_0c_0, Table first_table, Field name in first_table.

-- Select the database
USE hbtn_0c_0

-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table `first_table` to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field name in `first_table to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

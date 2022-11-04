-- Converts 'hbtn_0c_0' database to UTF-8 
-- Source https://stackoverflow.com/questions/72715542/character-set-vs-convert-to-character-set
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

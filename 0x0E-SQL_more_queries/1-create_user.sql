-- Create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

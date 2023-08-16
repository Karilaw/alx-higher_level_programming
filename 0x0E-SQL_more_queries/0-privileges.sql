-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- Select the user and host for the specified users
SELECT CONCAT('Grants for ', user, '@', host) FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';

-- Show grants for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show grants for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Lists all privileges of specific MySQL users on your server
SELECT * FROM information_schema.user_privileges WHERE GRANTEE LIKE '\'user_0d_1\'@\'localhost\'' OR GRANTEE LIKE '\'user_0d_2\'@\'localhost\'';

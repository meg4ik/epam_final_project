CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'qwerty';
GRANT
    INSERT, SELECT, UPDATE, DELETE
    , SHOW VIEW
ON
    db_user.*
TO
    'db_user'@'localhost';

FLUSH PRIVILEGES;


CREATE DATABASE department_project;
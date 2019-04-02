-- ------------------------------------------------------
-- ------------------------------------------------------

-- Test user for project mysql-log-analysis-ELK

create user 'learning-user'@'%' identified by 'learning';
grant execute on learning.* to 'learning-user'@'%';
flush privileges;

-- ------------------------------------------------------
-- ------------------------------------------------------


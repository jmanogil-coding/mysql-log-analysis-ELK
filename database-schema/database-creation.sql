-- ------------------------------------------------------
-- ------------------------------------------------------

-- Database sample for project mysql-log-analysis-ELK


-- MySQL dump 10.13  Distrib 5.7.21, for Win32 (AMD64)
--
-- Host: localhost    Database: learning
-- ------------------------------------------------------
-- Server version	5.7.21-log


DROP DATABASE IF EXISTS `learning`;
CREATE DATABASE `learning`;
USE `learning`;
DROP TABLE IF EXISTS `person`;

CREATE TABLE `person` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping routines for database 'learning'
--
DELIMITER ;;
CREATE PROCEDURE `usp_person_del`(v_id int(10))
BEGIN

	declare mysql_message varchar(3000);

	declare exit handler for sqlexception 
		begin  
			get stacked diagnostics condition 1 mysql_message= message_text;
			select 0 as result, mysql_message as message;   			
	end;

	delete from learning.person
    where id = v_id;

	if row_count() = 0 then
		select 0 as result, 'No rows found' as message;
	else
    	select 1 as result, 'OK' as message;
	end if;

END ;;

CREATE PROCEDURE `usp_person_ins`(v_first_name varchar(100), v_last_name varchar(100), v_birth_date DATE)
BEGIN

	declare mysql_message varchar(3000);

	declare exit handler for sqlexception 
		begin  
			get stacked diagnostics condition 1 mysql_message= message_text;
			select 0 as result, mysql_message as message;   			
	end;
	insert into learning.person (first_name, last_name, birth_date) values (v_first_name, v_last_name, v_birth_date);

	select 1 as result, 'OK' as message;

END ;;
CREATE PROCEDURE `usp_person_sel`(v_id int(10))
BEGIN

	-- all rows using v_id = 0
	select id, first_name, last_name, birth_date from learning.person where (id = v_id or v_id = 0);

END ;;

CREATE PROCEDURE `usp_person_upd`(v_id int(10), v_first_name varchar(100), v_last_name varchar(100), v_birth_date date)
BEGIN

	declare mysql_message varchar(3000);

	declare exit handler for sqlexception 
		begin  
			get stacked diagnostics condition 1 mysql_message= message_text;
			select 0 as result, mysql_message as message;   			
	end;

	update learning.person
    set 
		first_name = v_first_name,
		last_name = v_last_name,        
        birth_date = v_birth_date
    where id = v_id;
    
    if row_count() = 1 then
		select 1 as result, 'OK' as message;
    else
		select 0 as result, 'No row updated' as message;
	end if;

END ;;
DELIMITER ;

-- ------------------------------------------------------
-- ------------------------------------------------------

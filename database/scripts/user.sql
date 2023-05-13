DROP DATABASE IF EXISTS `test_userDB`;

CREATE DATABASE IF NOT EXISTS `test_userDB`;

USE `test_userDB`;

CREATE TABLE
    IF NOT EXISTS `userTBL` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `userid` VARCHAR(10) NOT NULL,
        `password` VARCHAR(100) NOT NULL,
        `name` VARCHAR(4) NOT NULL,
        `gender` CHAR(1) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY `userid_UNIQUE` (`userid`)
    ) ENGINE = InnoDB;

CREATE TABLE
    IF NOT EXISTS `recordTBL` (
        `id` INT(11) NOT NULL,
        `answer` VARCHAR(50) NOT NULL,
        `question` VARCHAR(50) NOT NULL,
        `date` DATETIME NOT NULL,
        PRIMARY KEY (`id`, `date`),
        CONSTRAINT `fk_recordTBL_userTBL` FOREIGN KEY (`id`) REFERENCES `userTBL` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
    ) ENGINE = InnoDB;
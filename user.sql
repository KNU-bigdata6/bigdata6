DROP SCHEMA IF EXISTS `test_userDB`;
CREATE SCHEMA IF NOT EXISTS `test_userDB`;
USE `test_userDB`;

CREATE TABLE IF NOT EXISTS `test_userDB`.`userTBL` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userid` VARCHAR(10) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `name` VARCHAR(4) NOT NULL,
  `gender` CHAR(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) VISIBLE);

CREATE TABLE IF NOT EXISTS `test_userDB`.`recordTBL` (
  `id` INT NOT NULL,
  `subject` VARCHAR(10) NOT NULL,
  `answer` VARCHAR(500) NOT NULL,
  `question` VARCHAR(500) NOT NULL,
  `date` DATETIME NOT NULL,
  CONSTRAINT `fk_recordTBL_userTBL`
    FOREIGN KEY (`id`)
    REFERENCES `test_userDB`.`userTBL` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
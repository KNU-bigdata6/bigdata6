DROP SCHEMA IF EXISTS `test_userDB`;

CREATE SCHEMA IF NOT EXISTS `test_userDB`;

USE `test_userDB`;

-- 사용자 테이블

CREATE TABLE
    IF NOT EXISTS `test_userDB`.`userTBL` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `userid` VARCHAR(10) NOT NULL,
        `password` VARCHAR(100) NOT NULL,
        `name` VARCHAR(4) NOT NULL,
        `gender` CHAR(1) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) VISIBLE
    );

-- 대화 내용 기록 테이블

CREATE TABLE
    IF NOT EXISTS `test_userDB`.`recordTBL` (
        `id` INT NOT NULL,
        `subject` VARCHAR(10) NOT NULL,
        `answer` VARCHAR(500) NOT NULL,
        `question` VARCHAR(500) NOT NULL,
        `date` DATETIME NOT NULL,
        CONSTRAINT `fk_recordTBL_userTBL` FOREIGN KEY (`id`) REFERENCES `test_userDB`.`userTBL` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- 게시글 테이블

CREATE TABLE
    IF NOT EXISTS `test_userDB`.`postTBL` (
        `idx` INT NOT NULL AUTO_INCREMENT,
        `id` INT NOT NULL,
        `userid` VARCHAR(10) NOT NULL,
        `title` VARCHAR(100) NOT NULL,
        `content` TEXT NOT NULL,
        `name` VARCHAR(4) NOT NULL,
        `city` VARCHAR(20) NOT NULL,
        `district` VARCHAR(20) NOT NULL,
        `views` INT NOT NULL DEFAULT 0,
        `date` DATETIME NOT NULL,
        PRIMARY KEY (`idx`),
        CONSTRAINT `fk_postTBL_userTBL1` FOREIGN KEY (`id`) REFERENCES `test_userDB`.`userTBL` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
    );

-- 댓글 테이블

CREATE TABLE
    IF NOT EXISTS `test_userDB`.`commentTBL` (
        `comment_num` INT NOT NULL AUTO_INCREMENT,
        `idx` INT NOT NULL,
        `id` INT NOT NULL,
        `userid` VARCHAR(10) NOT NULL,
        `text` TEXT NOT NULL,
        `name` VARCHAR(4) NOT NULL,
        `date` DATETIME NOT NULL,
        PRIMARY KEY (`comment_num`),
        INDEX `fk_commentTBL_userTBL1_idx` (`id` ASC) VISIBLE,
        INDEX `fk_commentTBL_postTBL1_idx` (`idx` ASC) VISIBLE,
        CONSTRAINT `fk_commentTBL_userTBL1` FOREIGN KEY (`id`) REFERENCES `test_userDB`.`userTBL` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
        CONSTRAINT `fk_commentTBL_postTBL1` FOREIGN KEY (`idx`) REFERENCES `test_userDB`.`postTBL` (`idx`) ON DELETE CASCADE
    )
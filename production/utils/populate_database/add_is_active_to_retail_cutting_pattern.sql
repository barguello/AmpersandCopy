SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

ALTER TABLE `Ampersand`.`retail_cutting_pattern_output` ADD COLUMN `is_active` TINYINT(1) NOT NULL DEFAULT 1  AFTER `is_for_cradle` ;


-- -----------------------------------------------------
-- Placeholder table for view `Ampersand`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Ampersand`.`view1` (`id` INT);


USE `Ampersand`;

-- -----------------------------------------------------
-- View `Ampersand`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Ampersand`.`view1`;
USE `Ampersand`;
;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

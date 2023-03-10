-- MySQL Script generated by MySQL Workbench
-- qua 08 fev 2023 16:49:52
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Conta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Conta` (
  `numero_conta` INT NOT NULL AUTO_INCREMENT,
  `cpf` VARCHAR(11) NOT NULL,
  `titular` VARCHAR(60) NOT NULL,
  `saldo` FLOAT NOT NULL,
  `senha` VARCHAR(32) NOT NULL,
  `login` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`numero_conta`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Historico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Historico` (
  `idHistorico` INT NOT NULL,
  `tipo_operacao` VARCHAR(45) NOT NULL,
  `data` VARCHAR(45) NOT NULL,
  `valor` FLOAT NULL,
  `Conta_numero_conta` INT NOT NULL,
  PRIMARY KEY (`idHistorico`),
  INDEX `fk_Historico_Conta_idx` (`Conta_numero_conta` ASC) VISIBLE,
  CONSTRAINT `fk_Historico_Conta`
    FOREIGN KEY (`Conta_numero_conta`)
    REFERENCES `mydb`.`Conta` (`numero_conta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

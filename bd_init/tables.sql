-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'User'
-- Quick user infos.
-- ---

USE projet;

DROP TABLE IF EXISTS `User`;
		
CREATE TABLE `User` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`)
) COMMENT 'Quick user infos.';

-- ---
-- Table 'Recipe'
-- 
-- ---

DROP TABLE IF EXISTS `Recipe`;
		
CREATE TABLE `Recipe` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_User` INTEGER NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `directives` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`)
);

-- ---
-- Table 'Cart'
-- 
-- ---

DROP TABLE IF EXISTS `Cart`;
		
CREATE TABLE `Cart` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_User` INTEGER NOT NULL,
  `totalCost` DECIMAL NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Ingredient'
-- 
-- ---

DROP TABLE IF EXISTS `Ingredient`;
		
CREATE TABLE `Ingredient` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_IngredientType` INTEGER NOT NULL,
  `id_QuantityUnit` INTEGER NOT NULL,
  `name` VARCHAR(30) NOT NULL,
  `baseCost` DECIMAL NOT NULL,
  `baseQuantity` DECIMAL NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`)
);

-- ---
-- Table 'Rating'
-- 
-- ---

DROP TABLE IF EXISTS `Rating`;
		
CREATE TABLE `Rating` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Recipe` INTEGER NOT NULL,
  `id_User` INTEGER NOT NULL,
  `value` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Comment'
-- 
-- ---

DROP TABLE IF EXISTS `Comment`;
		
CREATE TABLE `Comment` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Recipe` INTEGER NOT NULL,
  `id_User` INTEGER NULL DEFAULT NULL,
  `text` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'CartItem'
-- 
-- ---

DROP TABLE IF EXISTS `CartItem`;
		
CREATE TABLE `CartItem` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Ingredient` INTEGER NOT NULL,
  `id_Cart` INTEGER NOT NULL,
  `multiplier` INT NOT NULL,
  `subCost` DECIMAL NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'RecipeIngredient'
-- 
-- ---

DROP TABLE IF EXISTS `RecipeIngredient`;
		
CREATE TABLE `RecipeIngredient` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Recipe` INTEGER NOT NULL,
  `id_Ingredient` INTEGER NOT NULL,
  `id_QuantityUnit` INTEGER NOT NULL,
  `totalQuantity` DECIMAL NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'LikeRecipe'
-- 
-- ---

DROP TABLE IF EXISTS `LikeRecipe`;
		
CREATE TABLE `LikeRecipe` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Recipe` INTEGER NOT NULL,
  `id_User` INTEGER NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Account'
-- Private user infos.
-- ---

DROP TABLE IF EXISTS `Account`;
		
CREATE TABLE `Account` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_User` INTEGER NOT NULL,
  `id_Address` INTEGER NOT NULL,
  `firstName` VARCHAR(50) NOT NULL,
  `lastName` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT 'Private user infos.';

-- ---
-- Table 'Commands'
-- 
-- ---

DROP TABLE IF EXISTS `Commands`;
		
CREATE TABLE `Commands` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_Cart` INTEGER NOT NULL,
  `creationDate` DATE NOT NULL,
  `arrivalDate` DATE NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'IngredientType'
-- 
-- ---

DROP TABLE IF EXISTS `IngredientType`;
		
CREATE TABLE `IngredientType` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`name`)
);

-- ---
-- Table 'Address'
-- 
-- ---

DROP TABLE IF EXISTS `Address`;
		
CREATE TABLE `Address` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `number` INTEGER NOT NULL,
  `apartment` INTEGER NULL DEFAULT NULL,
  `street` VARCHAR(30) NOT NULL,
  `city` VARCHAR(30) NOT NULL,
  `country` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'Profile'
-- Other users public infos. To be shared publicly on his wall.
-- ---

DROP TABLE IF EXISTS `Profile`;
		
CREATE TABLE `Profile` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_User` INTEGER NOT NULL,
  `bio` MEDIUMTEXT NULL DEFAULT NULL,
  `backgroundPicture` BLOB NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) COMMENT 'Other users public infos. To be shared publicly on his wall.';

-- ---
-- Table 'QuantityUnit'
-- Register all mesure units (like mL, cups, g, table spoon, etc.). Contains both the name and the abbreviation. 
-- ---

DROP TABLE IF EXISTS `QuantityUnit`;
		
CREATE TABLE `QuantityUnit` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `id_QuantityType` INTEGER NOT NULL,
  `name` VARCHAR(20) NOT NULL,
  `abbreviation` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT 'Register all mesure units (like mL, cups, g, table spoon, et';

-- ---
-- Table 'QuantityType'
-- Contains the type of mesure (weight, volume, units, etc.)
-- ---

DROP TABLE IF EXISTS `QuantityType`;
		
CREATE TABLE `QuantityType` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT 'Contains the type of mesure (weight, volume, units, etc.)';

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `Recipe` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `Cart` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `Ingredient` ADD FOREIGN KEY (id_IngredientType) REFERENCES `IngredientType` (`id`);
ALTER TABLE `Ingredient` ADD FOREIGN KEY (id_QuantityUnit) REFERENCES `QuantityUnit` (`id`);
ALTER TABLE `Rating` ADD FOREIGN KEY (id_Recipe) REFERENCES `Recipe` (`id`);
ALTER TABLE `Rating` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `Comment` ADD FOREIGN KEY (id_Recipe) REFERENCES `Recipe` (`id`);
ALTER TABLE `Comment` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `CartItem` ADD FOREIGN KEY (id_Ingredient) REFERENCES `Ingredient` (`id`);
ALTER TABLE `CartItem` ADD FOREIGN KEY (id_Cart) REFERENCES `Cart` (`id`);
ALTER TABLE `RecipeIngredient` ADD FOREIGN KEY (id_Recipe) REFERENCES `Recipe` (`id`);
ALTER TABLE `RecipeIngredient` ADD FOREIGN KEY (id_Ingredient) REFERENCES `Ingredient` (`id`);
ALTER TABLE `RecipeIngredient` ADD FOREIGN KEY (id_QuantityUnit) REFERENCES `QuantityUnit` (`id`);
ALTER TABLE `LikeRecipe` ADD FOREIGN KEY (id_Recipe) REFERENCES `Recipe` (`id`);
ALTER TABLE `LikeRecipe` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `Account` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `Account` ADD FOREIGN KEY (id_Address) REFERENCES `Address` (`id`);
ALTER TABLE `Commands` ADD FOREIGN KEY (id_Cart) REFERENCES `Cart` (`id`);
ALTER TABLE `Profile` ADD FOREIGN KEY (id_User) REFERENCES `User` (`id`);
ALTER TABLE `QuantityUnit` ADD FOREIGN KEY (id_QuantityType) REFERENCES `QuantityType` (`id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `User` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Recipe` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Cart` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Ingredient` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Rating` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Comment` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `CartItem` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `RecipeIngredient` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Like` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Account` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Commands` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `IngredientType` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Address` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Profile` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `QuantityUnit` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `QuantityType` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `User` (`id`,`username`) VALUES
-- ('','');
-- INSERT INTO `Recipe` (`id`,`id_User`,`name`,`directives`) VALUES
-- ('','','','');
-- INSERT INTO `Cart` (`id`,`id_User`,`totalCost`) VALUES
-- ('','','');
-- INSERT INTO `Ingredient` (`id`,`id_IngredientType`,`id_QuantityUnit`,`name`,`baseCost`,`baseQuantity`) VALUES
-- ('','','','','','');
-- INSERT INTO `Rating` (`id`,`id_Recipe`,`id_User`,`value`) VALUES
-- ('','','','');
-- INSERT INTO `Comment` (`id`,`id_Recipe`,`id_User`,`text`) VALUES
-- ('','','','');
-- INSERT INTO `CartItem` (`id`,`id_Ingredient`,`id_Cart`,`multiplier`,`subCost`) VALUES
-- ('','','','','');
-- INSERT INTO `RecipeIngredient` (`id`,`id_Recipe`,`id_Ingredient`,`id_QuantityUnit`,`quantity`) VALUES
-- ('','','','','');
-- INSERT INTO `Like` (`id`,`id_Recipe`,`id_User`) VALUES
-- ('','','');
-- INSERT INTO `Account` (`id`,`id_User`,`id_Address`,`firstName`,`lastName`,`email`,`password`) VALUES
-- ('','','','','','','');
-- INSERT INTO `Commands` (`id`,`id_Cart`,`creationDate`,`arrivalDate`) VALUES
-- ('','','','');
-- INSERT INTO `IngredientType` (`id`,`name`) VALUES
-- ('','');
-- INSERT INTO `Address` (`id`,`number`,`apartment`,`street`,`city`,`country`) VALUES
-- ('','','','','','');
-- INSERT INTO `Profile` (`id`,`id_User`,`bio`,`backgroundPicture`) VALUES
-- ('','','','');
-- INSERT INTO `QuantityUnit` (`id`,`id_QuantityType`,`name`,`abbreviation`) VALUES
-- ('','','','');
-- INSERT INTO `QuantityType` (`id`,`name`) VALUES
-- ('','');
USE projet;


/*---------- STATIC TABLES ----------*/

INSERT INTO `IngredientType` (`id`,`name`) VALUES
(NULL, 'Dairy products'),
(NULL, 'Oils'),
(NULL, 'Fruits and vegetables'),
(NULL, 'Confectionery'),
(NULL, 'Cereal products'),
(NULL, 'Meat products'),
(NULL, 'Fish products'),
(NULL, 'Egg products'),
(NULL, 'Spices'),
(NULL, 'Beverages'),
(NULL, 'Salads'),
(NULL, 'Prepared foods'),
(NULL, 'Others');


INSERT INTO `QuantityType` (`id`,`name`) VALUES
(NULL, 'Volume'),
(NULL, 'Weight'),
(NULL, 'Length'),
(NULL, 'Unit');


INSERT INTO `QuantityUnit` (`id`,`id_QuantityType`,`name`,`abbreviation`) VALUES
(NULL, 1, 'teaspoon', 'tsp'),
(NULL, 1, 'tablespoon', 'tbsp'),
(NULL, 1, 'fluid ounce', 'fl oz'),
(NULL, 1, 'cup', 'c'),
(NULL, 1, 'pint', 'p'),
(NULL, 1, 'quart', 'q'),
(NULL, 1, 'gallon', 'g'),
(NULL, 1, 'milliliter', 'mL'),
(NULL, 1, 'liter', 'L'),
(NULL, 1, 'deciliter', 'dL'),
(NULL, 2, 'pound', 'lb'),
(NULL, 2, 'ounce', 'oz'),
(NULL, 2, 'miligram', 'mg'),
(NULL, 2, 'gram', 'g'),
(NULL, 2, 'kilogram', 'kg'),
(NULL, 3, 'milimeter', 'mm'),
(NULL, 3, 'centimeter', 'cm'),
(NULL, 3, 'meter', 'm'),
(NULL, 3, 'inch', 'in'),
(NULL, 4, 'unit', '');


/*---------- TEST DATA ----------*/

INSERT INTO `User` (`id`,`username`) VALUES
(NULL, 'Test'),
(NULL, 'test2');

INSERT INTO `Ingredient` (`id`,`id_IngredientType`,`id_QuantityUnit`,`name`,`baseCost`,`baseQuantity`) VALUES
(NULL, 3, 15, 'Apple', 3.20, 1);

INSERT INTO `Recipe` (`id`,`id_User`,`name`,`directives`) VALUES
(NULL, 1,'Best Recepie','1 - edfffseff 2 - fesfsgfsf 3 - sfffffwfw');

 INSERT INTO `Cart` (`id`,`id_User`,`totalCost`) VALUES
(Null, 1, 300);

 INSERT INTO `Rating` (`id`,`id_Recipe`,`id_User`,`value`) VALUES
(Null,1, 1, 4);

 INSERT INTO `Comment` (`id`,`id_Recipe`,`id_User`,`text`) VALUES
(Null, 1, 1,'Very good');

INSERT INTO `CartItem` (`id`,`id_Ingredient`,`id_Cart`,`multiplier`,`subCost`) VALUES
(NULL, 1, 1, 4, 12.80);

INSERT INTO `LikeRecipe` (`id`,`id_Recipe`,`id_User`) VALUES
(NULL, 1, 1);

INSERT INTO `Address` (`id`,`number`,`apartment`,`street`,`city`,`country`) VALUES
(NULL,'15', NULL,'Laurier','QC','Canada');

 INSERT INTO `Account` (`id`,`id_User`,`id_Address`,`firstName`,`lastName`,`email`,`password`) VALUES
(NULL, 1, 1, 'Jhon', 'Pro','jhonPro47@gmail.com','12345');

INSERT INTO `Profile` (`id`,`id_User`,`bio`,`backgroundPicture`) VALUES
(NULL, 1,'Big Jhon', NULL);

 INSERT INTO `RecipeIngredient` (`id`,`id_Recipe`,`id_Ingredient`,`id_QuantityUnit`,`totalQuantity`) VALUES
(NULL, 1, 1, 4, 1);

INSERT INTO `Commands` (`id`,`id_Cart`, `creationDate`, `arrivalDate`) VALUES
(NULL, 1, NOW(), NOW());



/*---------- RANDOM DATA ----------*/

DELIMITER $$
CREATE PROCEDURE insertValueUser(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `User` VALUES (NULL, i);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueIngredient(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Ingredient` VALUES (NULL, 3, 10, i, 2, 1);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueRecipe(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Recipe` VALUES (NULL, 1, i, "test");
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueCart(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Cart` VALUES (NULL, 1, 300);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueRating(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;

        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Rating` VALUES (NULL, 1, i, 5);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueComment(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Comment` VALUES (NULL, 1, i, "text");
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueCartItem(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `CartItem` VALUES (NULL, 1, 1, 3, 6);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueLikeRecipe(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `LikeRecipe` VALUES (NULL, 1, i);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueAddress(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Address` VALUES (NULL, i, NULL, "test", "QC", "Canada");
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueAccount(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Account` VALUES (NULL, i, i, "Phil", "Lucky", "philLucky77@gmail.com", "12345");
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueProfile(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Profile` VALUES (NULL, i, "small phil", NULL);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueRecipeIngredient(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `RecipeIngredient` VALUES (NULL, i, 1, 4, 1);
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE insertValueCommands(IN numRows INTEGER)
    BEGIN
        DECLARE i INTEGER;
        SET i = 1;
        WHILE i <= numRows DO
            INSERT INTO `Commands` VALUES (NULL, i, NOW(), NOW());
            SET i = i + 1;
        END WHILE;
    END$$
DELIMITER ;


CALL insertValueUser(100);
CALL insertValueIngredient(100);
CALL insertValueRecipe(100);
CALL insertValueCart(100);
CALL insertValueRating(100);
CALL insertValueComment(100);
CALL insertValueCartItem(100);
CALL insertValueLikeRecipe(100);
CALL insertValueAddress(100);
CALL insertValueAccount(100);
CALL insertValueProfile(100);
CALL insertValueRecipeIngredient(100);
CALL insertValueCommands(100);
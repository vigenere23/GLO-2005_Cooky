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
(Null,1,1, 4/5);

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
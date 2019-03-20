USE projet;

INSERT INTO `User` (`id`,`username`) VALUES
(NULL,'Test'), (NULL,"test2");



-- ---
-- Data Table 'IngredientType'
-- 
-- ---
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
(NULL, 'salads'),
(NULL, 'Prepared foods'),
(NULL, 'Others');


-- ---
-- Data Table 'MesureType'
-- Contains the type of mesure (weight, volume, units, etc.)
-- ---

INSERT INTO `MesureType` (`id`,`name`) VALUES
(NULL,'Volume'),
(NULL, 'Weight'),
(NULL, 'Length'),
(NULL, 'Temperature');

-- ---
-- Table 'Ingredient'
-- 
-- ---

INSERT INTO `Ingredient` (`id`,`id_MesureType`,`id_IngredientType`,`name`,`cost`,`baseQuantity`) VALUES
 (NULL, 1, 3,'Pomme', 3.20, 1);


-- ---
-- Table 'MesureUnit'
-- Register all mesure units (like mL, cups, g, table spoon, etc.). Contains both the name and the abbreviation. 
-- ---
INSERT INTO `MesureUnit` (`id`,`id_MesureType`,`name`,`abbreviation`) VALUES
(NULL, 1,'teaspoon','tsp'),
(NULL, 1,'tablespoon','tbsp'),
(NULL, 1,'fluid ounce','fl oz'),
(NULL, 1,'cup','c'),
(NULL, 1,'pint','p'),
(NULL, 1,'quart','q'),
(NULL, 1,'gallon','g'),
(NULL, 1,'milliliter','mL'),
(NULL, 1,'liter','L'),
(NULL, 1,'deciliter','dL'),
(NULL, 2, 'pound', 'lb'),
(NULL, 2, 'ounce', 'oz'),
(NULL, 2, 'miligram', 'mg'),
(NULL, 2, 'gram', 'g'),
(NULL, 2, 'kilogram', 'kg'),
(NULL, 3, 'milimeter', 'mm'),
(NULL, 3, 'centimeter', 'cm'),
(NULL, 3, 'meter', 'm'),
(NULL, 3, 'inch', 'in'),
(NULL, 4, 'Fahrenheit', '°F'),
(NULL, 4, 'Celsius', '°C');



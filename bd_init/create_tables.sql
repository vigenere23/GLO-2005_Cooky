DROP DATABASE IF EXISTS projet;
CREATE DATABASE projet;
USE projet;

CREATE TABLE User(
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  username CHAR(20) UNIQUE
);

CREATE TABLE Recipe(
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  title CHAR(50)
);

CREATE TABLE Ingredient(
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  name CHAR(50)
);

CREATE TABLE CreateRecipe(
  userId INTEGER,
  recipeId INTEGER,
  FOREIGN KEY(userId)
    REFERENCES User(id)
    ON DELETE CASCADE,
  FOREIGN KEY(recipeId)
    REFERENCES Recipe(id)
    ON DELETE CASCADE
);

CREATE TABLE RecipeIngredients(
  recipeId INTEGER,
  ingredientId INTEGER,
  FOREIGN KEY(recipeId)
    REFERENCES Recipe(id)
    ON UPDATE CASCADE,
  FOREIGN KEY(ingredientId)
    REFERENCES Ingredient(id)
    ON UPDATE CASCADE
);

CREATE TABLE LikeRecipe(
  userId INTEGER,
  recipeId INTEGER,
  FOREIGN KEY(userId)
    REFERENCES User(id)
    ON DELETE CASCADE,
  FOREIGN KEY(recipeId)
    REFERENCES Recipe(id)
    ON DELETE CASCADE
);

CREATE TABLE BookmarkRecipe
  LIKE LikeRecipe;

CREATE TABLE ShopIngredients(
  userId INTEGER,
  ingredientId INTEGER,
  FOREIGN KEY(userId)
    REFERENCES User(id)
    ON DELETE CASCADE,
  FOREIGN KEY(ingredientId)
    REFERENCES Ingredient(id)
    ON DELETE CASCADE
);

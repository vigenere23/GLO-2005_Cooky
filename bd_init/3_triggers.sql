use projet;

DELIMITER //

CREATE TRIGGER `NewCartForNewUser`
AFTER INSERT ON `User`
FOR EACH ROW
BEGIN
  INSERT INTO `Cart` (`id`, `id_User`, `totalCost`)
  VALUES (NULL, NEW.id, 0);
END;
//

CREATE TRIGGER `CalculateAverageRating`
AFTER INSERT ON `Rating`
FOR EACH ROW
BEGIN
  SET @rating := (SELECT AVG(R.value) FROM Rating R WHERE R.id_Recipe = NEW.id_Recipe);
  UPDATE Recipe R SET R.rating := @rating WHERE R.id = NEW.id_Recipe;
END;
//

CREATE TRIGGER `NewCartAfterCommand`
AFTER INSERT ON `Command`
FOR EACH ROW
BEGIN
  SET @userId := (SELECT Cart.id_User FROM Cart WHERE Cart.id = NEW.id_Cart);
  INSERT INTO `Cart` (`id`, `id_User`, `totalCost`)
  VALUES (NULL, @userId, 0);
END;
//

CREATE TRIGGER `CalculateSubCostCartItem`
BEFORE UPDATE ON `CartItem`
FOR EACH ROW
BEGIN
  SET @baseCost := (SELECT I.baseCost FROM Ingredient I WHERE I.id = NEW.id_Ingredient);
  SET NEW.subCost := @baseCost * NEW.multiplier;
END;
//

CREATE TRIGGER `CalculateTotalCostCart`
AFTER UPDATE ON `CartItem`
FOR EACH ROW
BEGIN
  SET @totalCost := (SELECT SUM(C.subCost) FROM CartItem C WHERE C.id_Cart = NEW.id_Cart);
  UPDATE Cart C SET C.totalCost := @totalCost WHERE C.id = NEW.id_Cart;
END;
//

CREATE TRIGGER `PreventModificationOfCommands`
BEFORE UPDATE ON `CartItem`
FOR EACH ROW
BEGIN
  SET @commandCountWithCartId := (SELECT COUNT(*) FROM Command C WHERE C.id_Cart = NEW.id_Cart);
  IF @commandCountWithCartId > 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = "Le panier à déjà été commandé et n'est plus modifiable";
  END IF;
END;
//

DELIMITER ;

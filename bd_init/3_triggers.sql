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

DELIMITER ;

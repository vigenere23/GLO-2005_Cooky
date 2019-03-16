DROP DATABASE IF EXISTS projet;
CREATE DATABASE projet;
USE projet;

CREATE TABLE Panier(
  idPanier INTEGER PRIMARY KEY,
  coutTotal FLOAT
);

CREATE TABLE Aliment(
  idAliment INTEGER PRIMARY KEY,
  nom VARCHAR(50),
  cout FLOAT
);

CREATE TABLE Contient(
  idPanier INTEGER,
  idAliment INTEGER,
  quantite INTEGER,
  FOREIGN KEY(idPanier) REFERENCES Panier(idPanier) ON DELETE CASCADE,
  FOREIGN KEY(idAliment) REFERENCES Aliment(idAliment) ON DELETE CASCADE
);

CREATE TABLE Commande(
idCommande INTEGER PRIMARY KEY
);

CREATE TABLE Confirmer(
  idPanier INTEGER,
  idCommande INTEGER,
  FOREIGN KEY(idPanier) REFERENCES Panier(idPanier) ON DELETE CASCADE,
  FOREIGN KEY(idCommande) REFERENCES Commande(idCommande) ON DELETE CASCADE
);

CREATE TABLE Domicile(
  adresse VARCHAR(200) PRIMARY KEY
);

CREATE TABLE Livrer(
  idCommande INTEGER,
  adresse VARCHAR(200),
  FOREIGN KEY(idCommande) REFERENCES Commande(idCommande) ON DELETE CASCADE,
  FOREIGN KEY(adresse) REFERENCES Domicile(adresse) ON DELETE CASCADE
);
  
CREATE TABLE Utilisateur(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nomUtilisateur VARCHAR(100),
  motDePasse VARCHAR(50),
  preference TEXT
);

INSERT INTO Utilisateur(id, nomUtilisateur, motDePasse, preference)
VALUES (NULL, "yolo", "motdepassepastresbon", "pas de bananes svp");

CREATE TABLE Rempli(
  idPanier INTEGER,
  id INTEGER,
  FOREIGN KEY(idPanier) REFERENCES Panier(idPanier) ON DELETE CASCADE,
  FOREIGN KEY(id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE TABLE TypeAliment(
  idType INTEGER PRIMARY KEY,
  nom VARCHAR(50)
);

CREATE TABLE TypeDe(
  idAliment INTEGER,
  idType INTEGER,
  FOREIGN KEY(idAliment) REFERENCES Aliment(idAliment) ON DELETE CASCADE,
  FOREIGN KEY(idType) REFERENCES TypeAliment(idType) ON DELETE CASCADE
);

CREATE TABLE Acheter(
  id INTEGER,
  idAliment INTEGER,
  FOREIGN KEY(idAliment) REFERENCES Aliment(idAliment) ON DELETE CASCADE,
  FOREIGN KEY(id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE TABLE Recette(
  idRecette INTEGER PRIMARY KEY,
  note INTEGER
);

CREATE TABLE Inclut(
  idRecette INTEGER,
  idAliment INTEGER,
  FOREIGN KEY(idAliment) REFERENCES Aliment(idAliment) ON DELETE CASCADE,
  FOREIGN KEY(idRecette) REFERENCES Recette(idRecette) ON DELETE CASCADE
);

CREATE TABLE Instruction(
  idInstruction INTEGER PRIMARY KEY,
  texte TEXT
);

CREATE TABLE Possede(
  idRecette INTEGER,
  idInstruction INTEGER,
  FOREIGN KEY(idRecette) REFERENCES Recette(idRecette) ON DELETE CASCADE,
  FOREIGN KEY(idInstruction) REFERENCES Instruction(idInstruction) ON DELETE CASCADE
);

CREATE TABLE Noter(
  idRecette INTEGER,
  id INTEGER,
  note INTEGER,
  FOREIGN KEY(idRecette) REFERENCES Recette(idRecette) ON DELETE CASCADE,
  FOREIGN KEY(id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE TABLE Aimer(
  idRecette INTEGER,
  id INTEGER,
  aime BIT,
  FOREIGN KEY(idRecette) REFERENCES Recette(idRecette) ON DELETE CASCADE,
  FOREIGN KEY(id) REFERENCES Utilisateur(id) ON DELETE CASCADE
);

CREATE TABLE Commentaire(
  idCommentaire INTEGER PRIMARY KEY,
  texte TEXT
);

CREATE TABLE Commenter(
  idRecette INTEGER,
  id INTEGER,
  idCommentaire INTEGER,
  FOREIGN KEY(idRecette) REFERENCES Recette(idRecette) ON DELETE CASCADE,
  FOREIGN KEY(id) REFERENCES Utilisateur(id) ON DELETE CASCADE,
  FOREIGN KEY(idCommentaire) REFERENCES Commentaire(idCommentaire) ON DELETE CASCADE
);

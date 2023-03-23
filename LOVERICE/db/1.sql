CREATE TABLE `Site_Marchand` (
  `URLSite` VARCHAR(255) NOT NULL,
  `NomSite` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`URLSite`)
);

CREATE TABLE `Utilisateur` (
  `idUtilisateur` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idUtilisateur`)
);

CREATE TABLE `Service_Client` (
  `IdSAV` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`IdSAV`)
);

CREATE TABLE `Thème` (
  `IdThème` INT NOT NULL AUTO_INCREMENT,
  `NomThème` VARCHAR(255) NOT NULL,
  `idUtilisateur` INT NOT NULL,
  PRIMARY KEY (`IdThème`),
  FOREIGN KEY (`idUtilisateur`) REFERENCES `Utilisateur`(`idUtilisateur`)
);

CREATE TABLE `Article` (
  `IdArt` INT NOT NULL AUTO_INCREMENT,
  `NomArt` VARCHAR(255) NOT NULL,
  `PrixArt` DECIMAL(10, 2) NOT NULL,
  `descriptionArt` TEXT NOT NULL,
  `URLArt` VARCHAR(255) NOT NULL,
  `IdThème` INT NOT NULL,
  PRIMARY KEY (`IdArt`),
  FOREIGN KEY (`IdThème`) REFERENCES `Thème`(`IdThème`)
);

CREATE TABLE `Proposer` (
  `IdArt` INT NOT NULL,
  `URLSite` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`IdArt`, `URLSite`),
  FOREIGN KEY (`IdArt`) REFERENCES `Article`(`IdArt`),
  FOREIGN KEY (`URLSite`) REFERENCES `Site_Marchand`(`URLSite`)
);

CREATE TABLE `Suggérer` (
  `IdArt` INT NOT NULL,
  `idUtilisateur` INT NOT NULL,
  PRIMARY KEY (`IdArt`, `idUtilisateur`),
  FOREIGN KEY (`IdArt`) REFERENCES `Article`(`IdArt`),
  FOREIGN KEY (`idUtilisateur`) REFERENCES `Utilisateur`(`idUtilisateur`)
);

CREATE TABLE `Rechercher` (
  `IdArt` INT NOT NULL,
  `idUtilisateur` INT NOT NULL,
  PRIMARY KEY (`IdArt`, `idUtilisateur`),
  FOREIGN KEY (`IdArt`) REFERENCES `Article`(`IdArt`),
  FOREIGN KEY (`idUtilisateur`) REFERENCES `Utilisateur`(`idUtilisateur`)
);

CREATE TABLE `Contacter` (
  `idUtilisateur` INT NOT NULL,
  `IdSAV` INT NOT NULL,
  `mailUtil` VARCHAR(255) NOT NULL,
  `NomUtil` VARCHAR(255) NOT NULL,
  `NumUtil` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`idUtilisateur`, `IdSAV`),
  FOREIGN KEY (`idUtilisateur`) REFERENCES `Utilisateur`(`idUtilisateur`),
  FOREIGN KEY (`IdSAV`) REFERENCES `Service_Client`(`IdSAV`)
);
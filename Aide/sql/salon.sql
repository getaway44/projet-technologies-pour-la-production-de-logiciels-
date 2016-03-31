

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


-- --------------------------------------------------------

--
-- Structure de la table `salon`
--

CREATE TABLE IF NOT EXISTS `salon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idpseudo` int(11) NOT NULL,
  `message` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idpseudo` (`idpseudo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



--
-- Contraintes pour la table `salon`
--
ALTER TABLE `salon`
  ADD CONSTRAINT `salon_ibfk_2` FOREIGN KEY (`idpseudo`) REFERENCES `pseudonyme` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;



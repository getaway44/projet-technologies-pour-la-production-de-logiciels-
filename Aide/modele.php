<?php


//####################################################################
// Question I

// Classe generale de definition d'exception
class MonException extends Exception{
  private $chaine;
  public function __construct($chaine){
    $this->chaine=$chaine;
  }

  public function afficher(){
    return $this->chaine;
  }

}


// Exception relative à un probleme de connexion
class ConnexionException extends MonException{
}

// Exception relative à un probleme d'accès à une table
class TableAccesException extends MonException{
}


// Classe qui gère les accès à la base de données

class Modele{
private $connexion;

// Constructeur de la classe
// remplacer X par les informations qui vous concernent
// à développer dans la question I

  public function __construct(){
  try{
      $chaine="mysql:host=localhost;dbname=E145530K";
      $this->connexion = new PDO($chaine,"E145530K","E145530K");
      // pour la prise en charge des exceptions par PHP
      $this->connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
     }
    catch(PDOException $e){
      $exception=new ConnexionException("problème de connection à la base");
      throw $exception;
    }
  }




// à développer dans la question I
// méthode qui permet de se deconnecter de la base
public function deconnexion()
{
	$connexion = null;
}



// à développer dans la question I
// méthode qui permet de récupérer les pseudos dans la table pseudo
// post-condition:
//retourne un tableau à deux dimensions dont le premier indice est un entier (commence à 0) qui correspond au numéro de ligne du résultat
// c'est en fait simplement le résultat de l'application de la méthode fetchAll()
// le second indice est une chaine de caractère qui correspond au nom de la colonne dans la table
// si un problème est rencontré, une exception de type TableAccesException est levée

public function getPseudos()
{
	try
	{
		$co = $this->connexion->prepare("SELECT * FROM pseudonyme");
		$co->execute();	
	
		//print("PDO::FETCH_ASSOC: ");
		//print("Retourne la ligne suivante en tant qu'un tableau indexé par le nom des colonnes\n");
		$result = $co->fetchAll();
		return($result);
	}
	catch(PDOException $e)
	{
		$exception=new ConnexionException("Erreur d'acces a la table.");
		throw $exception;
	}
}


// à développer dans la question I
//vérifie qu'un pseudo existe dans la table pseudonyme
// post-condition retourne vrai si le pseudo existe sinon faux
// si un problème est rencontré, une exception de type TableAccesException est levée
public function exists($pseudo)
{
	$co = $this->connexion->prepare("SELECT * FROM pseudonyme where pseudo ='" . $pseudo . "'");
	$co->execute();	
	
	$result = $co->fetchAll();
	if($result != null)
	{
		return true;
	}
	else
	{
		return false;
	}
}




// à développer dans la question II
// méthode qui permet de récupérer les 10 derniers messages émis sur le salon
// post-condition:
//retourne un tableau à deux dimensions dont le premier indice est un entier (commence à 0) qui correspond au numéro de ligne du résultat
// c'est en fait simplement le résultat de l'application de la méthode fetchAll()
// le second indice est une chaine de caractère qui correspond au nom de la colonne dans la table
// si un problème est rencontré, une exception de type TableAccesException est levée
public function get10RecentMessage()
{
	try
	{
		$co = $this->connexion->prepare("SELECT pseudo, message FROM pseudonyme p, salon s where p.id = s.idpseudo order by s.id DESC LIMIT 0, 10");
		$co->execute();	
	
		$result = $co->fetchAll();
		return($result);
	}
	catch(PDOException $e)
	{
		$exception=new ConnexionException("Erreur d'acces a la table.");
		throw $exception;
	}
	 
}


// à développer dans la question II
// ajoute un message sur le salon => pseudonyme + message
// precondition: le pseudo existe dans la table pseudonyme
// post-condition: le message est ajouté dans la table salon
// si un problème est rencontré, une exception de type TableAccesException est levée
		  
public function majSalon($pseudo,$message)
{
	try
	{
		if($this->exists($pseudo))
		{
			$co = $this->connexion->prepare("INSERT INTO salon (idpseudo, message) VALUES (?,?)");
			foreach ($this->connexion->query("select id from pseudonyme where pseudo ='".$pseudo."'") as $row)
			{
				$id = $row['id'];
			}
			$co->bindParam(1, $idpseudo);
			$co->bindParam(2, $message);
			$idpseudo = $id;
			$co->execute();
		}	
		else
		{
			echo 'Vous devez etre inscrit pour pouvoir participer au chat.';
		}	
	}
	catch(PDOException $e)
	{
		$exception=new TableAccesException("Erreur d'acces a la table.");
		throw $exception;
	}		      
}








}

?>

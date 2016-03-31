<?php
	include 'modele.php';
	$mod = new modele();
	if(isset($_POST['pseudo']))
	{
		if($mod->exists($_POST['pseudo'])){
		$bool = true;
		}
		else
		{
		$bool = false;
		}
	}
?>

<!doctype html>
<html lang="fr">
<head>
<title>Forum</title>
<meta charset="utf-8" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<link rel="stylesheet" href="style.css" style="text/css">
</head>
<body>
<div>
	<form action ="http://infoweb/~e145530k/TD4/vue.php" method="POST" >
	<?php 
	if(isset($_POST['pseudo']))
	{
		if($bool == false) 
		{
			echo 'Vous devez etre connecte pour pouvoir participer a la discussion';
		}
	}
	?>
	<p>
	<label for="pseudo">Pseudo :</label>
	<input type="text" name="pseudo" require/>
	</p>	
	
	<p>
	<label for="commentaire">Vos commentaires ?</label>
	<br>
	<textarea name="commentaire" value="commentaire" row="15" cols="50"></textarea>
	</p>
	
	<p>
	<input type="submit"  value="ENVOYER"/>
	<input type="reset"  value="Annuler"/>
	</p>
	<br>

 	<h2> Liste des 10 messages les plus récents </h2>

	<?php
	if(isset($bool))
	{
		if($bool == true)
		{
			$mod->majSalon($_POST['pseudo'], $_POST['commentaire']);
		}
	}	
	$tabResult=$mod->get10RecentMessage();
	foreach ($tabResult as $row)
	{
		echo $row['pseudo']." => ".$row['message']."<br/>";
	}
	?>
</form>	
</div>		
</body>
</html>

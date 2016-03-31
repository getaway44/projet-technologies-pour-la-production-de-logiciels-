<?php

// vous ne devez rien modifier dans ce script qui vous permet de tester votre classe Modele

header("Content-type: text/html; charset=utf-8");
require_once "modele.php";



// test pour la question I)

try{
$modele=new Modele();
$listePseudos=$modele->getPseudos();?>
<h1> Liste des pseudos dans la base </h1>
<?php
foreach ($listePseudos as $pseudo){
echo $pseudo["pseudo"];
echo "<br/>";
}
echo "<br/>";
?>
<h1> le pseudo existe t'il ? </h1>

<?php
if ($modele->exists("lebofred")){ 
echo "OK"."<br/>";
}
else{
echo "Non"."<br/>";
}


// test pour la question II)
// à décommenter pour la question II)

for ($i=0;$i<6;$i++){
$modele->majSalon("lebofred","coucou, je suis lebofred ".$i);
$modele->majSalon("titi44","coucou, je suis titi44 ".$i);
}



$tabResult=$modele->get10RecentMessage();

?>
 <h1> Liste des 10 messages les plus récents </h1>

<?php

foreach ($tabResult as $row){
echo $row['pseudo']." => ".$row['message']."<br/>";
}


}

catch (ConnexionException $e){
echo "problème de connexion";
}
catch (TableAccesException $e){
echo "problème de d'acces à une table";
}


?>

<?php
require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';
require 'classes/clients/MoviesApiClient.php';

use App\ElasticClient;
use App\MoviesApiClient;

$elastic = new ElasticClient();

$search_entry = htmlspecialchars($_POST['search_entry']);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Study movie search - search</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <h3 class="small_website_title">SMS</h1>
    <form id="search_entry" action="search.php" method="POST">
        <input type="text" name="search_entry" placeholder="">
        <button type="submit">Search</button>
    </form>
    <?php
        echo $elastic->search('movies', ['title' => $search_entry]);
    ?>
</body>
<?php
require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';
require 'classes/clients/MoviesApiClient.php';

use App\ElasticClient;
use App\MoviesApiClient;

$elastic = new ElasticClient();

$search_entry = htmlspecialchars($_POST['search_entry']);
$movies = json_decode($elastic->search('movies', ['title' => $search_entry]), true)['hits']['hits'];
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
    <?php foreach($movies as $entry): ?>
        <?php $movie = $entry['_source'];?>
        <div class="movie_entry">
            <img src=<?= $movie['poster']?>>
            <h4><?=$movie['title']?> (<?=$movie['year']?>)</h4> <?=$movie['runtime']?>, <?=$movie['rated']?>
            <?=$movie['plot']?>
            IMDb rating: <?=$movie['imdbRating']?>
            <?php //var_dump($movie);?>
        </div>
    <?php endforeach; ?>
</body>
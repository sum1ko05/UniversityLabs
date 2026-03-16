<?php
require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';
require 'classes/clients/MoviesApiClient.php';

use App\ElasticClient;
use App\MoviesApiClient;

$elastic = new ElasticClient();
$moviesapi = new MoviesApiClient();

$moviesapi_data = json_decode($moviesapi->get_all(), true)['data'];
// Pass data from api to Elastic
foreach($moviesapi_data as $entry)
{
    $entry_id = $entry['id'];
    unset($entry['id']);
    $elastic->indexDocument('movies', $entry_id, $entry);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Study movie search</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <h1 class="website_title">Study movie search</h1>
    <form id="search_entry" action="search.php" method="POST">
        <input type="text" name="search_entry" placeholder="">
        <button type="submit">Search</i></button>
    </form>
</body>
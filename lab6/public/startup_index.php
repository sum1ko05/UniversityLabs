<?php
//echo getcwd();
require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';
require 'classes/clients/MoviesApiClient.php';

//echo("Require passed\n");

use App\ElasticClient;
use App\MoviesApiClient;

$elastic = new ElasticClient();
$moviesapi = new MoviesApiClient();

//echo("Clients creation passed\n");

$moviesapi_data = json_decode($moviesapi->get_all(), true)['data'];

//echo("Data fetched\n");
// Pass data from api to Elastic
//$elastic->indexBulk('movies', $moviesapi_data);

foreach($moviesapi_data as $entry)
{
    $entry_id = $entry['id'];
    $elastic->indexDocument('movies', $entry_id, $entry);
}

//echo("Data indexed\n");

header("Location: index.html");
exit();
?>
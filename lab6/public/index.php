<?php

require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';
require 'classes/clients/MoviesApiClient.php';

use App\ElasticClient;
use App\MoviesApiClient;

// Elasticsearch
$elastic = new ElasticClient();
echo $elastic->indexDocument('books', 1, ['title' => '1984', 'author' => 'Orwell']);
echo $elastic->search('books', ['author' => 'Orwell']);

// MoviesApiClient
$moviesapi = new MoviesApiClient();
$moviesapidata = json_decode($moviesapi->get_all(), true)['data'];
echo "<br>";
foreach($moviesapidata as $entry)
{
    unset($entry['id']);
    var_dump($entry);
    echo "<br>";
}
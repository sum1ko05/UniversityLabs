<?php

require 'vendor/autoload.php';
require 'classes/clients/ElasticClient.php';

use App\ElasticClient;

// Elasticsearch
$elastic = new ElasticClient();
echo $elastic->indexDocument('books', 1, ['title' => '1984', 'author' => 'Orwell']);
echo $elastic->search('books', ['author' => 'Orwell']);

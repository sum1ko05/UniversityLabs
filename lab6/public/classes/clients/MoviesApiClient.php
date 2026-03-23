<?php

namespace App;

require 'vendor/autoload.php';
require_once 'ClientFactory.php';

use App\Helpers\ClientFactory;

class MoviesApiClient 
{
    private $client;

    public function __construct()
    {
        $this->client = ClientFactory::make('https://fooapi.com');
    }

    public function get_all()
    {
        $response = $this->client->get("/api/movies");
        return $response->getBody()->getContents();
    }
}

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
        $response = $this->client->get("api/movies");
        return $response->getBody()->getContents();
    }

    /*
    public function indexDocument($index, $id, $data)
    {
        $response = $this->client->put("$index/_doc/$id", [
            'json' => $data
        ]);
        return $response->getBody()->getContents();
    }

    public function search($index, $query)
    {
        $response = $this->client->get("$index/_search", [
            'json' => ['query' => ['match' => $query]]
        ]);
        return $response->getBody()->getContents();
    }
    */
}

//use GuzzleHttp\Client;

/*
class ApiClient {
    private Client $client;

    public function __construct() {
        $this->client = new Client();
    }

    public function request(string $url): array {
        try {
            $response = $this->client->get($url);
            $body = $response->getBody()->getContents();
            return json_decode($body, true);
        } catch (\Exception $e) {
            return ['error' => $e->getMessage()];
        }
    }
}
*/

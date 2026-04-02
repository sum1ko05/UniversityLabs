<?php

use PHPUnit\Framework\TestCase;
use GuzzleHttp\Client;

use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Psr7\Response;


class ApiTest extends TestCase
{
    public function testRequest()
    {
        $client = new Client([
            'base_uri' => 'http://localhost:8080'
        ]);

        $response = $client->get('/index.php');

        $this->assertEquals(200, $response->getStatusCode());
    }

    public function testMockRequest()
    {
        $mock = new MockHandler([
            new Response(200, [], 'OK')
        ]);

        $handlerStack = HandlerStack::create($mock);
        $client = new Client(['handler' => $handlerStack]);

        $response = $client->get('/test');

        $this->assertEquals(200, $response->getStatusCode());
    }

}

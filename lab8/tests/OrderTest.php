<?php

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../public/classes/Order.php';

class OrderTest extends TestCase
{
    private $pdo_mock;
    private $order;

    protected function setUp(): void
    {
        $stmt_mock = $this->createMock(PDOStatement::class);
        $stmt_mock->method("execute")
                         ->willReturn(true);
    
        $this->pdo_mock = $this->createMock(PDO::class);
        $this->pdo_mock->method("prepare")
                        ->willReturn($stmt_mock);
        $this->pdo_mock->method("query")
                        ->willReturn($stmt_mock);

        #var_dump($this->$pdo_mock);
        
        $this->order = new Order($this->pdo_mock);
    }
   
    public function testCreateWithMock()
    {
        $result = $this->order->create("Ivan", 
                                       "ivan@snafu.com", 
                                       "chair", 
                                       1, 
                                       0, 
                                       "pickup_delivery");

        #var_dump($result);

        $this->assertEquals(null, $result);
    }

    public function testReadAll()
    {
        $result = $this->order->readAll();

        $this->assertEquals([], $result);
    }
}

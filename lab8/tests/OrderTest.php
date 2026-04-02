<?php

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../public/classes/Order.php';

class OrderTest extends TestCase
{
   public function testCreateWithMock()
   {
        $stmt_mock = $this->createMock(PDOStatement::class);
        $stmt_mock->method("execute")
                  ->willReturn(true);
    
        $pdo_mock = $this->createMock(PDO::class);
        $pdo_mock->method("prepare")
                 ->willReturn($stmt_mock);

        $order = new Order($pdo_mock);

        $result = $order->create("Ivan", 
                                 "ivan@snafu.com", 
                                 "chair", 
                                 1, 
                                 0, 
                                 "pickup_delivery");

        $this->assertEquals(null, $result);
   }
}

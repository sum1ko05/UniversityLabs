<?php

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../public/classes/Order.php';

class OrderTest extends TestCase
{
   public function testCreate()
   {
       $order = new Order(null);

       $result = $order->create("Ivan", 
                                "ivan@test.com", 
                                "chair", 
                                1, 
                                false, 
                                "pickup_delivery");

       $this->assertEquals("Ivan's order created", $result);
   }
}

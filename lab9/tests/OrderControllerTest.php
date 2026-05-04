<?php
require_once __DIR__."/../vendor/autoload.php";

use PHPUnit\Framework\TestCase;

use App\Controller\OrderController;
use App\DTO\OrderDTO;

use function PHPUnit\Framework\assertEquals;

class OrderControllerTest extends TestCase
{
    private OrderController $order_controller;
    
    protected function setUp(): void
    {
        $this->order_controller = new OrderController();
    }

    private function POSTCorrectCase(): void
    {
        // Mock incoming POST request
        $_POST['username'] = "Ivan";
        $_POST['email'] = "ivanpetrovich@somemail.com";
        $_POST['model'] = "chair";
        $_POST['amount'] = "2";
        $_POST['assembly_included'] = "true";
        $_POST['delivery'] = "pickup_delivery";
    }

    public function testGetOrderFromPOST()
    {
        // Correct data case
        $this->POSTCorrectCase();

        $expected_order = new OrderDTO("Ivan", 
                                       "ivanpetrovich@somemail.com",
                                       "chair",
                                       "2",
                                       "true",
                                       "pickup_delivery");

        assertEquals($expected_order, $this->order_controller->getOrderFromPOST());
    }
}
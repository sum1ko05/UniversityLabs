<?php
require_once __DIR__."/../vendor/autoload.php";

use PHPUnit\Framework\TestCase;

use App\Controller\OrderController;
use App\Service\OrderValidationService;
use App\DTO\OrderDTO;
use App\Exception\ExceptionArray;

use function PHPUnit\Framework\assertEquals;
use function PHPUnit\Framework\assertFalse;
use function PHPUnit\Framework\assertTrue;

class OrderValidationTest extends TestCase
{
    private OrderController $order_controller;
    private OrderValidationService $validation_service;
    
    protected function setUp(): void
    {
        $this->order_controller = new OrderController();
        $this->validation_service = new OrderValidationService();
    }

    public function testValidateCorrectOrder()
    {
        // Correct data case
        $correct_order = new OrderDTO("Ivan", 
                                      "ivanpetrovich@somemail.com",
                                      "chair",
                                      "2",
                                      "true",
                                      "pickup_delivery");

        assertTrue($this->validation_service->isDTOValid($correct_order));
    }

    public function testValidateIncorrectOrderSimple()
    {
        // Incorrect data case
        $incorrect_order = new OrderDTO("", 
                                        "ivanpetrovichatsomemaildotcom",
                                        "chair",
                                        "0",
                                        "true",
                                        "pickup_delivery");

        assertFalse($this->validation_service->isDTOValid($incorrect_order));
    }

    public function testValidateIncorrectOrderDetailed()
    {
        // Incorrect data case
        $incorrect_order = new OrderDTO("", 
                                        "ivanpetrovichatsomemaildotcom",
                                        "chair",
                                        "0",
                                        "true",
                                        "pickup_delivery");

        // Exceptions, that should be thrown
        $expected_exarray = [new Exception("Name cannot be empty!", 400),
                             new Exception("Invalid email!", 400),
                             new Exception("Invalid item amount!", 400)];

        try {
            $this->validation_service->execute($incorrect_order);
        }
        catch (ExceptionArray $exarray)
        {
            assertEquals("Invalid order", $exarray->getMessage());
            assertEquals($expected_exarray, $exarray->GetExceptions());
        }
    }
}
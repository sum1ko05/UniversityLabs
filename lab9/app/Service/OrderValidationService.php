<?php

namespace App\Service;

use App\Service\IOrderService;

use App\DTO\OrderDTO;
use App\Exception\ExceptionArray;
use Exception;

class OrderValidationService implements IOrderService
{
    private Array $exceptions;
    
    public function execute(OrderDTO $dto): void
    {
        if (!$this->isDTOValid($dto))
        {
            // Invalid Order - 400 Bad Request
            throw new ExceptionArray(message: "Invalid order",
                                     code: 400,
                                     exceptions: $this->exceptions);
        }
    }

    public function isDTOValid(OrderDTO $dto): bool
    {
        $this->exceptions = [];
        // Check every property
        if (empty($dto->customerName)) {
            $this->exceptions[] = new Exception("Name cannot be empty!", 400);
        }
        if (!empty($dto->customerEmail) && !filter_var($dto->customerEmail, FILTER_VALIDATE_EMAIL)) {
            $this->exceptions[] = new Exception("Invalid email!", 400);
        }
        if (empty($dto->itemModel)) {
            $this->exceptions[] = new Exception("Item model name cannot be empty!", 400);
        }
        if ($dto->itemAmount < 1) {
            $this->exceptions[] = new Exception("Invalid item amount!", 400);
        }
        if (!isset($dto->assemblyIncluded)) {
            $this->exceptions[] = new Exception("assemblyIncluded option was not assigned", 500);
        }
        if (empty($dto->deliveryType)) {
            $this->exceptions[] = new Exception("Pick one delivery type!", 400);
        }

        // Check if we caught any exceptions
        if (empty($this->exceptions)) {return true;}
        else {return false;}
    }
    /*
    private OrderRepository $repository;

    public function __construct(OrderRepository $repository) {
        // Connect this immediately
        $this->repository = $repository;
    }

    public function connectRepository(OrderRepository $repository) {
        $this->repository = $repository;
    }
    */
}
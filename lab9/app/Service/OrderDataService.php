<?php

namespace App\Service;

use App\Service\IOrderService;

use App\DTO\OrderDTO;
use App\Repository\OrderRepository;

class OrderDataService implements IOrderService
{
    private OrderRepository $repository;

    public function __construct(OrderRepository $repository) {
        // Connect this immediately
        $this->repository = $repository;
    }

    public function connectRepository(OrderRepository $repository) {
        $this->repository = $repository;
    }
    
    public function execute(OrderDTO $dto): void
    {
        
    }
}
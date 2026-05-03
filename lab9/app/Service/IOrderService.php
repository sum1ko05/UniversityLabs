<?php

namespace App\Service;

use App\DTO\OrderDTO;

interface IOrderService
{
    public function execute(OrderDTO $dto): void;
}
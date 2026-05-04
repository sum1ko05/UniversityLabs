<?php

namespace App\Service;

use App\DTO\OrderDTO;

interface IOrderService
{
    public function execute(?OrderDTO $dto = null, ?Array $params = null): void;
}
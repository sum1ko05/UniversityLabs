<?php

namespace App\DTO;

# Immutable object only for data transfer
# Create through controller
class OrderDTO
{
    public readonly string $customerName;
    public readonly string $customerEmail;
    public readonly string $itemModel;
    public readonly int $itemAmount;
    public readonly bool $assemblyIncluded;
    public readonly string $deliveryType;

    public function __construct(string $name, string $email, string $model,
                                int $amount, bool $assemblyIncluded, 
                                string $deliveryType)
    {
        $this->customerName = $name;
        $this->customerEmail = $email;
        $this->itemModel = $model;
        $this->itemAmount = $amount;
        $this->assemblyIncluded = $assemblyIncluded;
        $this->deliveryType = $deliveryType;
    }
}
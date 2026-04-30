<?php

namespace App\Repository;

use App\DTO\OrderDTO;

# Class for interacting with DB
# Do not invoke it directly!
class OrderRepository
{
    protected PDO $pdo;

    public function __construct()
    {
        
    }
}
<?php

namespace App\Controller;

use App\DTO\OrderDTO;

class OrderController
{    
    public function getOrderFromSession(): OrderDTO
    {
        $name = htmlspecialchars($_POST['username']);
        $email = htmlspecialchars($_POST['email'] ?? '');
        $model = htmlspecialchars($_POST['model']);
        $amount = intval($_POST['amount'] ?? 1);
        $assembly_included = isset($_POST['assembly_included']);
        $delivery = htmlspecialchars($_POST['delivery'] ?? '');

        return new OrderDTO($name, $email, $model, $amount, $assembly_included, $delivery);
    }
}
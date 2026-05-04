<?php

namespace App\Repository;

require_once __DIR__."/../../vendor/autoload.php";

use App\DTO\OrderDTO;
use PDO;

# Class for interacting with DB
class OrderRepository
{
    protected PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    #region CRUD:
    public function create(OrderDTO $order) {
        $stmt = $this->pdo->prepare(
            "INSERT INTO orders (name, email, model, amount, assembly_included, delivery) VALUES (?, ?, ?, ?, ?, ?)"
        );
        $stmt->execute([$order->customerName, 
                        $order->customerEmail, 
                        $order->itemModel, 
                        $order->itemAmount, 
                        $order->assemblyIncluded ? 1 : 0, 
                        $order->deliveryType]);
    }

    public function readAll() {
        $stmt = $this->pdo->query("SELECT * FROM orders");
        return $stmt->fetchAll();
    }

    public function update(string $name, int $id) {
        $stmt = $this->pdo->prepare("UPDATE orders SET name=? WHERE id=?");
        $stmt->execute([$name, $id]);
    }

    public function delete(int $id) {
        $stmt = $this->pdo->prepare("DELETE FROM orders WHERE id=?");
        $stmt->execute([$id]);
    }
    #endregion
}
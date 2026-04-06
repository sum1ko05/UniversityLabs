<?php

use PHPUnit\Framework\TestCase;

require_once __DIR__ . '/../public/classes/Order.php';

class OrderTest extends TestCase
{
    private $stmt_mock;
    private $pdo_mock;
    private $order;

    protected function setUp(): void
    {
        $this->stmt_mock = $this->createMock(PDOStatement::class);
        $this->pdo_mock = $this->createMock(PDO::class);
        $this->order = new Order($this->pdo_mock);
    }
    
    public function testCreateWithMock()
    {
        $this->stmt_mock->expects($this->once())
                        ->method("execute")
                        ->with(["Ivan", "ivan@snafu.com", "chair", 1, 0, "pickup_delivery"])
                        ->willReturn(true);

        $this->pdo_mock->expects($this->once())
                       ->method("prepare")
                       ->with("INSERT INTO orders (name, email, model, amount, assembly_included, delivery) VALUES (?, ?, ?, ?, ?, ?)")
                       ->willReturn($this->stmt_mock);

        $result = $this->order->create("Ivan", 
                                       "ivan@snafu.com", 
                                       "chair", 
                                       1, 
                                       0, 
                                       "pickup_delivery");
    }

    public function testReadAllWithMock()
    {
        $this->stmt_mock->expects($this->once())
                        ->method("fetchAll")
                        ->with()
                        ->willReturn([]);

        $this->pdo_mock->expects($this->once())
                       ->method("query")
                       ->with("SELECT * FROM orders")
                       ->willReturn($this->stmt_mock);

        $result = $this->order->readAll();

        $this->assertEquals([], $result);
    }
}

<?php

namespace App\Service;

use App\Service\IOrderService;

use App\DTO\OrderDTO;
use App\Repository\OrderRepository;
use Exception;

class OrderDataService implements IOrderService
{
    private OrderRepository $repository;
    private Array $result;

    public function __construct(OrderRepository $repository) {
        // Connect this immediately
        $this->repository = $repository;
    }

    public function connectRepository(OrderRepository $repository) {
        $this->repository = $repository;
    }

    public function getResult(): Array
    {
        return $this->result;
    }
    
    public function execute(?OrderDTO $dto = null, ?Array $params = null): void
    {
        if (!array_key_exists(key: "func", array: $params))
        {
            throw new Exception("OrderDataService params should include 'func' param", 500);
        }
        
        $func = $params["func"];
        if ($func == "create")
        {
            if ($dto !== null) {$this->repository->create($dto);}
            else {throw new Exception("Order should not be null on repo addition", 500);}
        }
        else if ($func == "read")
        {
            $this->result = $this->repository->readAll();
        }
        else if ($func == "update")
        {
            if (array_key_exists(key: "name", array: $params) && array_key_exists(key: "id", array: $params))
            {
                if (gettype($params["name"]) == "string" && gettype($params["id"]) == "integer")
                {
                    if (empty($params["name"])) {
                        throw new Exception("Name cannot be empty!", 400);
                    }
                    else if ($params["id"] < 1) {
                        throw new Exception("Invalid 'id' param!", 400);
                    }
                    else {$this->repository->update($params["name"], $params["id"]);}
                }
                else {throw new Exception("Incorrect 'name' or 'id' params type", 500);}
            }
            else {throw new Exception("'update' func should contain params 'name' and 'id'", 500);}
        }
        else if ($func == "delete")
        {
            if (array_key_exists(key: "id", array: $params))
            {
                if (gettype($params["id"]) == "integer")
                {
                    if ($params["id"] < 1) {
                        throw new Exception("Invalid 'id' param!", 400);
                    }
                    else {$this->repository->delete($params["id"]);}
                }
                else {throw new Exception("Incorrect 'id' param type", 500);}
            }
            else {throw new Exception("'delete' func should contain param 'id'", 500);}
        }
        else
        {
            throw new Exception("$func is not implemented in OrderDataService (yet)", 500);
        }
    }
}
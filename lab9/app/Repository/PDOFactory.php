<?php

namespace App\Repository;

require_once __DIR__."/../../vendor/autoload.php";

use PDO;

class PDOFactory
{
    public function createFromEnv(): PDO
    {
        $host = getenv("MYSQL_HOST");
        $db   = getenv("MYSQL_DATABASE");
        $user = getenv("MYSQL_USER");
        $pass = getenv("MYSQL_PASSWORD");
        $charset = 'utf8mb4';

        $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ];

        try 
        {
            $pdo = new PDO($dsn, $user, $pass, $options);
        }
        catch (\PDOException $e) 
        {
            echo "Connection error: " . $e->getMessage();
            exit();
        }
        return $pdo;
    }
}
<?php
require_once __DIR__."/../vendor/autoload.php";

use App\Controller\OrderController;
use App\Service\OrderValidationService;
use App\Service\OrderDataService;
use App\Repository\OrderRepository;
use App\Repository\PDOFactory;

use App\Exception\ExceptionArray;

session_start();

//Saving cookie right after submitting
setcookie("last_submission", date('Y-m-d H:i:s'), time() + 3600, "/");

$pdo = new PDOFactory();

$order_controller = new OrderController();
$order_validator = new OrderValidationService();
$order_repository = new OrderRepository($pdo->createFromEnv());

$current_order = $order_controller->getOrderFromPOST();

$_SESSION['errors'] = null;
try {
    $order_validator->execute($current_order);
}
catch (ExceptionArray $array) {
    foreach ($array->GetExceptions() as $e)
    {
        //echo gettype($array->GetExceptions());
        $_SESSION['errors'][] = $e->message;
    }
    // Redirect to index.php
    header("Location: index.php");
    exit();
}

$order_data_service = new OrderDataService($order_repository);
try {
    $order_data_service->execute($current_order, ["func" => "create"]);
}
catch (Exception $e) {
    $_SESSION['errors'][] = $e->getMessage();
    // Redirect to index.php
    header("Location: index.php");
    exit();
}

//var_dump($current_order);

// Redirect to index.php
header("Location: index.php");
exit();

?>
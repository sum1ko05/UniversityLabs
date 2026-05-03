<?php
require_once __DIR__."/../vendor/autoload.php";

use App\Controller\OrderController;
use App\Service\OrderValidationService;
use App\Repository\PDOFactory;

use App\Exception\ExceptionArray;

session_start();

//Saving cookie right after submitting
setcookie("last_submission", date('Y-m-d H:i:s'), time() + 3600, "/");

var_dump(class_exists(\App\Controller\OrderController::class));

$order_controller = new OrderController();
$order_validator = new OrderValidationService();

$current_order = $order_controller->getOrderFromSession();

try {
    $order_validator->execute($current_order);
}
catch (ExceptionArray $array) {
    foreach ($array as $e)
    {
        $_SESSION['errors'][] = $e->message;
    }
    // Redirect to index.php
    header("Location: index.php");
    exit();
}

var_dump($current_order);

// Redirect to index.php
header("Location: index.php");
exit();

?>
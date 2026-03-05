<?php
session_start();

require 'classes/db.php';
require 'classes/Order.php';

$order = new Order($pdo);

//Saving cookie right after submitting
setcookie("last_submission", date('Y-m-d H:i:s'), time() + 3600, "/");

// Pull data from form
$name = htmlspecialchars($_POST['username']);
$email = htmlspecialchars($_POST['email'] ?? '');
$model = htmlspecialchars($_POST['model']);
$amount = intval($_POST['amount'] ?? 1);
$assembly_included = isset($_POST['assembly_included']) ? 1 : 0;
$delivery = htmlspecialchars($_POST['delivery'] ?? '');

// Validate form data first
$errors = [];
if(empty($name)) $errors[] = "Имя не может быть пустым";
if(!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Некорректный email";
if(empty($model)) $errors[] = "Модель не была выбрана";

// Don't save anything to session if we got any errors
if(!empty($errors)){
    $_SESSION['errors'] = $errors;
    header("Location: index.php");
    exit();
}

// Save form data to session
$_SESSION['name'] = $name;
$_SESSION['email'] = $email;

// Write form data to database
$order->create($name, $email, $model, $amount, $assembly_included, $delivery);

// Redirect to index.php
header("Location: index.php");
exit();

?>
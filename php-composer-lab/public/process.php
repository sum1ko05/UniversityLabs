<?php

session_start();

// Pull data from form
$username = htmlspecialchars($_POST['username']);
$email = htmlspecialchars($_POST['email'] ?? '');

// Validate form data first
$errors = [];
if(empty($username)) $errors[] = "Имя не может быть пустым";
if(!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Некорректный email";

// Don't save anything to session if we got any errors
if(!empty($errors)){
    $_SESSION['errors'] = $errors;
    header("Location: index.php");
    exit();
}

// Save form data to session
$_SESSION['username'] = $username;
$_SESSION['email'] = $email;

// Write form data to external text file
$line = $username . ";" . $email . "\n";
file_put_contents("data/data.txt", $line, FILE_APPEND);

// Form handling finished, add external API data to session
require_once 'classes/ApiClient.php';
$api = new ApiClient();

$url = 'https://dummyjson.com/products/category/furniture';
$apiData = $api->request($url);

$_SESSION['api_data'] = $apiData;

// Redirect to index.php
header("Location: index.php");
exit();

?>
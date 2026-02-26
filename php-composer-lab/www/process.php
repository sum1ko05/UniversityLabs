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
file_put_contents("data.txt", $line, FILE_APPEND);

// Redirect to index.php
header("Location: index.php");
exit();

?>
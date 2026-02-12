<?php

session_start();

// Pull data from form
$username = htmlspecialchars($_POST['username']);
$email = htmlspecialchars($_POST['email'] ?? '');

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
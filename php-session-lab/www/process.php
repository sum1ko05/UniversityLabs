<?php

session_start();

$username = htmlspecialchars($_POST['username']);
$email = htmlspecialchars($_POST['email'] ?? '');

// Save form data to session
$_SESSION['username'] = $username;
$_SESSION['email'] = $email;

header("Location: index.php");
exit();

?>
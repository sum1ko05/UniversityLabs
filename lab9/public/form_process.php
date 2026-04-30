<?php
session_start();

//Saving cookie right after submitting
setcookie("last_submission", date('Y-m-d H:i:s'), time() + 3600, "/");

// Pull data from form
$name = htmlspecialchars($_POST['username']);
$email = htmlspecialchars($_POST['email'] ?? '');
$model = htmlspecialchars($_POST['model']);
$amount = intval($_POST['amount'] ?? 1);
$assembly_included = isset($_POST['assembly_included']) ? 1 : 0;
$delivery = htmlspecialchars($_POST['delivery'] ?? '');

// Redirect to index.php
header("Location: index.php");
exit();

?>
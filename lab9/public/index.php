<?php session_start(); ?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Все данные</title>
    <link rel="stylesheet" href="styles/common_style.css">
</head>
<body>
    <div class="session_data">
        <?php if(isset($_SESSION['name'])): ?>
            <h2>Данные из сессии:</h2>
            <ul>
                <li>Имя: <?= $_SESSION['name'] ?></li>
                <li>Email: <?= $_SESSION['email'] ?></li>
            </ul>
        <?php else: ?>
            <p>Данных пока нет.</p>
        <?php endif; ?>
    </div>
    <div class="form_and_view_links">
        <a href="form.html">Заполнить форму</a>
    </div>
</body>
<?php session_start(); ?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Все данные</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <div class="session_data">
        <?php if(isset($_SESSION['username'])): ?>
            <h2>Данные из сессии:</h2>
            <ul>
                <li>Имя: <?= $_SESSION['username'] ?></li>
                <li>Email: <?= $_SESSION['email'] ?></li>
            </ul>
        <?php else: ?>
            <p>Данных пока нет.</p>
        <?php endif; ?>
    </div>
    <div class="form_and_view_links">
        <a href="form.html">Заполнить форму</a> |
        <a href="view.php">Посмотреть все данные</a>
    </div>
    <div class="errors">
        <?php if(isset($_SESSION['errors'])): ?>
            <ul>
                <p>Данные не сохранены!</p>
                <?php foreach($_SESSION['errors'] as $error): ?>
                    <li><?= $error ?></li>
                <?php endforeach; ?>
            </ul>
            <?php unset($_SESSION['errors']); ?>
        <?php endif; ?>
    </div>
</body>
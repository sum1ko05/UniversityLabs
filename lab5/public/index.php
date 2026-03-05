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
    <div class="errors">
        <?php if(isset($_SESSION['errors'])): ?>
            <h2>Данные не сохранены!</h2>
            <ul>
                <?php foreach($_SESSION['errors'] as $error): ?>
                    <li><?= $error ?></li>
                <?php endforeach; ?>
            </ul>
            <?php unset($_SESSION['errors']); ?>
        <?php endif; ?>
    </div>
    <div class="saved_data">
        <?php
            require 'classes/db.php';
            require 'classes/Order.php';

            $order = new Order($pdo);
            $all = $order->readAll();
        ?>
        <h2>Сохранённые данные:</h2>
        <ul>
            <?php foreach($all as $row): ?>
                <li><?= $row['name'] ?> (<?= $row['email'] ?>), <?= $row['model'] ?>, <?= $row['amount'] ?>, Сборка включена: <?= $row['assembly_included'] ? 'Да' : 'Нет' ?>, <?= $row['delivery'] ?></li>
            <?php endforeach; ?>
        </ul>
    </div>
    <div class="form_and_view_links">
        <a href="form.html">Заполнить форму</a>
    </div>
</body>
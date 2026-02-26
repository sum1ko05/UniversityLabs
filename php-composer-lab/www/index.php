<?php session_start(); ?>

<head>
    <title>Главная</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="common_style.css">
</head>

<div>
<?php if(isset($_SESSION['username'])): ?>
    <p>Данные из сессии:</p>
    <ul>
        <li>Имя: <?= $_SESSION['username'] ?></li>
        <li>Email: <?= $_SESSION['email'] ?></li>
    </ul>
<?php else: ?>
    <p>Данных пока нет.</p>
<?php endif; ?>

<a href="form.html">Заполнить форму</a> |
<a href="view.php">Посмотреть все данные</a>
</div>

<?php if(isset($_SESSION['errors'])): ?>
    <ul style="color:red;">
        Данные не сохранены!
        <?php foreach($_SESSION['errors'] as $error): ?>
            <li><?= $error ?></li>
        <?php endforeach; ?>
    </ul>
    <?php unset($_SESSION['errors']); ?>
<?php endif; ?>

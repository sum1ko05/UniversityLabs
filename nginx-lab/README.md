# Лабораторная работа №1: Nginx + Docker

## 👩‍💻 Автор
ФИО: Хуснутдинов Роман Сергеевич

Группа: 2ИП-1

---

## 📌 Описание задания
Создать веб-сервер в Docker с использованием Nginx и подключить HTML-страницу.  
Результат доступен по адресу [http://localhost:8080](http://localhost:8080).

---

## ⚙️ Как запустить проект

1. Клонировать ветку репозитория:
   ```bash
   git clone -b web https://github.com/sum1ko05/UniversityLabs.git
   cd UniversityLabs/nginx-lab
   ```
2. Запустить контейнеры:
   ```bash
   docker compose up -d --build
   ```
3. Открыть в браузере:
   ```http://localhost:8080```

📂 Содержимое проекта

```docker-compose.yml``` — описание сервиса Nginx

```code/index.html``` — главная HTML-страница

```screenshots/``` — все скриншоты

📸 Скриншоты работы

![Скриншот этапа 1](/nginx-lab/screenshots/stage1.png)

![Скриншот этапа 2](/nginx-lab/screenshots/stage2.png)

![Скриншот этапа 3](/nginx-lab/screenshots/stage3.png)

![Скриншот этапа 4, эксперимент 1](/nginx-lab/screenshots/stage4_index_change.png)

![Скриншот этапа 4, эксперимент 2](/nginx-lab/screenshots/stage4_new_page.png)

![Скриншот этапа 4, эксперимент 3](/nginx-lab/screenshots/stage4_new_port.png)

✅ Результат

Сервер в Docker успешно запущен, Nginx отдаёт мою HTML-страницу.
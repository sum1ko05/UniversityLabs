FROM php:8.4-fpm

RUN docker-php-ext-install pdo pdo_mysql
RUN apt-get update && apt-get install -y unzip git

# Composer installation
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/composer
COPY ./public /var/www/html
COPY ./composer.json /var/www/composer/composer.json
COPY ./composer.lock /var/www/composer/composer.lock

RUN composer install

CMD ["php-fpm"]
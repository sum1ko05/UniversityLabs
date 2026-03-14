FROM php:8.2-fpm

# Just a defensive practice
RUN apt-get update && apt-get install -y unzip git

# Composer installation
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/composer
COPY ./public /var/www/html
COPY ./composer.json /var/www/composer/composer.json
COPY ./composer.lock /var/www/composer/composer.lock

RUN composer install

CMD ["php-fpm"]

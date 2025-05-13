FROM php:8.2-apache
COPY uploads/ /var/www/html/uploads/
RUN chmod -R 755 /var/www/html/uploads/
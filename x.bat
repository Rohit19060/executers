@echo off

IF "%1"=="flutter" (
   flutter clean
   flutter pub get
)
IF "%1"=="flutterupdate" (
   flutter pub upgrade --major-versions
   flutter pub upgrade --tighten
)
IF "%1"=="php" (
    composer install
    composer update
    php artisan key:generate
    php artisan cache:clear
    php artisan migrate:fresh --seed
)
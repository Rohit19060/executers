@echo off

IF "%1"=="flutter" (
   flutter clean
   flutter pub get
   flutter analyze
)
IF "%1"=="flutterupdate" (
   flutter clean
   flutter pub upgrade --major-versions
   flutter pub upgrade --tighten
   flutter analyze
)
IF "%1"=="php" (
    composer install
    composer update
    php artisan key:generate
    php artisan cache:clear
    php artisan migrate:fresh --seed
)
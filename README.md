# jpg-webp
Генерация картинок jpg и webp

В теме WP Морковина UserFirst при переходе от php 7.4 на 8.2 перестает работать правильная генерация миниатюр, и если вы удалили файлы в папке \wp-content\cache\thumb  , скрипт который их
создает (class.Kama_Make_Thumb.php) падает с 500 ошибкой и не генерирует.
Таким методом скрипты позволяют сгенерировать временные файлы, так как плагины типа regenerate thumbnails не помогут.


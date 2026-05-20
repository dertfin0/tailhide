# TailHide
TailHide - утилита, которая шифрует и прячет файлы в изображениях по паролю, с возможностью в дальнейшем извлечь 
исходный файл. Предназначена для скрытия факта наличия зашифрованной информации

### Установка

### Использование
Чтобы спрятать файл в изображении:  
```bash
th --hide --image your-photo.png --file secret-file.txt --password your_strong_password
```

Чтобы извлечь спрятанный файл:  
```bash
th --reveal --image your-photo.png --password your_strong_password
```
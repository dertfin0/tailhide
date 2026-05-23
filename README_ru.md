# TailHide
TailHide - утилита, которая шифрует и прячет файлы в изображениях по паролю, с возможностью в дальнейшем извлечь 
исходный файл. Предназначена для скрытия факта наличия зашифрованной информации

- [EN](https://github.com/dertfin0/tailhide/blob/master/README.md)

### Установка

На данный момент <u>готовые</u> сборки tailhide есть <u>только под `x86_64`</u> (amd64)

Если Вы используете Debian/Ubuntu, скачайте со [страницы последнего релиза](https://github.com/dertfin0/tailhide/releases/latest) файл `tailhide.deb` и установите его:
```bash
wget https://github.com/dertfin0/tailhide/releases/download/1.0.0/tailhide.deb
sudo apt install ./tailhide.deb -y
```

Если Вы используете другой дистрибутив, то скачайте `th.tar.gz`, распакуйте его и перенесите бинарный файл в нужную директорию:
```bash
wget https://github.com/dertfin0/tailhide/releases/download/1.0.0/th.tar.gz
tar -xf th.tar.gz
chmod +x ./th
sudo mv th /usr/local/bin/

rm th.tar.gz
```

### Использование
Чтобы спрятать файл в изображении:  
```bash
th --hide --image your-photo.png --file secret-file.txt --password your_strong_password
```

Чтобы извлечь спрятанный файл:  
```bash
th --reveal --image your-photo.png --password your_strong_password
```
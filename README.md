# TailHide
TailHide is a utility that encrypts and hides files in images using a password, with the ability to later retrieve the original file. Designed to hide the presence of encrypted information.

- [RU](https://github.com/dertfin0/tailhide/blob/master/README_ru.md)

### Installation

Currently, tailhide builds are only available for x86_64 (amd64).

If you are using Debian/Ubuntu, download the `tailhide.deb` file from the [latest release page](https://github.com/dertfin0/tailhide/releases/latest) and install it:
```bash
wget https://github.com/dertfin0/tailhide/releases/download/1.0.0/tailhide.deb
sudo apt install ./tailhide.deb -y
```

If you are using a different distribution, download `th.tar.gz`, extract it, and move the binary to the desired directory:
```bash
wget https://github.com/dertfin0/tailhide/releases/download/1.0.0/th.tar.gz
tar -xf th.tar.gz
chmod +x ./th
sudo mv th /usr/local/bin/

rm th.tar.gz
```

### Usage
To hide a file in an image: 
```bash
th --hide --image your-photo.png --file secret-file.txt --password your_strong_password
```

To reveal a hidden file: 
```bash
th --reveal --image your-photo.png --password your_strong_password
```
import os
from cryptography.fernet import Fernet
from base64 import b64encode
import argparse

def get_formatted_password(password: str):
    if len(password) > 32:
        raise ValueError("Password must be 32 or less characters long")

    while len(password) != 32:
        password += " "

    return b64encode(password.encode())

def hide(image: str, secret_file: str, password: str):
    EOF_SEPARATOR = b"th-eof"
    FILENAME_SEPARATOR = b"fn-end"

    enc = Fernet(get_formatted_password(password))

    with open(secret_file, 'rb') as f:
        secret_file_content = f.read()
        secret_file_content = enc.encrypt(secret_file_content)

    with open(image, 'rb') as f:
        image_file_content = f.read()

    os.remove(image)

    with open(image, 'wb') as f:
        f.write(image_file_content + EOF_SEPARATOR + secret_file.encode("utf-8") + FILENAME_SEPARATOR + secret_file_content)

def reveal(image: str, password: str):
    EOF_SEPARATOR = b"th-eof"
    FILENAME_SEPARATOR = b"fn-end"

    enc = Fernet(get_formatted_password(password))

    with open(image, "rb") as f:
        image_file_content = f.read()

    EOF_INDEX = image_file_content.find(EOF_SEPARATOR)
    FILENAME_INDEX = image_file_content.find(FILENAME_SEPARATOR)

    if EOF_INDEX == -1:
        raise IOError()

    filename = image_file_content[EOF_INDEX + len(EOF_SEPARATOR):FILENAME_INDEX].decode("utf-8")
    file_content = image_file_content[FILENAME_INDEX + len(FILENAME_SEPARATOR):]
    file_content = enc.decrypt(file_content)

    with open(filename, 'wb') as f:
        f.write(file_content)

    os.remove(image)
    with open(image, 'wb') as f:
        f.write(image_file_content[:EOF_INDEX])

parser = argparse.ArgumentParser()
parser.add_argument("--hide", help="Hide mode", action='store_true')
parser.add_argument("--reveal", help="Reveal mode", action='store_true')

parser.add_argument("--image", help="Visible wrapper image")
parser.add_argument("--file", help="Secret file to hide")
parser.add_argument("--password", help="Encryption password")

if __name__ == "__main__":
    args = parser.parse_args()
    if (args.hide and args.reveal) or (not args.hide and not args.reveal):
        print("Invalid arguments. Try th --help")
        exit(0)


    if args.hide:
        if args.image and args.file and args.password:
            try:
                hide(args.image, args.file, args.password)
                print("Done")
            except ValueError:
                print("Password must be 32 or less characters long")
        else:
            print("Invalid arguments. Try th --help")
    elif args.reveal:
        if args.image and args.password:
            try:
                reveal(args.image, args.password)
                print("Done")
            except IOError:
                print("No hidden file found")
            except ValueError:
                print("Password must be 32 or less characters long")
            except Exception:
                print("Encryption error. Make sure the password is correct.")
        else:
            print("Invalid arguments. Try th --help")
#!/bin/bash
pip install pyinstaller cryptography
pyinstaller \
	--clean \
	--hidden-import cryptography \
	--exclude-module tkinter --exclude-module unittest \
	--onefile \
	--noupx \
	tailhide.py


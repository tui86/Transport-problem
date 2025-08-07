@echo off
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile main.py
pause

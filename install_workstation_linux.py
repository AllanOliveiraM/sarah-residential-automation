#!/usr/bin python3
# coding: utf-8

'''
MIT License

Copyright (c) 2020 Allan Oliveira Miraballes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from os import system
import sys
import subprocess


def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


def upgrade_pip():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])


def run_pycommand(command):
    subprocess.check_call([sys.executable, command])


def run_command(command):
    subprocess.check_call(command)


def try_pip():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'])
        return True
    except:
        return False


def main():

    # Verifying installed venv's
    try:
        # Try import Lib
        from glob import glob
        if './venv' in glob('./*'):
            venv_installed = True
        else:
            venv_installed = False
    except:
        print("INFO > Can't verify installed venv's in this directory. Continuing installing...")
        venv_installed = False


    # Verifying if pyhton version == 3
    if sys.version_info[0] != 3:
        print('\nIMPORTANT\n\nUse Python 3 to run this project.\nYou can run:\n\npython3 install_workstation.py\n')
        sys.exit()


    # Install & Activate Venv
    if venv_installed == False:
        try:
            run_command(['sudo', 'apt-get', 'install', 'python3-venv'])
        except:
            print('\n\n< ERROR >\n\nInstall Venv python3 module before run this module.\n')
            sys.exit()
        else:
            run_command([sys.executable, '-m', 'venv', 'venv'])
    else:
        pass


    # Verifying if are pip installed and upgraded
    if try_pip() == False:
        system('. venv/bin/activate & python modules/dependency-manager/get-pip.py')
    else:
        upgrade_pip()


    print('\n\nSarah Venv Installed Successfully!\nIf not auto, run this commands to continue install:\n\nsource ./venv/bin/activate\npip install -r requirements.txt\n')


if __name__ == "__main__":
    main()
else:
    print('\n< Ops! >\n\ninstall_workstation.py\n\nThis module cannot be imported. Only run it manually.\n')

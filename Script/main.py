def info():
    print(
        colored(' [*] Your PC/exec. Informations:', 'dark_grey'),

f'''
    Platform:\t\t {platform.system()} - {platform.architecture()[0]}
    Py. Version:\t Python {platform.python_version()[0]}
    
    --pywin32 = \"{version('pywin32')}\" / termcolor = \"{version('termcolor')
}\".\n''')

def show(self):
    info(); self.scanoutput, self.scoutput = check_output(['pnputil', '/enum-devices', '/connected', '/class', 'USB']).decode('windows-1252').split('\n'), []

    for i in self.scanoutput:
        if '\\' in i:
            i = '\\'.join((i.split(':')[1].split(' ')[-1].split('\r')[0]).split('\\')[0:2])
            if 'USB' in i: self.scoutput.append(i)
    
    self.scanoutput = self.scoutput

    for (i, x) in zip(self.scanoutput, range(len(self.scanoutput))):
        print(colored(f' [+] {("0" if x+1 < 10 else "") + str(x+1)}: {self.scanoutput[x]}', 'green'), end='\n')

def main(self):
    '''
    ** MADE WITH/FOR:
        Platform:\t Windows
        Py. Version:\t Python 3
        
        --pywin32 = "306" / termcolor = "2.2.0".
    
    FUNCTION: remove \"USB\\" by The Selection Of The User (by <class 'int'>).

    ** THIS IS A PREVIEW: Don't Check If You Are Admin or Not; Don't Re-connect Devices.
    '''

    try:
        self.show()

        device = int(input('\n [*] Choose One Device To Remove: '))
        assert len(self.scanoutput) >= device > 0, 'Error With Device'
    except Exception as err: input(colored(f'\n {type(err).__name__}: {err}.', 'red')); return

    wmi = win32com.client.GetObject('winmgmts:')
    usb = wmi.InstancesOf("Win32_USBHub")
    ind = len(usb)

    for (usb, ind) in zip(usb, range(ind)):
        dvc = '\\'.join(usb.DeviceID.split('\\')[0:2])
        if dvc == self.scanoutput[device-1]: fnd = usb.DeviceID; break

    try:
        fnd

        if input(f'\n [*] Remove The Device \"{dvc}\"? ').lower() in ('y', 'yes'):
            system('cls'); print(colored('\n [*] Trying To Remove The Device...\n', 'green'))
            system(f'pnputil /remove-device "{fnd}"'); input()

    except NameError: input('\n [*] Device Not Found.')

import win32com.client, platform

from importlib.metadata import version
from subprocess import check_output
from termcolor import colored
from os import system

obj = type('Obj', (object, ), {'show': show, 'main': main})
start = obj()

try:
    while True: system('cls'); help(obj.main); start.main()
except KeyboardInterrupt: exit(0)
except Exception as err: input(colored(f' {type(err).__name__}: {err}.', 'red'))

finally: system('cls')
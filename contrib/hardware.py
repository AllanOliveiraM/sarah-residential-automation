# coding: utf-8


"""Hardware connection module."""


from time import sleep
from collections import deque
from serial import Serial

from contrib.actions import resolveResponse


class Hardware():
    """Hardware: Create object with connection."""

    def __init__(self):
        '''Start new connection with Arduino.
        
        Props: Define Self Connection object.
        '''
        
        __ports = [
            '/dev/ttyUSB0',
            '/dev/ttyUSB1',
            '/dev/ttyUSB2',
            '/dev/ttyUSB3',
            '/dev/ttyUSB4',
            '/dev/ttyUSB5',
            '/dev/ttyUSB6',
        ]
        
        for port, at in zip(__ports, range(len(__ports))):
            try:
                self.connection = Serial(str(port), 9600, timeout=1)
                sleep(1.8)
                print('Hardware Connected.')
                break
            except:
                print('Trying connect with Hardware again. {0} of {1}'.format(
                    at + 1,
                    len(__ports)
                    ))
        else:
            self.connection = None
            
        self._commands = deque([''])


    def start_processing(self):
        """Start processing Arduino Tag Responses."""

        try:
            response = self.connection.readline().decode()
            response = response.replace('\n', '')
            response = response.replace('\r', '')
            if response != '':
                resolveResponse(self, response)
            
            try:
                while True:
                    __next_command = self._commands.popleft()
                    self.write_command(__next_command)
                    sleep(0.3)
            except:
                pass
            
            sleep(0.01)
        except:
            print('No hardware success connection.')
            
            
    def write_command(self, command):
        '''Send new command to Arduino.
        
        Return: Arduino Response.
        '''

        try:
            self.connection.write(command.encode())
            response = self.connection.readline().decode()
            response = response.replace('\n', '')
            response = response.replace('\r', '')
            if response != '':
                resolveResponse(self, response)
            sleep(0.05)
        except:
            print('No hardware success connection.')


    def new_command(self, command):
        """Add new command to processor queue."""
        self._commands.append(command)

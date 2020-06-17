# coding: utf-8


"""Hardware connection module."""


from time import sleep
from serial import Serial
import threading

from contrib.actions import resolveResponse


class Hardware(object):

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


    def __new_thread_run(self, function, funcargs=None):
        '''Run function in new thread.
        
        Function: Function to run in a new thread immediately.
        Funcargs: Function args in a list.
        '''

        __backend_thread = threading.Thread(target=function, args=funcargs)
        __backend_thread.start()


    def start_processing_response(self):
        """Start processing Arduino Tag Responses."""

        try:
            response = self.connection.readline().decode()
            response = response.replace('\n', '')
            response = response.replace('\r', '')
            if response != '':
                resolveResponse(self, response)
        except:
            print('No hardware success connection.')


    def write_command(self, char_):
        '''Send new command to Arduino.
        
        Return: Arduino Response.
        '''

        try:
            self.connection.write(char_.encode())
        except:
            print('No hardware success connection.')

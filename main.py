# coding: utf-8


import threading
from os import mkdir, remove, listdir

from contrib.hardware import Hardware


class Main():
    """Main class to manage Hardware."""
    
    def __init__(self):
        """Start Command manager loop and Hardware Instance."""

        def new_thread_run(function, funcargs=None):
            '''Run a function in new thread.
            
            Function: Function to run in a new thread immediately.
            Funcargs: Function args in a list.
            '''

            __backend_thread = threading.Thread(target=function,
                                                args=funcargs
                                                )
            __backend_thread.start()
        
        
        self.hardware = Hardware()
        
        
        """Create 'queue' folder if not exist."""
        try:
            open('./queue/temp.tmp', 'w')
            remove('./queue/temp.tmp')
        except:
            mkdir('./queue')
        
        
        def processor(self):
            """Command Processor."""
            
            while True:
                _command_tasts = listdir('./queue/')
                
                if _command_tasts != []:
                    _command_tasts.sort()
                    print(_command_tasts)
                
                for command in _command_tasts:
                    command_file = open('./queue/' + command, 'r')
                    command_data = command_file.read()
                    command_file.close()
                    remove('./queue/'+ command)
                    self.hardware.new_command(command_data)
                
                self.hardware.start_processing()
                
        new_thread_run(processor, [self])
            
            
    def command(self, command):
        """Send a new command to Arduino."""
        
        name = 1
        while True:
            
            _command_tasts = listdir('./queue/')
            
            if not str(name) in _command_tasts:
                command_file = open(f'./queue/{name}', 'w')
                command_file.write(command)
                command_file.close()
                break

            name += 1
        

main = Main()

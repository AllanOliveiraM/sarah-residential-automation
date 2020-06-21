# coding: utf-8


"""Actions to Hardware do."""


from time import sleep


def resolveResponse(hardware, response):
    """Resolve Arduino responses."""

    if response == 'SERVER':
        hardware.write_command('T')

    elif response == 'A5:A9:9C:73' or response == 'D0:E5:6D:C1' or response == '5A:2C:77:89':
        hardware.write_command('a')
        sleep(0.5)
        hardware.write_command('b')

    elif response == 'US-INF':
        print('US-INF')

    elif response == 'US-SUP':
        print('US-SUP')
        
    elif response == 'RELE-1-ON':
        print('RELE-1-ON')

    elif response == 'RELE-1-OFF':
        print('RELE-1-OFF')

    elif response == 'RELE-2-ON':
        print('RELE-2-ON')

    elif response == 'RELE-2-OFF':
        print('RELE-2-OFF')
    
    else:
        print('> Unresolved response: ' + str(response))

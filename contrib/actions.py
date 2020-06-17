# coding: utf-8


"""Actions to Hardware do."""


from time import sleep


def resolveResponse(hardware, response):
    """Resolve Arduino responses."""


    if response == 'A5:A9:9C:73':
        hardware.write_command('a')
        sleep(0.5)
        hardware.write_command('b')

    elif response == '5A:2C:77:89':
        hardware.write_command('c')
        sleep(0.5)
        hardware.write_command('d')

    elif response == 'RELE-1-ON':
        print('RELE-1-ON')

    elif response == 'RELE-1-OFF':
        print('RELE-1-OFF')

    elif response == 'RELE-2-ON':
        print('RELE-2-ON')

    elif response == 'RELE-2-OFF':
        print('RELE-2-OFF')

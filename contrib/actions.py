# coding: utf-8


"""Actions to Hardware do."""


from time import sleep


def resolveResponse(hardware, response):
    """Resolve Arduino responses."""


    if response == 'A5:A9:9C:73':
        hardware.write_command('a')
        sleep(2)
        hardware.write_command('b')

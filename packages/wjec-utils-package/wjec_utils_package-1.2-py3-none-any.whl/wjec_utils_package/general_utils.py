"""
Module:     general_utils.py
Package:    ShakeAlert Utilities
Date:       Mar 2020
Updated:    November 2021
Owner:      WJE

Description:
        General utilities for Python ShakeAlert code.
"""
import time
from signal import signal, SIGINT
from platform import system
from os import devnull, path
from subprocess import call as subprocess_call
from platform import system as platform_system


def sleep_loop(length,
               division=1):
    """
    Function to run a series of 1 second sleeps.
    This allows signal interruptions (such as shutdowns) to be caught every wake up cycle.
    :param division:
    :param length: number of seconds to sleep for
    :return:
    """
    counter_max = int(length / division)
    for counter in range(0, counter_max):
        time.sleep(division)


def sleep_delay(delay_sec,
                start_time=time.time(),
                division=1):
    """
    Function to sleep until a specific amount of time has passed.
    You can set the origin of that 'specific time' using the 'start_time' parameter
    :param delay_sec: float - the time in seconds to delay
    :param start_time: time.time() - when to start counting from
    :param division: float - the granularity desired (in seconds)
    :return:
    """
    while time.time() < start_time + delay_sec:
        time.sleep(division)



def connection_check_network(host_address,
                             network_pings=1):
    """
    Ping the server at host_address to determine if internet is available.
    Code has been taken from:
    "https://stackoverflow.com/questions/2953462/pinging-servers-in-python"
    # TODO: pipe contents /dev/null
    """
    param = '-n' if platform_system().lower() == 'windows' else '-c'
    command = ['ping',
               param,
               str(network_pings),
               host_address]
    with open(devnull, 'w') as DEVNULL:
        return subprocess_call(command, stdout=DEVNULL) == 0


def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    # for t in threading.enumerate():
    #    print(str(t)) # ensure all t's are daemons
    exit(0)


def enable_kbd_interrupt(kbd_interrupt_handler):
    """
    enable the program execution to be interrupted by Ctrl-C.
    Pass as an argument, a function which takes two arguments: signal, frame
    :param kbd_interrupt_handler: function - used to handle the interrupt
    :return:
    """
    signal(SIGINT, kbd_interrupt_handler)


def enable_signal_interrupt(signal_code, interrupt_handler):
    """
    Enable generic handling of process signals.
    The function 'interrupt_handler' must take two arguments, 'signal' and 'frame'
    :param signal: signal.SIGNAL type - the signal to be handled (e.g. SIGINT, SIGTERM, SIGKILL)
    :param interrupt_handler: function - the handle to a function to be called from the signal
    :return:
    """
    signal(signal_code, interrupt_handler)


def get_log_dir(shakealert_path):
    """
    Generate the log directory
    :param shakealert_path:
    :return:
    """
    if system() == 'Linux':
        return path.join(shakealert_path, 'log')
    else:
        return 'log'

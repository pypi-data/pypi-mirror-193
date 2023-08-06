"""
Module:   logging_util.py
Package:  varius/util
Date:     Mar 2020
Owner:    WJE

Description:  The wrapper for the logger used for the ShakeAlert software.

              The logging utility uses the python package 'logging' to create a logger
              with proper formatting and handling.
              Note that loggers do no need to be passed into new modules during construction,
              Instead, having once initialized the desired logger with name <name>, a handle
              can be created from anywhere in the program by importing 'logging' and making
              a call to logging.getLogger(<name>)
"""

from os import getcwd, makedirs
from os.path import join, split, exists
from platform import system
import logging
from logging.handlers import RotatingFileHandler


def get_log_dir(shakealert_path):
    """
    Generate the log directory
    :param shakealert_path:
    :return:
    """
    if system() == 'Linux':
        return join(shakealert_path, 'log')
    else:
        return 'log'


def log_formatter(log_format):
    """
    Utility to allow easy choice of logging formats.
    Example message lines:
        default:    2020-03-17 10:45:45,762 - auxTest - ERROR - This is an example message
        statistics: 2020-03-17 10:46:46,482 - This is an example message
        debugging:  2020-03-17 10:46:21,901 - auxTest - 49 - ERROR - This is an example message
        console:    2020-03-17 10:44:15,822 - Test_logger - ERROR - This is an example message
        scas:       2020-03-17 10:44:16     This is an example message
    :param log_format: string - the input format, selected from the dictionary
    :return: The format string associated with the input format.
    """
    format_options = {'default': '%(asctime)s    %(levelname)-8s %(message)s',
                      'statistics': '%(asctime)s - %(message)s',
                      'debugging': '%(asctime)s - %(module)-14s - %(lineno)3s - %(levelname)s - %(message)s',
                      'console': '%(asctime)s - %(name)10s - %(levelname)-8s - %(message)s',
                      'scas': '%(asctime)s   %(message)s'}
    try:
        return format_options[log_format]
    except Exception:
        return format_options['default']


def datetime_formatter(dtformat,
                       UTC=False):
    """
    Utility to allow easy choice of date and tim format for logging
    Example datetime formats:
        default: 2020-03-17 10:45:45,762
        character: 2020 Mar 17 10:45:45
        short: 2020-03-17 10:45:45
        short, with UTC: 2020-03-17 10:45:45 UTC
    UTC=yes options appends 'UTC' to the end of the datetime string
    :param dtformat: string - any of the above example values
    :param UTC: boolean - append the string 'UTC' to the end of the format
    :return:
    """
    format_options = {'default': None,
                      'character': '%Y %b %d %H:%M:%S',
                      'short': '%Y-%m-%d %H:%M:%S'}
    try:
        format = format_options[dtformat]
    except KeyError:
        return format_options['default']
    if format and UTC:
        format += ' UTC'
    return format


def level_formatter():
    """
    Returns a logging level based on the configuration input.
    :return:
    """
    pass        # TODO, implement


def create_logger(log_name,
                  filename,
                  log_format='default',
                  datetime_format='default',
                  show_UTC=False,
                  level='default',
                  rotation_type='default',
                  max_size=8388608,
                  backup_count=5):
    """
    Creates an object of type logging with the parameters specified by the user.
    This function is called to create a new log file.
    Putting the 'log_name' in the form <parent>.<child> will make the logger
    a child of the parent logger, making messages appear in both based on the heirarchy.
    :param log_name: string - Name of the log, used to get the object handle
    :param filename: string - Filename of the log
    :param log_format: string - Format of the log ('default','statistics','debugging','console')
    :param datetime_format: string - Format of the datetime ('default','character','short')
    :param show_UTC: boolean - Append the word 'UTC' to the timestamp
    :param level: Level of the logger (logging.DEBUG,INFO,WARNING,ERROR,CRITICAL)
    :param rotation_type: Either 'default', which rotates, otherwise none
    :param max_size: int - max size of log file
    :param backup_count: int - number of backup log fies to keep
    :return: Handle to the newly created log
    """
    formatter = log_formatter(log_format)  # Get the formatter string (log_formatter function)
    dt_formatter = datetime_formatter(datetime_format, UTC=show_UTC)
    if level == 'default':
        level = logging.INFO
    if rotation_type == 'default':
        rotation_type = 'rotating'
    log_directory, log_filename = split(filename)
    if not log_directory:
        log_directory = getcwd()
    file_path = join(log_directory,
                     log_filename)  # Get the log file full filepath
    if not exists(log_directory):
        makedirs(log_directory)
    log = setup_logger(log_name,
                       file_path,
                       formatter,
                       dt_formatter,
                       level,
                       rotation_type,
                       max_size,
                       backup_count)
    return log


def setup_logger(log_name,
                 file_path,
                 format,
                 datetime_format,
                 level,
                 rotation_type,
                 max_size,
                 backup_count):
    """
    Used to setup the logger, called by create_logger function.
    Separated from create_logger for clarity.
    Do not use this function on its own.
    """
    log = logging.getLogger(log_name)
    if rotation_type == 'rotating':
        file_handler = RotatingFileHandler(file_path,
                                           maxBytes=max_size,
                                           backupCount=backup_count)
    else:
        file_handler = logging.FileHandler(file_path)
    formatter = logging.Formatter(format, datefmt=datetime_format)
    file_handler.setFormatter(formatter)
    try:
        log.setLevel(level)
    except Exception as e:
        log.setLevel(logging.INFO)
    log.addHandler(file_handler)
    return log


def add_console_log(log_handle):
    """
    Adds a console logger to the log specified by 'log_handle'.
    If a console logger is added to both parent and child in a logger hierarchy,
    the logged message will appear twice if sent to the child.
    :param log_handle: string - the log name which is desired to log to console.
    :return:
    """
    log_handle.addHandler(logging.StreamHandler())

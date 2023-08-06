"""
Module:   sys_const
Package:  N/A
Date:     July 2020
Owner:    WJE

Description:  A module for system wide constant expressions
"""

#
# General system-wide constants
#
CONFIG_FILE_NAME = '/home/varius/config.ini'

SECONDS_PER_DAY = 86400
CONFIG_RELAY_MAGNITUDES = 'Relay Magnitudes'
CONFIG_GPS = 'GPS'
CONFIG_MODBUS = 'Modbus'
CONFIG_MAIL = 'Mail'
CONFIG_STOMP = 'Stomp'
CONFIG_ACCEL = 'Accel'

MAX_UDP_PACKET_SIZE = 2048

#
# Device configurations
#
UNIT_INFO_KEYS = ["Latitude", "Longitude", "Site name",
                  "Hard threshold", "Soft threshold"]

PING_HOST = '8.8.8.8'  # 8.8.8.8 is google

STATE_MACHINE_PING_TIME_SEC = 20.0

CONSOLE_LOGGER = 'console'
DEBUGGER_LOGGER = 'debugger'
STATS_LOGGER = 'stats'

#TIMEZONES = {0: "Pacific",  # TODO: put timezone select in config.ini
#             1: "Mountain",
#             2: "Central"}
#MESSAGE_PARAMETERS = {0: '%(site-name)',
#                      1: '%(date)',
#                      2: '%(time-utc)',
#                      3: '%(time-tz)',
#                      4: '%(magnitude)'}  # currently unused, will be used for email templates
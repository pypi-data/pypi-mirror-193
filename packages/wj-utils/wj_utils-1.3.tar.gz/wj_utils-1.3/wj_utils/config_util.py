"""
Module:     config_util.py
Package:    ShakeAlert Utilities
Date:       November 2021
Updated:
Owner:      WJE

Description:
        Utilities for reading and parsing configuration files on the ShakeAlert devices.
        These are specific to the flat text format configuration files.

        Added functionality (Nov 2021) will be needed to read zipped configurations.
"""
import configparser
from configparser import ConfigParser
from zipfile import ZipFile
from io import TextIOWrapper
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
import sys

from wj_utils import sys_const

SYS_CONFIG_ZIP = "config.zip"


def get_configs(config_file_name):
    cfg_file = config_file_name
    config = ConfigParser()
    config.optionxform = str
    config.read(cfg_file)
    return config


def get_logging_level(level):
    """
    Get a logging level from the level in a configuration file
    :param level: string - the level to use
    :return: logging.level
    """
    logging_levels = {'DEBUG': DEBUG,
                      'INFO': INFO,
                      'WARNING': WARNING,
                      'ERROR': ERROR,
                      'CRITICAL': CRITICAL}
    try:
        return logging_levels[level]
    except KeyError:
        return INFO


def get_client_configs():
    cfg_file = sys_const.CONFIG_FILE_NAME
    # Parse configuration file
    # if len(sys.argv) > 1:  # Count command line arguments
    #     cfg_file = str(sys.argv[1])  # Get command line argument: config.ini's path
    config_ini = ConfigParser()
    config_ini.optionxform = str # use a case-sensitive INI parser
    config_ini.read(cfg_file)
    return build_client_config(config_ini), cfg_file


def build_client_config(config_ini):
    """
    Build and return a sys. configuration.
    Is used by 'get_sys_configs()' function.
    :param config_ini: ConfigParser object containing the client configurations
    :return:
    """
    configurations = {"Soft Threshold": float(config_ini[sys_const.CONFIG_RELAY_MAGNITUDES]["Soft"]),
                      "Hard Threshold": float(config_ini[sys_const.CONFIG_RELAY_MAGNITUDES]["Hard"]),
                      "Min Likelihood": float(config_ini[sys_const.CONFIG_RELAY_MAGNITUDES]["Min Likelihood"]),
                      "Latitude": float(config_ini[sys_const.CONFIG_GPS]["Lat"]),
                      "Longitude": float(config_ini[sys_const.CONFIG_GPS]["Lon"]),
                      "Slave ID": int(config_ini[sys_const.CONFIG_MODBUS]["Slave ID"]),
                      "Site Name": str(config_ini[sys_const.CONFIG_MAIL]["Site Name"]),
                      "Admin Group": str(config_ini[sys_const.CONFIG_MAIL]["Admin"]),
                      "Status Group": str(config_ini[sys_const.CONFIG_MAIL]["Status"]),
                      "Alarm Group": str(config_ini[sys_const.CONFIG_MAIL]["Alarm"]),
                      "USGS Username": str(config_ini[sys_const.CONFIG_STOMP]["User"]),
                      "USGS Password": str(config_ini[sys_const.CONFIG_STOMP]["Pass"]),
                      "Accel Enabled": str(config_ini[sys_const.CONFIG_ACCEL]["Enabled Y/N"])}
    return configurations


def get_sys_config(zip_file="/root/shakealert/conffiles/config.zip",
                   config_file="config.txt"):
    """
    Function to read and return the system configuration file of an OmniMonitor ShakeAlert.
    :param zip_file: str - the filepath of the configuration archive
    :param config_file: str - the name of the configuration file within the zip archive
    :return:
    """
    config_parser = configparser.ConfigParser()
    sys_config_zip = zip_file
    with ZipFile(sys_config_zip) as config_zip:
        sys_config_bin = config_zip.open(config_file)
        sys_config = TextIOWrapper(sys_config_bin)
        config_parser.read_file(sys_config)
    return config_parser


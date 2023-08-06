#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging.handlers
import os
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_directory_path = os.getcwd() + '/logs'
if not os.path.exists(log_directory_path):
    os.makedirs(log_directory_path)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

rotating_file_handler = logging.handlers.TimedRotatingFileHandler(str(log_directory_path) + '/' + 'sp.log',
                                                       when='midnight',
                                                       interval=1,
                                                       backupCount=7,
                                                       atTime=datetime.time(0, 0, 0, 0))
rotating_file_handler.setFormatter(formatter)
logger.addHandler(rotating_file_handler)


# date_str = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
# log_file = (str(log_directory_path) + '/' + date_str + '.log')
# f_handler = logging.FileHandler(log_file)
# f_handler.setLevel(logging.DEBUG)
# f_handler.setFormatter(formatter)


def debug(msg):
    logger.debug('=====> ' + str(msg))


def info(msg):
    logger.info('=====> ' + str(msg))


def warning(msg):
    logger.warning('=====> ' + str(msg))


def error(msg):
    logger.error('=====> ' + str(msg))


if __name__ == '__main__':
    debug('logging')
    info('logging')
    warning('logging')
    error('logging')

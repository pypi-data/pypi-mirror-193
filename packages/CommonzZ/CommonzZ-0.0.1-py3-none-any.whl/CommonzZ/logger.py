#!/usr/bin/env python
# encoding: utf-8
__author__ = 'l9h8'
__time__ = '2020/9/3 4:33 PM'

import sys

from loguru import logger

logger.remove()
logger.add(sys.stdout,
           format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>')


def thin_log():
    logger.remove()
    logger.add(sys.stdout,
               format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level>| - <level>{message}</level>')


if __name__ == '__main__':
    thin_log()
    logger.info("1234567890")

__all__ = ["logger", "thin_log"]

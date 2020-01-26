#!/usr/bin/env python

import logging
import logging.config
from logging.handlers import RotatingFileHandler
import os


def setup_log():
    if not os.path.exists('log'):
        os.mkdir('log')

    formatter = '%(asctime)s,[%(levelname)s],%(module)s,%(name)s,%(message)s'
    logging.basicConfig(
        level=logging.DEBUG,
        format=formatter,
        handlers=[RotatingFileHandler(filename="log/app.log", maxBytes=100000, backupCount=10)]
    )


if __name__ == "__main__":
    setup_log()
    logger = logging.getLogger(__name__)
    logger.info('%s %s', 'test', 'test')

    logger.critical('critical')
    logger.error('error')
    logger.warning('warning')
    logger.info('info')
    logger.debug('debug')

    logging.debug('sample2')

#!/usr/bin/env python

import logging
import os


def setup_log():
    if not os.path.exists('log'):
        os.mkdir('log')

    # フォーマットを定義
    formatter = '%(asctime)s,[%(levelname)s],%(module)s,%(name)s,%(message)s'
    logging.basicConfig(filename="log/app.log", level=logging.DEBUG, format=formatter)


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

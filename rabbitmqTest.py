import pika
from loguru import logger

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
logger.add('web.log')
logger.debug('hello')
logger.info('world')
logger.warning('1')
logger.error('2')
logger.info('3')
logger.success('4')
logger.critical('5')

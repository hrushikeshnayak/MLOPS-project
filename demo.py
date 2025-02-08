from US_Visa.logger import logging
# logging.info('welcome to our custom log')
import sys 

from US_Visa.exception import USvisaException
try:
    a = 2/0
except Exception as e:
    raise USvisaException( e , sys )

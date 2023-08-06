
import os
import sys
cwd = os.path.abspath(os.getcwd())
include_path = f"{cwd}"
sys.path.append(include_path)
from it_eng_python_logger_utils_dev_pypi_test.logger_utils import LoggerHelper
import json
logger = LoggerHelper("test")

logger.info("you done gone did it")
logger.info("{'test':'test'}")
test = '{"testing":"test"}'
logger.info('{"test":"test"}')
testing = json.loads(test)
logger.info(testing)
logger.info('{"testing":"test"}')
import unittest
from io import StringIO
from datetime import datetime

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename=datetime.now().strftime("%Y%m%d%H%M%S") + '.log',
                    format="%(asctime)s - [%(threadName)-12.12s] - [%(levelname)-5.5s] - %(message)s",
                    filemode='w')
logger = logging.getLogger()


class LogCaptureResult(unittest._TextTestResult):

    def _exc_info_to_string(self, err, test):
        # jack into the bit that writes the tracebacks, and add captured log
        tb = super(LogCaptureResult, self)._exc_info_to_string(err, test)
        captured_log = test.stream.getvalue()
        return '\n'.join([tb, 'CAPTURED LOG', '=' * 70, captured_log])


class LogCaptureRunner(unittest.TextTestRunner):

    def _makeResult(self):
        # be nice if TextTestRunner just had a class attr for defaultResultClass
        return LogCaptureResult(self.stream, self.descriptions, self.verbosity)


class BaseTestCase(unittest.TestCase):

    def setUp(self, *args, **kwargs):
        super(BaseTestCase, self).setUp(*args, **kwargs)
        # create a in memory stream
        self.stream = StringIO()
        # add handler to logger
        self.handler = logging.StreamHandler(self.stream)
        logger.addHandler(self.handler)

    def tearDown(self, *args, **kwargs):
        super(BaseTestCase, self).tearDown(*args, **kwargs)
        # we're done with the caputre handler
        logger.removeHandler(self.handler)

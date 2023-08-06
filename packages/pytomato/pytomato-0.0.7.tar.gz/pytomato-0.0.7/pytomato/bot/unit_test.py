import os
import unittest

from .config import *
from .tokens import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        BotConfig.config(
            app_name='LiveCore Deliver',
            app_id=os.environ.get('LIVECORE_DELIVER_APP_ID'),
            app_secret=os.environ.get('LIVECORE_DELIVER_APP_SECRET'),
            base_url='https://fsopen.bytedance.net'
        )

    def test_bot_token(self):
        for i in range(1, 100):
            token = BotToken().get()
            self.assertIsNotNone(token)


if __name__ == '__main__':
    unittest.main()

# encoding:utf-8
import time

import requests

from ..base import ExpirationData, Singleton
from .config import BotConfig

__all__ = ['BotToken']


@Singleton
class BotToken(ExpirationData[str]):

    def refresh(self) -> str:
        url = f'{BotConfig.base_url}/open-apis/auth/v3/app_access_token/internal'
        params = {
            'app_id': BotConfig.app_id,
            'app_secret': BotConfig.app_secret
        }
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        res = requests.post(url, params=params, headers=headers)
        data = res.json()
        token = data['app_access_token']
        cur_ts = int(time.time())
        self.expire_ts = cur_ts + data['expire']
        return f'Bearer {token}'

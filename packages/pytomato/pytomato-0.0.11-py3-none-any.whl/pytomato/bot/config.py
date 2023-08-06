# encoding:utf-8

__all__ = ['BotConfig']


class BotConfig:
    app_name: str = None
    app_id: str = None
    app_secret: str = None
    base_url: str = None

    @classmethod
    def config(cls, app_name: str, app_id: str, app_secret: str, base_url: str):
        r"""
        机器人配置，在使用相关功能之前需要先配置参数
        :param app_name: 应用名称
        :param app_id: 应用app_id
        :param app_secret: 应用app_secret
        :param base_url 飞书开放平台open api域名（内部有公网收敛）
        :return:
        """
        cls.app_name = app_name
        cls.app_id = app_id
        cls.app_secret = app_secret
        cls.base_url = base_url

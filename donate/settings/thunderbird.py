from .environment import app, env


class ThunderbirdOverrides(object):
    INSTALLED_APPS = ['donate.thunderbird']
    TEMPLATES_DIR = [app('thunderbird/templates')]
    POST_DONATE_NEWSLETTER_URL = env("POST_DONATE_NEWSLETTER_URL")

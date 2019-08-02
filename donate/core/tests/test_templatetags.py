from django.test import TestCase, RequestFactory

from ..templatetags.util_tags import format_currency, get_localized_currency_symbol


class UtilTagsTestCase(TestCase):
    """
    These are integration tests that sanity check the output of key template tags.
    """

    def setUp(self):
        self.request = RequestFactory().get('/')

    def test_format_currency_usd_en_us(self):
        self.request.LANGUAGE_CODE = 'en-US'
        ctx = {
            'request': self.request
        }
        value = format_currency(ctx, 'usd', 1)
        self.assertEqual(value, '$1')

    def test_format_currency_usd_en_us_decimal(self):
        self.request.LANGUAGE_CODE = 'en-US'
        ctx = {
            'request': self.request
        }
        value = format_currency(ctx, 'usd', 1.5)
        self.assertEqual(value, '$1.5')

    def test_format_currency_usd_en_gb(self):
        self.request.LANGUAGE_CODE = 'en-GB'
        ctx = {
            'request': self.request
        }
        value = format_currency(ctx, 'usd', 1)
        self.assertEqual(value, 'US$1')

    def test_format_currency_aed_en_us(self):
        self.request.LANGUAGE_CODE = 'en-US'
        ctx = {
            'request': self.request
        }
        value = format_currency(ctx, 'aed', 1)
        self.assertEqual(value, 'Dhs1')

    def test_format_currency_aed_ar(self):
        self.request.LANGUAGE_CODE = 'ar'
        ctx = {
            'request': self.request
        }
        value = format_currency(ctx, 'aed', 1)
        self.assertEqual(value, 'د.إ1')

    def test_get_localised_symbol_usd_en_us(self):
        self.request.LANGUAGE_CODE = 'en-US'
        ctx = {
            'request': self.request
        }
        value = get_localized_currency_symbol(ctx, 'usd')
        self.assertEqual(value, '$')

    def test_get_localised_symbol_usd_en_gb(self):
        self.request.LANGUAGE_CODE = 'en-GB'
        ctx = {
            'request': self.request
        }
        value = get_localized_currency_symbol(ctx, 'usd')
        self.assertEqual(value, 'US$')

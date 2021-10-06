# -*- coding: utf-8 -*-

"""
Test cases for the inputs.
"""
from unittest import TestCase

from ..fields import MultiUploadMetaInput


NO_MATTER = None


class MultiUploadMetaInputTestCase(TestCase):
    """
    Test multi upload input widget
    """

    def test_returns_none(self):
        """value_from_datadict returns none if no file with name provided"""
        sut = MultiUploadMetaInput()

        files = {}

        value = sut.value_from_datadict(NO_MATTER, files, 'non-existing')

        self.assertIsNone(value)

    def test_returns_wrapped_scalar(self):
        """value_from_datadict wraps scalar"""
        sut = MultiUploadMetaInput()

        files = {'scalar': 'value'}

        value = sut.value_from_datadict(NO_MATTER, files, 'scalar')

        self.assertEqual(value, ['value'])

    def test_returns_list_value(self):
        """value_from_datadict returns list directly"""
        sut = MultiUploadMetaInput()

        files = {'list': ['value']}

        value = sut.value_from_datadict(NO_MATTER, files, 'list')

        self.assertEqual(value, ['value'])

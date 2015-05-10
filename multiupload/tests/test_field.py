from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .utils import UploadTestForm


class MinMaxNumTestCase(TestCase):
    """
    Test minimum / maximum file upload count validation
    """

    def setUp(self):
        self.attachment = SimpleUploadedFile(
            'test.txt',
            'test content'.encode('utf-8')
        )

    def test_min_num_none(self):
        """Zero uploaded files (not enough files)"""
        form = UploadTestForm({}, {})
        self.assertFalse(form.is_valid())

    def test_min_num_one(self):
        """One upload file (allowed)"""
        form_files = {'attachments': [self.attachment]}
        form = UploadTestForm({}, form_files)
        self.assertTrue(form.is_valid())

    def test_min_max_num_two(self):
        """Two uploaded files (allowed)"""
        form_files = {'attachments': [self.attachment] * 2}
        form = UploadTestForm({}, form_files)
        self.assertTrue(form.is_valid())

    def test_max_num_three(self):
        """Three uploaded files (allowed)"""
        form_files = {'attachments': [self.attachment] * 3}
        form = UploadTestForm({}, form_files)
        self.assertTrue(form.is_valid())

    def test_max_num_four(self):
        """Four uploaded files (too many)"""
        form_files = {'attachments': [self.attachment] * 4}
        form = UploadTestForm({}, form_files)
        self.assertFalse(form.is_valid())

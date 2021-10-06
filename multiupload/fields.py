# -*- coding: utf-8 -*-

"""
This module contains form fields to work with.
"""

from django import forms
from django.core.exceptions import ValidationError, FieldError
from django.utils.translation import gettext_lazy as _

# Feel free to extend this, see
# http://www.iana.org/assignments/media-types/media-types.xhtml
MEDIA_TYPES = ['image', 'audio', 'video']


class MultiUploadMetaInput(forms.ClearableFileInput):
    """ HTML5 <input> representation. """

    def __init__(self, *args, **kwargs):
        self.multiple = kwargs.pop('multiple', True)
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        if self.multiple:
            if not attrs:
                attrs = {}
            attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs, renderer)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        value = files.get(name)
        if value is None or isinstance(value, list):
            return value
        return [value]


class MultiUploadMetaField(forms.FileField):
    """ Base class for the all media types classes. """

    default_error_messages = {
        'min_num': _(
            u'Ensure at least %(min_num)s files are '
            u'uploaded (received %(num_files)s).'),
        'max_num': _(
            u'Ensure at most %(max_num)s files '
            u'are uploaded (received %(num_files)s).'),
        'file_size': _(
            u'File %(uploaded_file_name)s '
            u'exceeded maximum upload size.'),
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('max_file_size', None)
        self.widget = MultiUploadMetaInput(
            attrs=kwargs.pop('attrs', {}),
            multiple=(self.max_num is None or self.max_num > 1),
        )

        if self.min_num == 0:
            kwargs['required'] = False
        super().__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        data = data or []
        for item in data:
            i = super().to_python(item)
            if i:
                ret.append(i)
        return ret

    def validate(self, value):
        super().validate(value)

        num_files = len(value)
        if num_files and not value[0]:
            num_files = 0

        if not self.required and num_files == 0:
            return

        if num_files < self.min_num:
            raise ValidationError(
                self.error_messages['min_num'] % {
                    'min_num': self.min_num,
                    'num_files': num_files,
                }
            )

        if self.max_num and num_files > self.max_num:
            raise ValidationError(
                self.error_messages['max_num'] % {
                    'max_num': self.max_num,
                    'num_files': num_files,
                }
            )

        for uploaded_file in value:
            if (self.maximum_file_size and
                    uploaded_file.size > self.maximum_file_size):
                raise ValidationError(
                    self.error_messages['file_size'] % {
                        'uploaded_file_name': uploaded_file.name,
                    }
                )


class MultiFileField(MultiUploadMetaField):
    """ Handles plain files. """


class MultiMediaField(MultiUploadMetaField):
    """ Handles multimedia files."""

    error_messages = {
        'wrong_type': _(
            u'Invalid media_type. Valid types are: %(valid_types)s')
    }

    def __init__(self, *args, **kwargs):
        self.media_type = kwargs.pop('media_type', 'image')

        if self.media_type not in MEDIA_TYPES:
            raise FieldError(
                self.error_messages['wrong_type'] % {
                    'valid_types': ', '.join(MEDIA_TYPES),
                }
            )

        kwargs.update({
            'attrs': {
                'accept': '{0}/*'.format(self.media_type),
            }
        })
        super().__init__(*args, **kwargs)


class MultiImageField(MultiMediaField, forms.ImageField):
    """ Handles multiple image uploads, requires Pillow to be installed. """

    def __init__(self, *args, **kwargs):
        kwargs.update({'media_type': 'image'})
        super().__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        for item in data:
            i = forms.ImageField.to_python(self, item)
            if i:
                ret.append(i)
        return ret

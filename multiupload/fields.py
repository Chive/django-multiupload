# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError, FieldError
from django.utils.translation import ugettext_lazy as _

# feel free to extend this, see
# http://www.iana.org/assignments/media-types/media-types.xhtml
MEDIA_TYPES = ['image', 'audio', 'video']

class MultiUploadMetaInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None):
        attrs['multiple'] = 'multiple'
        return super(MultiUploadMetaInput, self).render(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            value = files.get(name)
            if isinstance(value, list):
                return value
            else:
                return [value]

class MultiUploadMetaField(forms.FileField):
    default_error_messages = {
        'min_num': _(u'Ensure at least %(min_num)s files are uploaded (received %(num_files)s).'),
        'max_num': _(u'Ensure at most %(max_num)s files are uploaded (received %(num_files)s).'),
        'file_size': _(u'File %(uploaded_file_name)s exceeded maximum upload size.'),
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('max_file_size', None)
        self.widget = MultiUploadMetaInput(attrs = kwargs.pop('attrs', {}))
        super(MultiUploadMetaField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        data = data or []
        for item in data:
            i = super(MultiUploadMetaField, self).to_python(item)
            if i:
                ret.append(i)
        return ret

    def validate(self, data):
        super(MultiUploadMetaField, self).validate(data)
        num_files = len(data)
        if len(data) and not data[0]:
            num_files = 0
        if not self.required and num_files == 0:
            return
        if num_files < self.min_num:
            raise ValidationError(self.error_messages['min_num'] % {'min_num': self.min_num, 'num_files': num_files})
        elif self.max_num and num_files > self.max_num:
            raise ValidationError(self.error_messages['max_num'] % {'max_num': self.max_num, 'num_files': num_files})
        for uploaded_file in data:
            if self.maximum_file_size and uploaded_file.size > self.maximum_file_size:
                raise ValidationError(self.error_messages['file_size'] % {'uploaded_file_name': uploaded_file.name})

class MultiMediaInput(MultiUploadMetaInput):
    pass

class MultiFileInput(MultiUploadMetaField):
    pass

class MultiMediaField(MultiUploadMetaField):
    error_messages = {
        'wrong_type': _(u'Invalid media_type. Valid types are: %(valid_types)s')
    }

    def __init__(self, *args, **kwargs):
        self.media_type = kwargs.pop('media_type', 'image')

        if self.media_type not in MEDIA_TYPES:
            raise FieldError(self.error_messages['wrong_type'] % {'valid_types': ', '.join(MEDIA_TYPES)})

        kwargs.update({ 'attrs': {'accept': '{0}/*'.format(self.media_type)} })
        super(MultiMediaField, self).__init__(*args, **kwargs)

class MultiFileField(MultiUploadMetaField):
    pass

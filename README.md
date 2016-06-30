# Django Multiupload

[![Build Status](https://travis-ci.org/Chive/django-multiupload.svg?branch=master)](https://travis-ci.org/Chive/django-multiupload)


Dead simple drop-in multi file upload field for django forms using HTML5's ``multiple`` attribute.

## Installation

* Install the package using pip (or easy_install if you really have to)

```bash
$ pip install django-multiupload
```

* Or directly from this repository to get the development version (if you're feeling adventurous)

```bash
$ pip install -e git+https://github.com/Chive/django-multiupload.git#egg=multiupload
```

## Usage

Add the form field to your form and make sure to save the uploaded files in the form's ``save`` method.

For more detailed examples visit the [examples section](https://github.com/Chive/django-multiupload/tree/master/examples).


```python
# forms.py
from django import forms
from multiupload.fields import MultiFileField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
    attachments = MultiMediaField(
        min_num=1, 
        max_num=3, 
        max_file_size=1024*1024*5, 
        media_type='video'  # 'audio', 'video' or 'image'
    )

    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
```

The latter two options just add fancy attributes to HTML's `<input>`, restricting the scope to corresponding filetypes.

```python
# models.py
from django.db import models

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments')

```

```python
# views.py
from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)

```

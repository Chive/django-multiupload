# Django Multiupload

Simple drop-in multi file upload field for django forms using HTML5's ``multiple`` attribute.

## Installation

* Install the package using pip (or easy_install if you really have to)

```sh
$ pip install django-multiupload
```

* .. or directly from this repository the get the development version (if you're feeling adventurous)

```sh
$ pip install -e git+https://github.com/Chive/django-multiupload.git#egg=multiupload
```

## Usage

* Add the form field to your form and make sure to save the uploaded files in the form's ``save`` method

```python
from multiupload.fields import MultiFileField


class MyUploadForm(forms.Form):
	attachments = MultiFileField(max_num=3, min_num=1, max_file_size=1024*1024*5)
	...

    def save(self, commit=True):
        super(MyUploadForm, self).save(commit=commit)

        for each in self.cleaned_data['attachments']:
            att = Attachment(parent=self.instance, file=each)
            att.save()

        return self.instance
```

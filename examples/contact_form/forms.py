from django import forms

from multiupload.fields import MultiFileField

from .models import Message, Attachment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author_name', 'author_email', 'content']  # not attachments!

    files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, message=instance)

        return instance

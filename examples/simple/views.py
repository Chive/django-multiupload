from django.views.generic.edit import FormView
from django.urls import reverse

from .forms import UploadForm
from .models import Attachment


class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:simple_attachment_changelist')

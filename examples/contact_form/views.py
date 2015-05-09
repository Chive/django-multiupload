from django.views.generic.edit import FormView, CreateView

from .forms import ContactForm
from .models import Message


class ContactView(CreateView):
    model = Message
    form_class = ContactForm
    template_name = 'contact_form/form.html'
    success_url = '?success'

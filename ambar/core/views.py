from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import DataForm
from .tasks import process_submission

class IndexView(TemplateView):
    template_name = "index.html"

class DataFormView(FormView):
    template_name = "data_form.html"
    form_class = DataForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        process_submission.send(form.cleaned_data["content"])
        return super().form_valid(form)

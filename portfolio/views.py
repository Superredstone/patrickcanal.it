from django.views.generic import TemplateView

from portfolio import models


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {"job_experiences": models.JobExperience.objects.all().order_by("-start")}

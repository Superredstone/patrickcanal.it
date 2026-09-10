from django.views.generic import ListView, TemplateView

from portfolio import models


class PortfolioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {
            "job_experiences": models.JobExperience.objects.all().order_by("-start")
        }


class ProjectList(ListView):
    template_name = "project_list.html"
    model = models.Project

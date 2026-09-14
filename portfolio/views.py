from django.conf import settings
from django.http.response import FileResponse, HttpResponseBadRequest
from django.utils.translation import gettext as _
from django.views.generic import DetailView, ListView, TemplateView
from post_office import mail

from portfolio import forms, models


class PortfolioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        contact_form = forms.ContactForm()
        return {
            "job_experiences": models.JobExperience.objects.all().order_by("-start"),
            "contact_form": contact_form,
        }


class ProjectList(ListView):
    template_name = "project_list.html"
    model = models.Project


class ContactSend(TemplateView):
    template_name = "contact_thanks.html"

    def post(self, request, *args, **kwargs):
        form = forms.ContactForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest(_("Invalid request"))

        mail.send(
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"],
            sender=settings.EMAIL_HOST_USER,
            cc=form.cleaned_data["email"],
            recipients=[settings.EMAIL_CONTACT],
        )

        return super().get(request, *args, **kwargs)


class CompanyLogo(DetailView):
    model = models.Company

    def get(self, request, *args, **kwargs):
        company = self.get_object()
        return FileResponse(company.logo)

from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    name = models.CharField(
        verbose_name=_("Company"), max_length=255, blank=False, null=False
    )
    location = models.CharField(
        verbose_name=_("Location"), max_length=255, blank=False, null=False
    )
    logo = models.FileField(upload_to="uploads/portfolio/companies_logo/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


class JobExperience(models.Model):
    position = models.CharField(verbose_name=_("Position"), null=False, blank=False)
    start = models.DateField(verbose_name=_("Start date"), null=False, blank=False)
    end = models.DateField(verbose_name=_("End date"), null=True, blank=True)
    company = models.ForeignKey(
        to=Company, null=False, blank=False, on_delete=models.PROTECT
    )

    @property
    def currently_employed(self) -> bool:
        return self.end is None

    def __str__(self):
        end = self.end if self.end else "today"
        return f"{self.company} from {self.start} to {end}"


class JobTask(models.Model):
    job = models.ForeignKey(
        to=JobExperience, null=False, blank=False, on_delete=models.CASCADE, related_name="job_tasks"
    )
    description = models.TextField(verbose_name=_("Description"), max_length=4192)

    def __str__(self):
        return self.job.__str__()

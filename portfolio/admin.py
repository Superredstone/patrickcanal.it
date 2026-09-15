from django.contrib import admin

from portfolio import models


@admin.register(models.JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    list_display = ["company", "position", "start", "end"]


@admin.register(models.JobTask)
class JobTaskAdmin(admin.ModelAdmin):
    list_display = ["job__company", "description", "job__start", "job__end"]


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "location"]


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]

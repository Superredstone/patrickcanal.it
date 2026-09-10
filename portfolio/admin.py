from django.contrib import admin

from portfolio import models


@admin.register(models.JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.JobTask)
class JobTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description"]

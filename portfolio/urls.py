from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="portfolio"),
    path("projects/", views.ProjectList.as_view(), name="projects"),
    path("contact/", views.ContactSend.as_view(), name="contact"),
    path("company/<int:pk>/logo/", views.CompanyLogo.as_view(), name="company-logo"),
]

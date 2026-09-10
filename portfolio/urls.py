from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="portfolio"),
    path("projects/", views.ProjectList.as_view(), name="projects"),
]

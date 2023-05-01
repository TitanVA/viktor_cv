from django.urls import path
from .views import HomePageView, SummaryPageView

urlpatterns = [
    path("about/", SummaryPageView.as_view(), name="summary"),
    path("", HomePageView.as_view(), name="home"),
]

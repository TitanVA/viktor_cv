from django.urls import path
from .views import HomePageView, SummaryListView, JobsListView, SummaryDetailView, JobsDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("summary/", SummaryListView.as_view(), name="summary_list"),
    path("summary/<uuid:pk>/", SummaryDetailView.as_view(), name="summary_detail"),
    path("jobs/", JobsListView.as_view(), name="jobs_list"),
    path("jobs/<uuid:pk>/", JobsDetailView.as_view(), name="job_detail"),
]

from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from posts.models import Summary, Jobs


class HomePageView(TemplateView):
    template_name = "home.html"


class SummaryListView(ListView):
    model = Summary
    context_object_name = "summary_list"
    template_name = "summary/summary_list.html"


class SummaryDetailView(DetailView):
    model = Summary
    context_object_name = "summary"
    template_name = "summary/summary_detail.html"


class JobsListView(ListView):
    model = Jobs
    context_object_name = "jobs_list"
    template_name = "jobs/jobs_list.html"


class JobsDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "jobs/job_detail.html"

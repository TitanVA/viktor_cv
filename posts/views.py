from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class SummaryPageView(TemplateView): # new
    template_name = "summary.html"

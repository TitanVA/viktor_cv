from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import SummaryPageView


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("summary")
        self.response = self.client.get(url)

    def test_summarypage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_summarypage_template(self):
        self.assertTemplateUsed(self.response, "summary.html")

    def test_summarypage_contains_correct_html(self):
        self.assertContains(self.response, "Summary:")

    def test_summarypage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, "Hi there! I should not be on the page.")

    def test_summarypage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            SummaryPageView.as_view().__name__
        )

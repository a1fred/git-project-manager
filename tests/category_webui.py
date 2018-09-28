from unittest import TestCase

from git_project.categories.webui import webapp


class CategoryWebUITests(TestCase):
    def test_url_index(self):
        with webapp.app.test_client() as c:
            index = c.get('/')
            self.assertEqual(index.status_code, 200)

    def test_url_about(self):
        with webapp.app.test_client() as c:
            index = c.get('/about')
            self.assertEqual(index.status_code, 200)

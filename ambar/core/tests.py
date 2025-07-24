from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

class IndexViewTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class DataFormTests(TestCase):
    def test_form_triggers_task(self):
        with patch('core.tasks.process_submission.send') as mocked:
            response = self.client.post(reverse('submit-data'), {'content': 'hi'})
            self.assertEqual(response.status_code, 302)
            mocked.assert_called_once_with('hi')

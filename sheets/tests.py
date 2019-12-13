import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Character
from django.test import TestCase


class CharacterModelTests(TestCase):

    def test_was_created_recently_with_future_char_sheet(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_sheet = Character(created=time)
        self.assertIs(future_sheet.was_created_recently(), False)

    def test_no_sheets(self):
        """
        If no sheets exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('sheets:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sheets are available.")
        self.assertQuerysetEqual(response.context['recent_char_list'], [])

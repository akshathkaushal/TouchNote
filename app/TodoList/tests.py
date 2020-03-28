from django.test import TestCase
from .models import List


class ListTestCase(TestCase):
    def test_list_objects(self):
        A = List()
        B = List()
        A.item = "A"
        B.item = "B"
        A.completed = True
        B.completed = False
        self.assertEqual(A.completed, True)
        self.assertEqual(B.completed, False)

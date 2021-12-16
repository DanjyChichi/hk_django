from django.test import TestCase

# Create your tests here. model과 view 테스트가 가능하다.

class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2, 3)

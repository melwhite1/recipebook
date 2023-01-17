from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
  def setUpTestData():
    User.objects.create(name='Bob')

  def test_user_name(self):
    recipe = User.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_name_max_length(self):
    recipe = User.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 120)
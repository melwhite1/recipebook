from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):
  def setUpTestData():
    Recipe.objects.create(name='Cake', cooking_time='35', ingredients='Flour, Milk, Yeast, Egg', difficulty='medium')

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 120)

  def test_ingredients_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 250)

  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')

  def test_form_validation_with_valid_data(self):
    form = RecipesSearchForm({'recipe_title': 'tea', 'chart_type': '#1'})
    self.assertTrue(form.is_valid())
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipesSearchForm
from .utils import get_recipename_from_id, get_chart

import pdb

import pandas as pd

# Create your views here.

def recipes_home(request):
   return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/detail.html'  

def records(request):
  form = RecipesSearchForm(request.POST or None)
  recipes_df=None
  chart = None
  if request.method =='POST':
    recipe_title = request.POST.get('recipe_title')
    chart_type = request.POST.get('chart_type')

    print (recipe_title, chart_type)

    # print ('Exploring querysets:')
    # print ('Case 1: Output of Recipe.objects.all()')
    qs=Recipe.objects.values_list('id', 'name')
    print (qs)

    qs=Recipe.objects.all()
    print (qs)
    for recipe_obj in qs:
      print(recipe_obj.id, recipe_obj.name)

    print ('Case 2: Output of Recipe.objects.filter(name=recipe_title)')
    qs =Recipe.objects.filter(name=recipe_title)
    print (qs)


    print ('Case 3: Output of qs.values')
    print (qs.values())

    print ('Case 4: Output of qs.values_list()')
    print (qs.values_list())

    # print ('Case 5: Output of Sale.objects.get(id=1)')
    # obj = Recipe.objects.get(id=1)
    # print (obj)

   # pdb.set_trace()
    if recipe_title=="name":
      qs = Recipe.objects.all()
    else: 
      qs = Recipe.objects.filter(name=recipe_title)
    if qs:
      recipes_df=pd.DataFrame(qs.values()) 
      print("recipes_df: ", recipes_df)
      recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)

      chart=get_chart(chart_type, recipes_df, labels=recipes_df['ingredients'].values)

      recipes_df=recipes_df.to_html()


  #pack up data to be sent to template in the context dictionary
  context={
    'form': form,
    'recipes_df': recipes_df,
    'chart': chart
    }

  #load the recipes/record.html page using the data that you just prepared
  return render(request, 'recipes/records.html', context)
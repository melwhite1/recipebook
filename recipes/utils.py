from recipes.models import Recipe

from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_recipename_from_id(val):
  recipename=Recipe.objects.get(id=val)
  return recipename

def get_graph():
  buffer = BytesIO()         
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  image_png=buffer.getvalue()
  graph=base64.b64encode(image_png)
  graph=graph.decode('utf-8')
  buffer.close()
  return graph

def get_chart(chart_type, data, **kwargs):
  plt.switch_backend('AGG')
  fig=plt.figure(figsize=(13,3))
  if chart_type == '#1':
      plt.bar(data['name'], data['ingredients'])
      plt.title('- Recipe Ingredients -')

  elif chart_type == '#2':
    plt.pie(data['cooking_time'], labels=data['name'])
    plt.title("- Cooking Time -")

  elif chart_type == '#3':
      plt.plot(data['name'], data['difficulty'])
      plt.title('- Recipe Difficulty -')
  else:
      print ('unknown chart type')

  #specify layout details
  plt.tight_layout()

  #render the graph to file
  chart =get_graph() 
  return chart 
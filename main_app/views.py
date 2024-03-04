from django.shortcuts import render



finches = [
  {'name': 'Peep', 'species': 'Zebra Finch', 'description': 'vibrant and energetic', 'age': 1},
  {'name': 'Sunny', 'species': 'American Goldfinch', 'description': 'bright yellow and cheerful', 'age': 2},
  {'name': 'Glimmer', 'species': 'Gouldian Finch', 'description': 'colorful and shy', 'age': 3},
  {'name': 'Chirpy', 'species': 'House Finch', 'description': 'social and vocal', 'age': 1},
]

# Create your views here.
def about (request):
    return render(request, 'about.html')


def finch_index (request):
    return render(request, 'pinches/index.html', {'finches': finches})
               
from django.shortcuts import render
from .models import Finch





# Create your views here.
def about (request):
    return render(request, 'about.html')


def finch_index (request):
    finches = Finch.objects.all() # retrieve all finches 
    return render(request, 'finches/index.html', {'finches': finches})
               
def finch_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {
        'finch':finch
    }
                  )
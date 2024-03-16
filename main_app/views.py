from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Feeding, Toy, Photo
from .forms import FeedingForm
import uuid # needed for generating random IDs
import boto3 # AWS Python SDK
import os # needed for accessing env vars




# Create your views here.
def home (request):
    return render(request, 'home.html')
def about (request):
    return render(request, 'about.html')


def finch_index (request):
    finches = Finch.objects.all() # retrieve all finches 
    return render(request, 'finches/index.html', {'finches': finches})
               
def finch_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all())
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch':finch,
        'feeding_form':feeding_form,
        'toys': toys_finch_doesnt_have

    }
                  )


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = "/finches"


def add_feeding (request, finch_id):
    ## create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  ## validate the form
  if form.is_valid():
    ## don't save the form to the db until it
   
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class ToyList(ListView):
    model = Toy
class ToyDetail(DetailView):
    model = Toy
class ToyCreate(CreateView):
    model=Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, finch_id, toy_id):
   Finch.objects.get(id=finch_id).toys.add(toy_id)
   return redirect('detail', finch_id=finch_id)

def assoc_toy_delete(request, finch_id, toy_id):
   finch=Finch.objects.get(id=finch_id)
   Toy.objects.get(id=toy_id).finch_set.remove(finch)
   return redirect('detail', finch_id=finch_id)


def add_photo (request, finch_id):
   photo_file = request.FILES.get('photo-file', None)
   if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # calls out to external services (e.g. S3) should be wrapped in try catches, because we don't know what might happen over the network!
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, finch_id=finch_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
   return redirect('detail', finch_id=finch_id)
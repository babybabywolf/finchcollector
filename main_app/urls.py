from django.urls import path
from . import views

urlpatterns = [
 path('about/', views.about, name='about'), # `name='home'` kwarg gives the route a name - naming is optional, but good practice (it will come in handy later)
 path('finches/', views.finch_index, name='index'),
 path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
]

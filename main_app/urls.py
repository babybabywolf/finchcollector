from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'), # `name='home'` kwarg gives the route a name - naming is optional, but good practice (it will come in handy later)
 path('finches/', views.finch_index, name='index'),
 path('finches/<int:finch_id>/', views.finch_detail, name='detail'),
 path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name="add_feeding"),
 path('finches/create/', views.FinchCreate.as_view(), name="finch_create"),
 path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
 path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finch_delete"),
 path('toys/', views.ToyList.as_view(), name='toys_index'),
 path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
 path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
 path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
 path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
 path('finches/<int:finch_id>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),
 path('finches/<int:finch_id>/assoc_toy/delete/<int:toy_id>', views.assoc_toy_delete, name="assoc_toy_delete"),
 path('finches/<int:finch_id>/add_photo/', views.add_photo, name="add_photo"),
]

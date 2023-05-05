
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('details/', views.DetailsTable.as_view(),name="details"),
    path('update/<int:pk>',views.DetailsUpdate.as_view()),

    
    path('',views.home),
    path('addemp',views.addemp),
    path('del',views.delt),
    path('update',views.update),
]

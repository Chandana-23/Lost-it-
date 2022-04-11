
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='/'),
    path('add',views.add,name='add'),
    path('claim/<int:pk>/',views.claim,name='claim')
]

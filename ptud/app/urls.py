from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cv/', cv, name='cv'),\
    path('todo/', todo, name='todo'),
    path('add-todo/', add_todo, name='add_todo'),
    path('delete-todo/<int:id>/', delete_todo, name='delete_todo'),
    
    path('update-cv', update_cv, name='update_cv')
]
from django.urls import include,path
from .views import ListTodo,DetailTodo
urlpatterns = [
    path('<int:pk>/',DetailTodo.as_view(),name='todos_detail'),
    path('',ListTodo.as_view(),name='todo_list')
]

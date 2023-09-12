from django.urls import path
from .views import AllTodoView,DetailTodoView,CreateTodoModel,UpdateTodoModel,DeleteTodoModel

urlpatterns = [
    path('all/',AllTodoView.as_view()),
    path('detail/<int:todo_id>/',DetailTodoView.as_view()),
    path('create/',CreateTodoModel.as_view()),
    path('update/<int:todo_id>/',UpdateTodoModel.as_view()),
    path('delete/<int:todo_id>/',DeleteTodoModel.as_view())
]
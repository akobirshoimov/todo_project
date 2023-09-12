from django.shortcuts import render,get_object_or_404
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AllTodoView(APIView):
    def get(self,request):
        all = TodoModel.objects.all()
        serializer = TodoSerializer(all,many=True)
        return Response(serializer.data)
    
class DetailTodoView(APIView):
    def get(self,request,*args,**kwargs):
        todo = get_object_or_404(TodoModel,id=kwargs['todo_id'])
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
class CreateTodoModel(APIView):
    def post(self,request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UpdateTodoModel(APIView):
    def patch(self,request,*args,**kwargs):
        todo = get_object_or_404(TodoModel,id=kwargs['todo_id'])
        serializer = TodoSerializer(todo,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class DeleteTodoModel(APIView):
    def delete(self,request,*args,**kwargs):
        todo = get_object_or_404(TodoModel,id=kwargs['todo_id'])
        todo.delete()
        return Response('data deleted')
    
    
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    
    if request.method == 'GET':
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
        pass
    
    elif request.method == 'POST':
        serializer=PostSerializer(data=request.data)
        if(serializer.is_valid()):
           serializer.save()
           return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400) 
@api_view(['GET', 'PUT','DELETE'])
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='GET':
        serializer=PostSerializer(post)
        return Response(serializer.data)
        pass
    elif request.method=='PUT':
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    elif request.method=='DELETE':
        post.delete()
        return Response(status=204)
@api_view(['POST'])
def Login(request):
   username=request.data.get('username')
   password=request.data.get('password')
   user=authenticate(username=username,password=password)
   if user:
       token,created=Token.objects.get_or_create(user=user)
       return Response({
           'token': token.key,
           'messege': 'login succesfully'
       }
       )
   else:
       return Response({
           'error':'Invalid username or password'
       },status=400)
#"token": "71ec82eee6f1edbf16ab0d4d6ce8edcdf063d1fd"
       
    
    
        

from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def PostsView(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        print(posts)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def postsdetail(request, pk):
    try:
        post = Post.objects.get(pk = pk)
    except post.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)

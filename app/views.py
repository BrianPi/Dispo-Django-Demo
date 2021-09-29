import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import User, Post, PostLike
from app.serializers import PostSerializer
from django.core import serializers
from django.db import IntegrityError
from django.db.models import Count

def get_user(request):
    return User.objects.get(id=request.data["user"])

@api_view(["POST"])
def create_user(request):
    try:
        User.objects.create_user(request.data["username"],password=request.data["password"])
    except KeyError:
        return Response(status=400)
    except IntegrityError:
        return Response(status=409)
    return Response(status=201)

@api_view(["GET"])
def list_top_users(request):
    return Response(User.objects.annotate(posts=Count('post')).order_by("-posts").filter(posts__gt=0).values("username","posts"))

@api_view(["POST"])
def follow_user(request):
    try:
        user=get_user(request)
    except KeyError:
        return Response(status=400)
    try:
        user.follow.add(User.objects.get(id=data["follow"]))
    except IntegrityError:
        return Response(status=409)
    return Response(status=201)
    
@api_view(["POST"])
def create_post(request):
    try:
        Post.objects.create(user=get_user(request),body=request.data["body"])
    except KeyError:
        return Response(status=400)
    return Response(status=201)
    
@api_view(["GET","PUT"])
def individual_post(request, post_id):
    if request.method=="GET":
        try:
            post=Post.objects.annotate(likes=Count('like')).get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=404)
        return Response(PostSerializer(post).data)
    elif request.method=="PUT":
        try:
            PostLike.objects.create(user=get_user(request),post=post_id)
        except IntegrityError:
            PostLike.objects.get(user=get_user(request),post=post_id).delete()
        except KeyError:
            return Response(status=400)
        return Response(status=200)
    
@api_view(["GET"])
def view_posts(request, user_id):
    poi_user = User.objects.get(id=user_id)
    relevant_users = poi_user.follow.all() | User.objects.filter(id=user_id)
    return Response(PostSerializer(Post.objects.filter(user__in=relevant_users).order_by('-timestamp'), many=True).data)
    

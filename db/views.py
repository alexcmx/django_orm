from django.shortcuts import render
from db import query
from django.http.response import *
# Create your views here.
from db.models import User, Blog, Topic
from db.query import *

def create1(request):
    # query.create()
    # User.objects.all().delete()
    # Blog.objects.all().delete()
    # Topic.objects.all().delete()
    for i in User.objects.all():
        print(i.first_name)
    for i in Blog.objects.all():
        print(i.title, i.subscribers)
    for i in Topic.objects.all():
        print(i.title, i.blog.title, i.author, i.created, i.likes)
    return HttpResponse(str(User.objects.all())+'\n'+str(Blog.objects.all())+'\n'+str(Topic.objects.all()))
def unsubscr(request):
    unsubscribe_u2_from_blogs()
    for i in Blog.objects.all():
        print(i.title)
        for j in i.subscribers.all():
            print(j.first_name)
    return HttpResponse("")

def get_topic_created_grated1(request):
    for i in get_topic_created_grated():
        print(i.title)
    return HttpResponse("")

def get_topic_title_ended1(request):
    for i in get_topic_title_ended():
        print(i.title)
    return HttpResponse("")
def get_topic_count1(request):
    blogs = get_topic_count()
    for i in blogs:
        print(i.topic_count)
    return HttpResponse("")
def get_avg_topic_count1(request):
    print(get_avg_topic_count())
    return HttpResponse("")

def get_blog_that_have_more_than_one_topic1(requset):
    for i in get_blog_that_have_more_than_one_topic():
        print(i.title)
    return HttpResponse("")

def get_topic_by_u11(request):
    for i in get_topic_by_u1():
        print(i.title)
    return HttpResponse("")

def get_user_that_dont_have_blog1(request):
    for i in get_user_that_dont_have_blog():
        print(i.first_name)
    return HttpResponse("")

def get_topic_that_like_all_users1(request):
    for i in get_topic_that_like_all_users():
        print(i.title)
    return HttpResponse("")

def get_topic_that_dont_have_like1(request):
    for i in get_topic_that_dont_have_like():
        print(i.title)
    return HttpResponse("")

from datetime import datetime

from django.db.models import Q, Count, Avg, F
from pytz import UTC
from datetime import *
from db.models import User, Blog, Topic


def create():
    u1 = User.objects.create(first_name="u1", last_name='u1')
    u2 = User.objects.create(first_name="u2", last_name='u2')
    u3 = User.objects.create(first_name="u3", last_name='u3')
    u1.save()
    u2.save()
    u3.save()
    b1 = Blog.objects.create(title='blog1', author=u1)
    b2 = Blog.objects.create(title='blog2', author=u1)
    b1.save()
    b2.save()
    b1.subscribers.add(u1)
    b1.subscribers.add(u2)
    b2.subscribers.add(u2)
    b1.save()
    b2.save()
    t1 = Topic(title="topic1", blog=b1, author=u1)
    t2 = Topic(title='topic2_content', blog=b1, author=u3, created='2017-01-01')

    t1.save()
    t2.save()
    t1.likes.add(u1, u2, u3)
    t1.save()

def edit_all():
    User.objects.all().update(first_name='uu1')


def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    for i in Blog.objects.all():
        i.subscribers.remove(User.objects.get(first_name='u2'))



def get_topic_created_grated():
    return Topic.objects.filter(created__gte=date(2018, 1, 1))


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith="content")


def get_user_with_limit():
    return User.objects.order_by('id')[-2:]


def get_topic_count():
    blogs = Blog.objects.annotate(topic_count=Count('topic')).order_by('-topic_count')
    return blogs

def get_avg_topic_count():
    sum = 0
    for i in Blog.objects.annotate(topic_count=Count('topic')):
        sum += i.topic_count
    return sum/Blog.objects.count()



def get_blog_that_have_more_than_one_topic():
    return Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=1)


def get_topic_by_u1():
    return Topic.objects.filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    return User.objects.annotate(blog_count=Count('blog')).filter(blog_count=0).order_by('id')


def get_topic_that_like_all_users():
    return Topic.objects.annotate(like_count=Count('likes')).filter(like_count=User.objects.all().count())


def get_topic_that_dont_have_like():
    return Topic.objects.annotate(like_count=Count('likes')).filter(like_count=0)

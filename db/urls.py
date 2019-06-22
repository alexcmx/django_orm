from django.conf.urls import url

from db.views import *

urlpatterns = [
    url(r'^create/$', create1),
    url(r'^subscr/$', unsubscr),
    url(r'^get_topic_created_grated1/$', get_topic_created_grated1),
    url(r'^get_topic_title_ended/$', get_topic_title_ended1),
    url(r'^get_topic_count/$', get_topic_count1),
    url(r'^get_avg_topic_count/$',get_avg_topic_count1),
    url(r'^get_blog_that_have_more_than_one_topic/$', get_blog_that_have_more_than_one_topic1),
    url(r'^get_topic_by_u1/$', get_topic_by_u11),
    url(r'^get_user_that_dont_have_blog/$', get_user_that_dont_have_blog1),
    url(r"^get_topic_that_like_all_users/$", get_topic_that_like_all_users1),
    url(r'^get_topic_that_dont_have_like/$',get_topic_that_dont_have_like1),

]

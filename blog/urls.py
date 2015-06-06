from django.conf.urls import patterns, url
from blog import views
from blog.views import UserRegView
urlpatterns = patterns('',

    url(r'^$', views.HomeView.as_view(), name='HomeView'),
    url(r'^user_reg/$', views.UserRegView.as_view(), name=UserRegView),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^blog_post/$', views.blog_post, name='blog_post'),
    url(r'^post_list/$', views.PostListView.as_view(), name='PostListView'),
    url(r'^post_view/(?P<id>\d+)/$', views.post_view, name='post_view'),
    url(r'^post_edit/(?P<id>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^passwordchange/$', views.passwordchange, name='passwordchange'),
)
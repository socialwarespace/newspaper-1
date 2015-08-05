from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newspaper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',                 include(admin.site.urls)),
    url(r'^$',                      'news.views.index', name='index'),
    url(r'^login/$',                'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^signup/$',               'news.views.signup', name='signup'),
    url(r'^signup/submit/$',        'news.views.signup_submit', name='signup_submit'),
    url(r'^logout/$',               'news.views.user_logout', name='user_logout'),
    url(r'^newest/$',               'news.views.newest_list', name='newest_list'),
    url(r'^thread/new/$',        'news.views.new_thread', name='new_thread'),
    url(r'^thread/submit/$',        'news.views.submit_thread', name='submit_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', 'news.views.read_thread', name='read_thread'),
    # upvote
    # devote
    # edit profile
    # submit comment
    # about
)

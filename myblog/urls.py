from django.conf.urls import include, url

urlpatterns = [
    url(r'^index/$', 'myblog.views.blog_list', name="blog_list"),
    url(r'^$', 'myblog.views.blog_list', name="blog_lsit"),
    url(r'^blog/(?P<pk>[0-9]+)$', 'myblog.views.blog_detail', name="blog_detail"),
]
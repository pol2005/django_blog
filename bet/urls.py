"""betvision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from views import PrognostikaListView
from django.contrib.sitemaps.views import sitemap
from bet.sitemaps import ArticleSitemap
from .api import v1_api
from feeds import LatestEntriesFeed

sitemaps = {
   'posts': ArticleSitemap,
}

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$', views.post_detail,name='post_detail'),
    url(r'^ajax_newsletter/$', views.ajax_newsletter, name='ajax_newsletter'),
    url(r'^kouponi', views.kouponi, name='kouponi'),
    url(r'^livescore', views.livescore, name='livescore'),
    url(r'^apodoseis', views.apodoseis, name='apodoseis'),
    url(r'^livestreaming', views.livestreaming, name='livestreaming'),
    url(r'^asianhandicap', views.asianhandicap, name='asianhandicap'),
    url(r'^tziroi', views.tziroi, name='tziroi'),
    url(r'^statistika', views.statistika, name='statistika'),
    url(r'^bonus', views.bonus, name='bonus'),
    url(r'^contact$', views.contact,name='contact'),
    url(r'^tables', views.tables, name='tables'),
    url(r'^newsletter/', views.newsletter,name='newsletter'),
    url(r'^category/analiseis/$', views.analiseis,name='analiseis'),
    url(r'^login/$',auth_views.login,name='login'),
    url(r'^logout/$',auth_views.logout,name='logout'),
    url(r'^logout-then-login/$',auth_views.logout_then_login,name='logout_then_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^prognostika-list/$', PrognostikaListView.as_view(), name='prognostika-list'),


    # login / logout urls

    #url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$',auth_views.password_change,{'post_change_redirect' : '/registration/password-change/done',},name='password_change'),
    url(r'^password-change/done/$',auth_views.password_change_done,name='password_change_done'),
    # restore password urls
    url(r'^password-reset/$',auth_views.password_reset,{'template_name':'registration/passsword_reset_form.html','post_reset_redirect' : '/registration/password-rest/done'},name='password_reset'),
    url(r'^password-reset/done/$',auth_views.password_reset_done,name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,{'post_reset_redirect' : '/registration/password-reset/complete'},name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auth_views.password_reset_complete,name='password_reset_complete'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'list/$',views.post_list, name = 'post_list'),
    url(r'^api/', include(v1_api.urls)),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    url(r'^category/(?P<tag_slug>[-\w]+)/$', views.post_list,name='post_list_by_tag'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^rss/$', LatestEntriesFeed()),
    #url(r'^(?P<post>[\w-]+)/$', views.post_detail,name='post_detail'),
    #url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

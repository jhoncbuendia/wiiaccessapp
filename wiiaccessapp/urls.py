from django.conf.urls import patterns, include, url
from rest_framework.authtoken import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiiaccessapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'usercontrol.views.index'),
    url(r'^login$', 'usercontrol.views.loginView'),
    url(r'^logout', 'usercontrol.views.logout_view'),
    url(r'^usertools', 'usertools.views.index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^directory/', include('directory.urls')),
    url(r'^api-token-auth', views.obtain_auth_token),
    url(r'^createtokens/', 'directory.views.createTokens'),
    url(r'^directory/docs/', include('rest_framework_swagger.urls')),

)

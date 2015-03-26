from django.conf.urls import patterns, include, url
from django.contrib import admin

# TastyPie
from tastypie.api import Api
from api.api import MeditationResource, SessionResource, UserResource, appUserResource

v1_api = Api(api_name='v1')
v1_api.register(MeditationResource())
v1_api.register(SessionResource())
v1_api.register(UserResource())
v1_api.register(appUserResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^backend/', include('api.urls')),
    url(r'^api/', include(v1_api.urls)),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
)

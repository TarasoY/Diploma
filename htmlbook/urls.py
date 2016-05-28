from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import htmltags.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'htmlbook.views.home', name='home'),
    # url(r'^htmlbook/', include('htmlbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^settings$', htmltags.views.ListTagsView.as_view(),
        name='tags-list'),
    url(r'^settings/new$', htmltags.views.CreateTagView.as_view(),
        name='tags-new'),
    url(r'^settings/edit/(?P<pk>\d+)/$', htmltags.views.UpdateTagsView.as_view(),
        name='tag-edit', ),
    url(r'^settings/delete/(?P<pk>\d+)/$', htmltags.views.DeleteTagView.as_view(),
        name='tag-delete', ),
    url(r'^$', htmltags.views.MainTagsView.as_view(),
        name='tags'),
    url(r'^details/(?P<pk>\d+)/$', htmltags.views.MainDetailsTagsView.as_view(),
        name='tags-details'),

)



urlpatterns += staticfiles_urlpatterns()
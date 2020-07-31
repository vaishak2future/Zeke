from django.conf.urls import url, include
#from django.contrib import admin
from zeke.views import root,about,contact,login,logout,plot

# http://stackoverflow.com/questions/3718077/
#\django-you-dont-have-permission-to-edit-anything
#admin.autodiscover()


urlpatterns = [
                       url(r'^$', root),#'zeke.views.root'),
                       url(r'^about/', about),#'zeke.views.about'),
                       url(r'^contact/', contact),#'zeke.views.contact'),
                       url(r'^login/', login),#'zeke.views._login'),
                       url(r'^logout/', logout),#'zeke.views._logout'),
#                       url(r'^admin/', admin.site.urls),
                       url(r'^plot$', plot)#'zeke.views.plot')
              ]

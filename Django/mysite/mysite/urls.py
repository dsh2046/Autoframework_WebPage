from django.conf.urls import url
from django.contrib import admin
from home import views as home_views

urlpatterns = [
    url(r'^index/', home_views.index, name='index'),
    url(r'^detail/', home_views.detail, name='detail'),
    url(r'^$', home_views.login, name='login'),
    url(r'^login/', home_views.login, name='login'),
    url(r'^logout/', home_views.logout, name='logout'),
    url(r'^login_validate/', home_views.login_validate, name='login_validate'),
    #url(r'^home/(\d+)/(\d+)', home_views.add, name='add'),
    url(r'^admin/', admin.site.urls),

]

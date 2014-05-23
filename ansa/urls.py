from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ansa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','usuarios.views.login_page',name='login'),
    url(r'^home/$','usuarios.views.home',name='home'),
    url(r'^logout/$','usuarios.views.cerrar_sesion',name='logout'),
    url(r'^usuarios/newuser/$','usuarios.views.newuser',name='newuser'),
    url(r'^usuarios/listuser/$', 'usuarios.views.listar_usuarios', name='listuser'),
    url(r'^usuarios/edituser/', 'usuarios.views.edit_user', name="edituser"),

    )

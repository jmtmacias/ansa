from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from usuarios.forms import UserCreateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

""" """
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/login/')

@login_required(login_url="/login/")
def newuser(request):
	if request.method == 'POST':
		formulario = UserCreateForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('usuarios/new_user.html')
	else:
		formulario = UserCreateForm();
		return render_to_response('usuarios/new_user.html',{'formulario':formulario},context_instance = RequestContext(request))

def login_page(request):
	if not request.user.is_anonymous():
		return render_to_response('home.html',context_instance=RequestContext(request))
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			if username=='' and password=='':
				return render_to_response('usuarios/login.html',{'message':'Alguno de los campos esta vacio!'},
																context_instance=RequestContext(request))
			acceso = authenticate(username = username, password = password)
			if acceso.is_active:
				login(request, acceso)
				return render_to_response('home.html',context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/login/')
	else:
		formulario = AuthenticationForm()
	return render_to_response('usuarios/login.html',{'formulario':formulario},context_instance = RequestContext(request))


@login_required(login_url="/login/")
def listar_usuarios( request ):
	usuarios = User.objects.all().order_by('last_name')
	return render_to_response('usuarios/list_user.html',{'usuarios':usuarios}, context_instance = RequestContext(request))

@login_required(login_url = '/login/')
def home(request):
	message = 'Mensaje 1'
	return render_to_response('home.html',context_instance=RequestContext(request))

@login_required
def edit_user(request):
   # This body will only run if the user is logged in
   # and the current logged in user will be in request.user

   formulario = UserChangeForm(instance=request.user,)
   return render_to_response('usuarios/user_edit.html',{'formulario':formulario},context_instance=RequestContext(request))
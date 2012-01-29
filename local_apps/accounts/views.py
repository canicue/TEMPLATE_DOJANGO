# Create your views here.
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from local_apps.accounts.forms import ProfileForm
from local_apps.accounts.forms import UserForm
from local_apps.accounts.models import Profile
from django.core.urlresolvers import reverse
from django.contrib import auth
def login(request):
 
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('aca_home'))
        
    if request.POST:
        formulario = AuthenticationForm(data=request.POST)

        if formulario.is_valid():
            auth.login(request, formulario.get_user())

            return HttpResponseRedirect(reverse('aca_home'))
    else:
        
        formulario = AuthenticationForm()

    return render_to_response('accounts/login.html', {'form':formulario},context_instance=RequestContext(request))

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return HttpResponseRedirect(reverse('aca_home'))

def mi_perfil(request):
    perfil = None
    try:
        perfil = Profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        #return HttpResponseRedirect('crear_perfil')
        return crear_perfil(request)
    formulario = ProfileForm(instance=perfil)
    perfil.save()
    return render_to_response('accounts/mi_perfil.html', {'form':formulario}, context_instance=RequestContext(request))


def crear_perfil(request):
    if request.method == 'POST':
        formulario = ProfileForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = ProfileForm()
    return render_to_response('accounts/crear_perfil.html', {'form':formulario}, context_instance=RequestContext(request))








@login_required
def ver_perfil(request, id_usuario=None):
    if id_usuario:
        pass
    else:
        try:
            perfil = Profile.objects.get(user=request.user)
            formulario = ProfileForm(instance=perfil)
            perfil.save()
        except ObjectDoesNotExist:
            formulario = ProfileForm()
    return render_to_response('accounts/profile.html', {'form':formulario}, context_instance=RequestContext(request))


@login_required
#@permission_required('auth.can_add_user')
def crear_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(data=request.POST)
        if formulario.is_valid():
            #User.objects.create_user({'username':'usuario','email':'email','password':'password'})
            formulario.save()
            return HttpResponseRedirect('/veremos/')
    else:
        formulario = UserCreationForm()
    return render_to_response('accounts/crear_usuario.html', {'form':formulario}, context_instance=RequestContext(request))

@login_required
def cambiar_password(request):
    """cambia el pass"""
    if request.method == 'POST':
        formulario = PasswordChangeForm(request.user, request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect('/indio.html')
    else:
        formulario = PasswordChangeForm(request.user)
    return render_to_response('accounts/cambiar_password.html', {'form':formulario, 'usuario':request.user, 'post':request.POST}, context_instance=RequestContext(request))
@login_required
def editar_perfil(request):

    if request.method == 'POST':

        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and perfil_form.is_valid():

            user_form.save()
            perfil_form.save()
            return HttpResponseRedirect('/veremos/')

    else:

        user_form = UserForm(instance=request.user)
        perfil_form = ProfileForm(instance=request.user.profile)

    return render_to_response('accounts/editar_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form}, context_instance=RequestContext(request))





#genericas
def add_user(*args, ** kwargs):
    from django.views.generic.create_update import create_object
    return create_object(*args, ** kwargs)


@login_required
def index(request):
    #assert False
    return render_to_response('accounts/index.html', {}, context_instance=RequestContext(request))

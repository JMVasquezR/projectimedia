import random
import string

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from faker import Factory

from app_correos.forms import *
from app_correos.models.registro import RegistroModel
from app_correos.task import task_enviar_mail


class ContactView(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = '/app_correos/listado_usuarios/'

    def post(self, request, *args, **kwargs):
        form = RegistroForm(data=request.POST)
        if form.is_valid():
            self.create_user(form.cleaned_data)

        return super().post(request, *args, **kwargs)

    @transaction.atomic()
    def create_user(self, valid_data):
        registro = RegistroModel(cantidad_de_usuario=valid_data['cantidad_de_usuario'],
                                 correo_emisor=valid_data['correo_emisor'],
                                 asunto=valid_data['asunto'],
                                 mensaje=valid_data['mensaje'])
        registro.save()

        cantidad = valid_data['cantidad_de_usuario']
        fake = Factory.create()
        for index in range(0, cantidad):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(9)])
            email = 'user_%s@imedia.pe' % (username,)
            extra_data_from_here = {
                'first_name': first_name,
                'last_name': last_name,
            }
            get_user_model().objects.create_user(
                username=username,
                email=email,
                password=None,
                **({**extra_data_from_here})
            )

            task_enviar_mail(valid_data['asunto'], valid_data['mensaje'], valid_data['correo_emisor'], [email])


class UsuariosViewSet(View):

    def __init__(self):
        self.contexto = {}

    def get_contexto(self, **kwargs):
        '''
        Retornar el contexto para retornar la vista
        :return: dict
        '''
        self.contexto['ls_usuarios'] = User.objects.all()
        return self.contexto

    def get(self, request):
        return render(request, 'listado.html', self.get_contexto())


class EliminarViewSet(View):

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return redirect(reverse('app-correos:listado'))


class PerfilView(FormView):
    template_name = 'perfil.html'
    form_class = PerfilForm
    success_url = '/app_correos/listado_usuarios/'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(PerfilView, self).get_context_data(**kwargs)
        context['ls_usuario'] = User.objects.get(id=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = PerfilForm(data=request.POST)
        if form.is_valid():
            self.edit_user(form.data)
        return self.form_valid(form)

    def edit_user(self, valid_data):
        usuario = User.objects.get(id=self.kwargs['pk'])
        usuario.first_name = valid_data['first_name']
        usuario.last_name = valid_data['last_name']
        usuario.email = valid_data['email']
        usuario.save()

from django.contrib import admin
from django import forms

from app_correos.models.registro import RegistroModel


class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroModel
        fields = '__all__'


class RegistroAdmin(admin.ModelAdmin):
    form = RegistroForm
    list_display = ['cantidad_de_usuario', 'correo_emisor', 'asunto']


admin.site.register(RegistroModel, RegistroAdmin)

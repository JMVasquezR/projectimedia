from django import forms


class RegistroForm(forms.Form):
    cantidad_de_usuario = forms.IntegerField(widget=forms.TextInput(
        attrs={"type": "number", "name": "cantidad_de_usuario", "id": "cantidad_de_usuario", "class": "form-control"}),
        required=True)
    correo_emisor = forms.CharField(widget=forms.TextInput(
        attrs={"type": "email", "name": "correo_emisor", "id": "correo_emisor", "class": "form-control"}),
        required=True)
    asunto = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text", "name": "asunto", "id": "asunto", "class": "form-control"}), required=True)
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={"name": "mensaje", "id": "mensaje", "class": "form-control"}), required=True)


class PerfilForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text", "name": "first_name", "id": "first_name", "class": "form-control", "value": ""}),
        required=True)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"type": "text", "name": "last_name", "id": "last_name", "class": "form-control", "value": ""}),
        required=True)

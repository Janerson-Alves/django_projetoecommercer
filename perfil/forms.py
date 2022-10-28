from django import forms
from django.contrib.auth.models import User
from . import models


# Perfil
class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'  # quais campos vou querer
        exclude = ('usuario',)  # excluir algum campo


# usando o forms
class UserForm(forms.ModelForm):
    # senha
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    # verificação de senha

    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )
    # verificar qual usuario esta enviando os dados e se esse usuario ja existe

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password', 'password2', 'email')

        # validando as coisas
        def clean(self, *args, **kwargs):
            data = self.data
            cleaned = self.cleaned_data
            validation_error_msgs = []

            usuario_data = cleaned.get('username')
            password_data = cleaned.get('password')
            password2_data = cleaned.get('password2')
            email_data = cleaned.get('email')

            usuario_db = User.objects.filter(username=usuario_data).first()
            email_db = User.objects.filter(email=email_data).first()
            password_db = User.objects.filter(password=password_data).first()
            password2_db = User.objects.filter(password=password2_data).first()

            error_msg_user_exists = 'Usuário ja existe'
            error_msg_email_exists = 'E-mail ja existe'
            error_msg_password_match = 'As duas senhas não conferem'
            error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracteres'
            error_msg_required_field = 'Este campo e obrigatorio'

            # Usuários logados: atualização
            if self.usuario:
                if usuario_db:
                    if usuario_data != usuario_db.username:
                        validation_error_msgs['username'] = error_msg_user_exists

                if email_db:
                    if email_data != email_db.email:
                        validation_error_msgs['email'] = error_msg_email_exists

                if password_data:
                    if password_data != password2_data:
                        validation_error_msgs['password'] = error_msg_password_match
                        validation_error_msgs['password2'] = error_msg_password_match

                    if len(password_data) < 6:
                        validation_error_msgs['password'] = error_msg_password_short

            # Usuário não logados: cadastro
            else:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

                if not password_data:
                    validation_error_msgs['password'] = error_msg_required_field

                if not password2_data:
                    validation_error_msgs['password2'] = error_msg_required_field

                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

            if validation_error_msgs:
                raise (forms.ValidationError(validation_error_msgs))

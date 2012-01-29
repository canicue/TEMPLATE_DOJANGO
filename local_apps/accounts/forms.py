from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from models import Profile

from django.forms.widgets import Textarea
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['company','notes']
        widgets={'notes':Textarea(attrs={'cols':12,'rows':11})}
class CrearUsuarioForm(UserCreationForm):
    base_field={}#ver para agregar mail


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


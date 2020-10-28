from django.forms import ModelForm
from .models import Boards

class createBoard(ModelForm):
    class Meta:
        model = Boards
        fields = '__all__'
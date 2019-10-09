from django import forms
from .models import House, HouseImage

class HouseUploadForm(forms.ModelForm):

    class Meta:
        model = House
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super(HouseUploadForm, self).__init__(*args, **kwargs)
        self.fields['images']=forms.ImageField()
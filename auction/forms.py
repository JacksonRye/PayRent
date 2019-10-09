
from django import forms
from django.utils import timezone
from flatpickr import DateTimePickerInput

from .models import AuctionSession


class AuctionSessionForm(forms.ModelForm):

    class Meta:
        model = AuctionSession
        # fields = ['title', 'description']
        fields = ('house', 'start', 'end',)

        # Use only when testing
        # fields = ('start', 'end',)

        widgets = {
            'start': DateTimePickerInput(),
            'end': DateTimePickerInput(),
        }

    def clean(self):
        cleaned_data = super(AuctionSessionForm, self).clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')

        if start and end:

            if end < start:
                raise forms.ValidationError(
                    "End cannot be before Start", code='invalid')

            if start < timezone.now():
                raise forms.ValidationError(
                    "Auction cannot start before 'right now'", code='invalid')

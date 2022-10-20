from django.forms import ModelForm
from .models import PlannedEvent


class EventForm(ModelForm):
    class Meta:
        model = PlannedEvent
        fields = ['date', 'type_of_event', 'description']

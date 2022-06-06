from django.forms import ModelForm
from django import forms
from .models import EventForm
import datetime


class EventBooking(ModelForm):
    required_css_class = 'required-field'
    user_email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
        )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
        )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
        )
    phone_no = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            ))
    event_date = forms.DateField(
        initial=datetime.date.today,
        help_text="Date format yyyy-mm-dd",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'datetimepicker'
        }),
        input_formats=['%d/%m/%Y %H:%M']
        )
    event_details = forms.CharField(widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                }
            ))

    class Meta:
        model = EventForm
        fields = "__all__"

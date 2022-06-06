from django.forms import ModelForm
from django import forms
from .models import EventForm


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
            ),
        min_value=10,
        )
    event_date = forms.DateField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'id': 'datetimepicker'
        }))
    event_details = forms.CharField(widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                }
            ))

    class Meta:
        model = EventForm
        fields = "__all__"

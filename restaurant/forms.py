from django.forms import ModelForm
from django import forms
from .models import EventForm, Booking


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
    phone_no = forms.CharField(
        min_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
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


class ReservationForm(ModelForm):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
        )
    booking_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            )
        )
    date = forms.DateField(
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
        model = Booking
        fields = fields = [
            'user',
            'booking_name',
            'date',
            'event_details',
            'allergies',
            ]

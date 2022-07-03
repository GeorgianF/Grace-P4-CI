from django.test import TestCase
from .forms import EventBooking, ReservationForm

# Create your tests here.


class TestEventBookingForm(TestCase):

    def test_email_is_required(self):
        form = EventBooking({'user_email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('user_email', form.errors.keys())
        self.assertEqual(
            form.errors['user_email'][0], 'This field is required.'
            )

    def test_first_name_is_required(self):
        form = EventBooking({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.'
            )

    def test_last_name_is_required(self):
        form = EventBooking({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(
            form.errors['last_name'][0], 'This field is required.'
            )

    def test_phone_no_is_required(self):
        form = EventBooking({'phone_no': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_no', form.errors.keys())
        self.assertEqual(
            form.errors['phone_no'][0], 'This field is required.'
            )

    def test_event_date_is_required(self):
        form = EventBooking({'event_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('event_date', form.errors.keys())
        self.assertEqual(
            form.errors['event_date'][0], 'This field is required.'
            )

    def test_event_details_is_required(self):
        form = EventBooking({'event_details': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('event_details', form.errors.keys())
        self.assertEqual(
            form.errors['event_details'][0], 'This field is required.'
            )

    def test_fields_are_explicit_in_form_metaclass(self):
        form = EventBooking()
        self.assertEqual(form.Meta.fields, '__all__')


class TestReservationForm(TestCase):
    def test_booking_name_is_required(self):
        form = ReservationForm({'booking_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('booking_name', form.errors.keys())
        self.assertEqual(
            form.errors['booking_name'][0], 'This field is required.'
            )

    def test_date_is_required(self):
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(
            form.errors['date'][0], 'This field is required.'
            )

    def test_arrival_time_is_required(self):
        form = ReservationForm({'arrival_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('arrival_time', form.errors.keys())
        self.assertEqual(
            form.errors['arrival_time'][0], 'This field is required.'
            )

    def test_booking_details_is_required(self):
        form = ReservationForm({'booking_details': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('booking_details', form.errors.keys())
        self.assertEqual(
            form.errors['booking_details'][0], 'This field is required.'
            )

    def test_number_of_persons_is_required(self):
        form = ReservationForm({'number_of_persons': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_persons', form.errors.keys())
        self.assertEqual(
            form.errors['number_of_persons'][0], 'This field is required.'
            )

    def test_number_of_persons_is_bigger_than_six(self):
        form = ReservationForm({'number_of_persons': '7'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors[
            'number_of_persons'][0],
            'Ensure this value is less than or equal to 6.')

    def test_reservation_fields_are_explicit_in_form_metaclass(self):
        form = ReservationForm()
        self.assertEqual(form.Meta.fields, [
            'booking_name',
            'date',
            'arrival_time',
            'booking_details',
            'number_of_persons',
            'allergies',
            ])

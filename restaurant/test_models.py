from django.test import TestCase, Client
from .models import Course, EventForm, Booking

# Create your tests here.


class TestModels(TestCase):

    def test_the_course_model(
        self,
        name='Course',
        slug='Course',
        description='Course',
        price='10',
        allergens='NO ALLERGIES',
        course_type="Course"
    ):
        return Course.objects.create(
            name=name,
            slug=slug,
            description=description,
            price=price,
            allergens=allergens,
            course_type=course_type
            )

    def test_model_str_course(self):
        course = Course.objects.create(name="Course", price="10")
        self.assertEqual(str(course), "Course")

    def test_the_event_form_model(
        self,
        user_email='test_user',
        first_name='FirstName',
        last_name='LastName',
        phone_no="+2144455566",
        event_date="2022-12-12"
    ):
        return EventForm.objects.create(
            user_email=user_email,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
            event_date=event_date,
            )

    def test_model_str_event(self):
        event = EventForm.objects.create(
            first_name="First",
            last_name="Last",
            event_date='2022-12-12')
        self.assertEqual(str(event), event.first_name + " " + event.last_name)

    # def test_the_reservation_model(
    #     self,
    #     user=Client(),
    #     booking_name="Some Name",
    #     date="2022-12-12",
    #     booking_details="A lot of details",
    #     arrival_time="17:00",
    #     number_of_persons='4',
    #     allergies="No Allergies"
    # ):
    #     return Booking.objects.create(
    #         user=user,
    #         booking_name=booking_name,
    #         date=date,
    #         booking_details=booking_details,
    #         arrival_time=arrival_time,
    #         number_of_persons=number_of_persons,
    #         allergies=allergies
    #     )

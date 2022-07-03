from django.test import TestCase, Client


# Create your tests here.
class TestViews(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_our_restaurant_page(self):
        response = self.client.get('/our-restaurant/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'our-restaurant.html')

    def test_get_reservation_page_login(self):
        c = Client()
        c.login(username='test_client', password='somepassword')
        response = self.client.get('/booking/')
        self.assertEqual = (response.status_code, 200)

    def test_get_menu_page(self):
        response = self.client.get('/menu/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_get_gallery_page(self):
        response = self.client.get('/gallery/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_get_team_page(self):
        response = self.client.get('/team/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'team.html')

    def test_get_faq_page(self):
        response = self.client.get('/faq/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')

    def test_get_events_page(self):
        response = self.client.get('/events/')
        self.assertEqual = (response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')

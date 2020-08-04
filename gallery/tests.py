from django.test import TestCase
from .models import categories,location,Gallery

# Create your tests here.
class categoriesTestCase(TestCase):
    def setUp(self):
        self.travel = categories(name = 'travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel, categories))

    def test_save_method(self):
        self.travel.save_category()
        category = categories.objects.all()
        self.assertTrue(categories)

class locationTestCase(TestCase):
    def setup(self):
        self.Zambia = location(name = 'Zambia')

    def test_instance(self):
        self.assertTrue(isinstance(self.Zambia,location))

    def test_save_method(self):
        self.Zambia.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations)>0)

class GalleryTestCase(TestCase):
    def setUp(self):
        self.Rusle = Image(name = 'Rusle', description = 'car of my dreams')
        self.Rusle.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.Rusle, Image))

    def test_save_method(self):
        self.Rusle.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

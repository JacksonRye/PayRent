from django.test import TestCase
from houses.forms import HouseUploadForm

class HouseUploadFormTest(TestCase):
    def test_house_upload_address_label(self):
        form = HouseUploadForm()
        self.assertTrue(form.fields['address'].label is None or
                        form.fields['address'].label == 'address'.title())

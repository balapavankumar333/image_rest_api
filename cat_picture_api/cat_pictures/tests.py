import os
from tempfile import TemporaryDirectory

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import CatPicture

class CatPictureAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.temp_dir = TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_temp_file(self, filename):
        return os.path.join(self.temp_dir.name, filename)

    def test_upload_cat_picture(self):
        # Create a temporary file for the cat picture
        cat_picture_path = self._create_temp_file('cat_picture.jpg')
        with open(cat_picture_path, 'wb') as image_file:
            # Write some dummy data to the file
            image_file.write(b'Test image data')

        # Upload the cat picture
        with open(cat_picture_path, 'rb') as image_file:
            response = self.client.post(reverse('cat-picture-list-create'), {'image': image_file}, format='multipart')

        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the cat picture object is created in the database
        self.assertTrue(CatPicture.objects.exists())

    def test_fetch_cat_picture_list(self):
        # Create some cat pictures
        CatPicture.objects.create(image=self._create_temp_file('cat_picture1.jpg'))
        CatPicture.objects.create(image=self._create_temp_file('cat_picture2.jpg'))

        # Fetch list of cat pictures
        response = self.client.get(reverse('cat-picture-list-create'))

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the correct number of cat pictures are returned
        self.assertEqual(len(response.data), 2)

    def test_fetch_cat_picture_by_id(self):
        # Create a cat picture
        cat_picture = CatPicture.objects.create(image=self._create_temp_file('cat_picture.jpg'))

        # Fetch the cat picture by ID
        response = self.client.get(reverse('cat-picture-retrieve-update-destroy', kwargs={'pk': cat_picture.pk}))

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the correct cat picture is returned
        self.assertEqual(response.data['id'], cat_picture.pk)

    def test_delete_cat_picture(self):
        # Create a cat picture
        cat_picture = CatPicture.objects.create(image=self._create_temp_file('cat_picture.jpg'))

        # Delete the cat picture
        response = self.client.delete(reverse('cat-picture-retrieve-update-destroy', kwargs={'pk': cat_picture.pk}))

        # Check if the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the cat picture is deleted from the database
        self.assertFalse(CatPicture.objects.exists())

    def test_update_cat_picture(self):
        # Create a cat picture
        cat_picture = CatPicture.objects.create(image=self._create_temp_file('cat_picture.jpg'))

        # Create a temporary file for the updated cat picture
        updated_cat_picture_path = self._create_temp_file('updated_cat_picture.jpg')
        with open(updated_cat_picture_path, 'wb') as updated_image_file:
            # Write some dummy data to the file
            updated_image_file.write(b'Updated test image data')

        # Update the cat picture
        with open(updated_cat_picture_path, 'rb') as updated_image_file:
            response = self.client.put(reverse('cat-picture-retrieve-update-destroy', kwargs={'pk': cat_picture.pk}),
                                       {'image': updated_image_file}, format='multipart')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the cat picture object from the database
        cat_picture.refresh_from_db()

        # Check if the cat picture is updated with the new image
        self.assertNotEqual(cat_picture.image.url, 'path/to/cat_picture.jpg')

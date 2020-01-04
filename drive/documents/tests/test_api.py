from tempfile import TemporaryFile

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class DocumentsAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="user2@example.com", password="somethinghard2no"
        )
        self.metadata_url = "/api/v1/metadata/"
        self.doc_url = "/api/v1/documents/"

    def test_user_can_upload_metadata(self):
        self.client.force_login(self.user)
        data = {
            'name': 'test',
            'string': 'test'
        }
        resp = self.client.post(self.metadata_url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_user_can_upload_document(self):
        self.client.force_login(self.user)
        simple_file = SimpleUploadedFile("txt.txt", b"some content")

        data = {
            'name': 'test',
            'file': simple_file
        }
        resp = self.client.post(self.doc_url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

from tempfile import TemporaryFile

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from drive.documents.models import Metadata, Document
from drive.documents.serializers import MetadataSerializer, DocumentSerializer

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

    def test_user_can_view_metadata_by_name(self):
        metadata = Metadata.objects.create(user=self.user, name='test_1', string="test 1")
        self.client.force_login(self.user)
        resp = self.client.get(f"{self.metadata_url}test_1/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        serializer = MetadataSerializer(metadata)
        self.assertEqual(resp.data, serializer.data)

    def test_user_can_view_document_by_name(self):
        doc = Document.objects.create(
            user=self.user,
            name='test_1',
            file=SimpleUploadedFile("txt.txt", b"some content")
        )
        self.client.force_login(self.user)
        resp = self.client.get(f"{self.doc_url}test_1/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['name'], doc.name)
        self.assertIn(doc.file.url, resp.data['file'])

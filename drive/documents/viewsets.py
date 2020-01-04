from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated

from drive.documents.models import Metadata, Document
from drive.documents.serializers import MetadataSerializer, DocumentSerializer


class MetadataViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        GenericViewSet):
    queryset = Metadata.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MetadataSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        GenericViewSet):
    queryset = Document.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

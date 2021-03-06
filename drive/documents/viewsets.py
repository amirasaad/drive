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
    """
        Api endpoint for list, retrieve and upload metadata.
    """

    queryset = Metadata.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MetadataSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentViewSet(
        mixins.CreateModelMixin,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        GenericViewSet):
    """
    Api endpoint for list, retrieve and upload document.
    """

    queryset = Document.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DocumentSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

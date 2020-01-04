from rest_framework.routers import DefaultRouter

from drive.documents.viewsets import MetadataViewSet, DocumentViewSet

documents_router = DefaultRouter()

documents_router.register(r'metadata', MetadataViewSet, basename='metadata')
documents_router.register(r'documents', DocumentViewSet, basename='document')

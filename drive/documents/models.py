from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel

User = get_user_model()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Metadata(TimeStampedModel):
    user = models.ForeignKey(User, related_name='metadata', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    string = models.CharField(max_length=255)


class Document(TimeStampedModel):
    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to=user_directory_path)

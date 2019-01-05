import string
from random import random

from django.db import models

# Create your models here.
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings


class PeptideStructureData(models.Model):
    email = models.EmailField()
    sequence = models.CharField(max_length=1000)
    file = models.FileField(storage=FileSystemStorage(location=settings.BASE_DIR),
                                   upload_to="media/modelData/upload/", default='NULL')
    status = models.CharField(max_length=20)


from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    vk_id = models.CharField(max_length=200)
    inst_id = models.CharField(max_length=200)

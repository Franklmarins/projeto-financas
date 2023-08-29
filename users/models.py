from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __repr__(self) -> str:
        return f"<User: {self.id}_{self.username}>"

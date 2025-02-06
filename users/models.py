from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserProfile(BaseModel):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255 , default='Tashkent')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
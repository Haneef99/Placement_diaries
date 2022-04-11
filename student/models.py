from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=now , editable=False)

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings
# Create your models here.
class PGlisting(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    rent=models.PositiveIntegerField()
    sharing_type=models.CharField(max_length=250,choices=[
        ('single','Single'),
        ('double','Double'),
        ('triple','Triple'),
    ])
    room_type=models.CharField(max_length=250,choices=[('ac','AC'),('non_ac','non_AC')])
    facilities=models.TextField(help_text='comma-separated list of facilities')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.location}'
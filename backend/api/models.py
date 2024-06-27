from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #automaticaly added date when created
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
     # on_delete means when we delete the User all his notes will be deleted; related_name means that if we put User.notes we will be able to see all his notes

    def __str__(self):
        return self.title

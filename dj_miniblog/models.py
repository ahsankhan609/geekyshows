from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    '''A model class that represents a blog post with a title, description, creation date and author.
    '''
    # a char field for the title of the post, with a maximum length of 255 characters    
    title = models.CharField(max_length=255)
    
    # a text field for the description of the post
    description = models.TextField()
    
    # a date time field for the creation date of the post, with auto_now_add set to True to automatically set the current date and time 
    created_at = models.DateTimeField(auto_now_add=True)
    
    # a foreign key field for the author of the post, referencing the User model
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.title

from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete

# Define a custom model class called Post that inherits from models.Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    
    # Define a string representation method for the Post model
    def __str__(self):
        return self.title
    
# create a receiver
def pre_save_post(sender, instance, **kwargs):
    print('Pre Saving post.....')
    
def post_save_post(sender, instance, **kwargs):
    print('Post Saving post.....')

def pre_delete_post(sender, instance, **kwargs):
    print('Pre Deleting post.....')

def after_delete_post(sender, instance, **kwargs):
    print('After Deleting post.....')

# create a Signal, when something happens
pre_save.connect(pre_save_post, sender=Post)
post_save.connect(post_save_post, sender=Post)

pre_delete.connect(pre_delete_post, sender=Post)
post_delete.connect(after_delete_post, sender=Post)
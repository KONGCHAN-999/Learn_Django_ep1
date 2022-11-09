from distutils.command.upload import upload
from email.mime import image
from turtle import update
from django.db import models
from django.utils.html import format_html

# Create your models here.

# class Blog_body(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     dcs = models.TextField()
#     image = models.ImageField(upload_to='medie', null='True', blank='True')
#     dete = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)
    
#     def show_image_pic(self):
#         if self.image:
#             return format_html('<img src="%s" height="50px">' % self.image.url)
#         return 'NULL'

#     show_image_pic.allow_tags =True

#     def __str__(self):
#         return self.title

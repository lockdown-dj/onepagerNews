from django.db import models
from datetime import datetime

# Create your models here.

class News(models.Model):  
    is_news = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    heading_one = models.CharField(max_length=250)
    heading_two = models.CharField(max_length=250 , blank = True)
    heading_three = models.CharField(max_length=250 , blank = True)

    image_one = models.ImageField(upload_to='media/images/')
    image_two = models.ImageField(upload_to='media/images/')
    image_three = models.ImageField(upload_to='media/images/')
    image_four = models.ImageField(upload_to='media/images/') 
    image_five = models.ImageField(upload_to='media/images/')
    image_six = models.ImageField(upload_to='media/images/',blank = True) 
    image_seven = models.ImageField(upload_to='media/images/',blank = True)
    image_eight = models.ImageField(upload_to='media/images/',blank = True)
    image_nine = models.ImageField(upload_to='media/images/',blank = True)

    para_one = models.TextField()    
    para_two = models.TextField(blank = True)     
    para_three = models.TextField(blank = True)    
    para_four = models.TextField(blank = True)    
    para_five = models.TextField(blank = True)    
    para_six = models.TextField(blank = True)    
    para_seven = models.TextField(blank = True)     
    para_eight = models.TextField(blank = True)    
    para_nine = models.TextField(blank = True)

    # def __str__(self):
    #     return self.name


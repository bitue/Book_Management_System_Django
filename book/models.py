from django.db import models

# Create your models here.


class Book(models.Model):
    CATEGORY =(
        ('Mystery', 'Mystery'),
        ('Science', 'Science'),
        ('Fiction', 'Fiction'),
        ('Engineering', 'Engineering'),
        
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    category = models.CharField(max_length=100 , choices=CATEGORY )
    first_published = models.DateTimeField(auto_now_add=True)
    last_published = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.book_name 

from django.db import models
genderC = (('male','female'),('female','female'))

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=100,choices=genderC)
    
    def __str__(self) -> str:
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=100)
    book_type = models.CharField(max_length=200)
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


# Create your models here.

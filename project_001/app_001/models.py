from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True, help_text="Short biography of the author", max_length=200)

    def __str__(self):
        return f"{self.full_name} {self.birth_date}"

class Profile(models.Model):
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')

class Book(models.Model):
    title = models.CharField(max_length=300)
    published_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

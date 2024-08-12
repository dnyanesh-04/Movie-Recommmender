from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='movie_images/')
    recommendations = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.title


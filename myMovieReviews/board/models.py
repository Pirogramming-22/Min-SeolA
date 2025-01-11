from django.db import models

# Create your models here.

class Board(models.Model):
    AGE_CHOICES=[
        ('G', '전체'),
        ('PG', '12'),
        ('F15', '15'),
        ('R', '청불'),
    ]

    MOVIE_GENRE_CHOICES =[
        ('ACTION', 'Action'),
        ('DRAMA', 'Drama'),
        ('COMEDY', 'Comedy'),
        ('THRILLER', 'Thriller'),
        ('HORROR', 'Horror'),
        ('SCI_FI', 'Sci-Fi'),
        ('ROMANCE', 'Romance'),
        ('DOCUMENTARY', 'Documentary'),
        ('ANIMATION', 'Animation'),
        ('FANTASY', 'Fantasy'),
        ('MUSIC', 'Music'),
        ('MUSICAL', 'Musical'),
    ]

    title=models.CharField(max_length=200)
    release=models.CharField(max_length=4)
    genre=models.CharField(choices=MOVIE_GENRE_CHOICES, default='ACTION', max_length=200)
    age=models.CharField(choices=AGE_CHOICES, default='G', max_length=200)
    rate=models.CharField(max_length=200)
    runningtime=models.CharField(max_length=200)
    review=models.TextField()
    director=models.CharField(max_length=200)
    actor=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    
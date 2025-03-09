from django.db import models
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Pole tekstowe do 200 znaków
    content = models.TextField()  # Pole do przechowywania większego tekstu
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia
    views = models.PositiveIntegerField(default=0)  # Licznik wyświetleń
    likes = models.PositiveIntegerField(default=0)  # Licznik polubień

    def __str__(self):
        return self.title  # Zwraca tytuł w panelu administracyjnym


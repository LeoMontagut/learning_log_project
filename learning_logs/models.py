from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Un tema del que el usuario este aprendiendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        # Si el texto ingresado es menor de 50 caracteres se imprime todo, sino "..."
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text

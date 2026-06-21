from django.db import models

class Experience(models.Model):
    TYPE_CHOICES = [
        ('academic',     'Academic'),
        ('professional', 'Professional'),
    ]
    title        = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date   = models.CharField(max_length=50)
    end_date     = models.CharField(max_length=50)
    description  = models.TextField()
    exp_type     = models.CharField(max_length=20, choices=TYPE_CHOICES, default='academic')
    order        = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} at {self.organization}"

    class Meta:
        ordering = ['order']

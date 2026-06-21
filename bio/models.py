from django.db import models

class Bio(models.Model):
    name        = models.CharField(max_length=100)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    email       = models.EmailField(blank=True)
    github      = models.URLField(blank=True)
    linkedin    = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bio'

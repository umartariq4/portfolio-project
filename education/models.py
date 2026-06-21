from django.db import models

class Education(models.Model):
    institution  = models.CharField(max_length=200)
    degree       = models.CharField(max_length=200)
    field        = models.CharField(max_length=200, blank=True)
    start_year   = models.CharField(max_length=10)
    end_year     = models.CharField(max_length=20)   # allows "Present"
    description  = models.TextField(blank=True)
    order        = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.degree} — {self.institution}"

    class Meta:
        ordering = ['order']

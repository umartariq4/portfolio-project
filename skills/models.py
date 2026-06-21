from django.db import models

class SkillCategory(models.Model):
    name  = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering          = ['order']
        verbose_name_plural = 'Skill Categories'

class Skill(models.Model):
    category    = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=80, help_text='0-100')

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['-proficiency']

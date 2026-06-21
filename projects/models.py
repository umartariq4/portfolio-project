from django.db import models

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack  = models.CharField(max_length=500, help_text='Comma-separated: Python, Django, ...')
    github_url  = models.URLField(blank=True)
    live_url    = models.URLField(blank=True)
    order       = models.PositiveIntegerField(default=0)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

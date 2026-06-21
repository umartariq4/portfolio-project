from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import SkillCategory
from experience.models import Experience
from projects.models import Project

def index(request):
    bio              = Bio.objects.first()
    education        = Education.objects.all().order_by('order')
    skill_categories = SkillCategory.objects.prefetch_related('skill_set').order_by('order')
    experience       = Experience.objects.all().order_by('order')
    projects         = Project.objects.all().order_by('order')

    return render(request, 'index.html', {
        'bio':              bio,
        'education':        education,
        'skill_categories': skill_categories,
        'experience':       experience,
        'projects':         projects,
    })

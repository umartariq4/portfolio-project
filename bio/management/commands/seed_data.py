from django.core.management.base import BaseCommand
from bio.models import Bio
from education.models import Education
from skills.models import SkillCategory, Skill
from experience.models import Experience
from projects.models import Project


class Command(BaseCommand):
    help = 'Seed portfolio database with Muhammad Umar Tariq\'s data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding portfolio data...')

        # ── Bio ────────────────────────────────────────────────────────────
        Bio.objects.all().delete()
        Bio.objects.create(
            name='Muhammad Umar Tariq',
            title='AI Engineer · Computer Science Student',
            description=(
                'A computer science undergraduate at the University of Management and Technology, '
                'focused on building intelligent systems at the intersection of machine learning '
                'and software engineering. With hands-on experience in deep learning, natural '
                'language processing, and computer vision, I approach problems with an engineering '
                'mindset — designing solutions that are both theoretically grounded and practically '
                'deployable. Currently exploring the frontier of large language models and AI agents.'
            ),
            profile_picture='profile/umar.jpg',
            email='13.90abdul@gmail.com',
            github='https://github.com/umartariq4',
            linkedin='https://www.linkedin.com/in/umar-tariq-57b95b2a1/',
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Bio'))

        # ── Education ──────────────────────────────────────────────────────
        Education.objects.all().delete()
        Education.objects.create(
            institution='University of Management and Technology (UMT)',
            degree='Bachelor of Science in Computer Science',
            field='BS Computer Science',
            start_year='2023',
            end_year='2027',
            description=(
                'Studying core CS fundamentals alongside advanced AI and machine learning '
                'coursework including algorithms, data structures, web technologies, and '
                'intelligent systems design.'
            ),
            order=1,
        )
        Education.objects.create(
            institution='Forman Christian College University (FCCU)',
            degree='Higher Secondary School Certificate (Intermediate)',
            field='Pre-Engineering / ICS',
            start_year='2021',
            end_year='2023',
            description=(
                'Completed intermediate education with a strong foundation in mathematics, '
                'physics, and computer science, building the analytical base for engineering studies.'
            ),
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Education'))

        # ── Skills ─────────────────────────────────────────────────────────
        SkillCategory.objects.all().delete()

        ai_cat = SkillCategory.objects.create(name='AI / Machine Learning', order=1)
        for name, pct in [('Python', 90), ('TensorFlow / Keras', 80), ('PyTorch', 75),
                          ('Scikit-learn', 82), ('NLP & Transformers', 78), ('Computer Vision', 74)]:
            Skill.objects.create(category=ai_cat, name=name, proficiency=pct)

        web_cat = SkillCategory.objects.create(name='Web Development', order=2)
        for name, pct in [('Django', 85), ('REST APIs', 80), ('HTML / CSS', 88),
                          ('JavaScript', 75), ('Bootstrap', 78)]:
            Skill.objects.create(category=web_cat, name=name, proficiency=pct)

        self.stdout.write(self.style.SUCCESS('  ✓ Skills'))

        # ── Experience ─────────────────────────────────────────────────────
        Experience.objects.all().delete()
        Experience.objects.create(
            title='Ruby on Rails Junior Developer',
            organization='Techionik',
            start_date='2025',
            end_date='Present',
            description=(
                'Building and maintaining web applications using Ruby on Rails. '
                'Contributing to full-stack feature development, database design, '
                'and API integration in a professional product environment.'
            ),
            exp_type='professional',
            order=1,
        )
        Experience.objects.create(
            title='Entrepreneur',
            organization='Independent',
            start_date='2025',
            end_date='Present',
            description=(
                'Founded and operate independent ventures at the intersection of technology '
                'and digital growth. Focused on building scalable systems, identifying market '
                'opportunities, and executing strategies that deliver measurable results.'
            ),
            exp_type='professional',
            order=2,
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Experience'))

        # ── Projects ───────────────────────────────────────────────────────
        Project.objects.all().delete()
        Project.objects.create(
            title='Scaled Client to 50K via Organic Marketing',
            description=(
                'Designed and executed a full organic growth strategy for a client, '
                'scaling their audience from zero to 50,000 through content systems, '
                'community building, and data-driven distribution — no paid ads.'
            ),
            tech_stack='Growth Strategy, Content Systems, Analytics, SEO',
            order=1,
        )
        Project.objects.create(
            title='Personal AI Chatbot',
            description=(
                'Built a private conversational AI assistant tailored to personal workflows. '
                'Integrated with a large language model API, featuring persistent context, '
                'custom instructions, and a minimal clean interface for daily use.'
            ),
            tech_stack='Python, OpenAI API, Django, JavaScript, HTML/CSS',
            github_url='https://github.com/umartariq4',
            order=2,
        )
        Project.objects.create(
            title='Image Classification Model',
            description=(
                'Trained a convolutional neural network for multi-class image classification. '
                'Experimented with architecture design and transfer learning to achieve '
                'high accuracy on a custom dataset.'
            ),
            tech_stack='Python, TensorFlow, Keras, NumPy, Jupyter',
            github_url='https://github.com/umartariq4',
            order=3,
        )
        self.stdout.write(self.style.SUCCESS('  ✓ Projects'))

        self.stdout.write(self.style.SUCCESS('\n✅  Database seeded successfully!'))

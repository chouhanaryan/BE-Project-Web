from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser

DOMAIN_CHOICES = [
    ("Data Mining & Analytics", ("Data Mining & Analytics")),
    ("Machine Learning", ("Machine Learning")),
    ("Deep Learning", ("Deep Learning")),
    ("Image Processing/Computer Vision", ("Image Processing/Computer Vision")),
    (
        "Natural Language Processing/Artificial Intelligence",
        ("Natural Language Processing/Artificial Intelligence"),
    ),
    ("Networking/Security", ("Networking/Security")),
    ("Internet of Things(IOT)", ("Internet of Things(IOT)")),
    ("Mobile Computing", ("Mobile Computing")),
    ("Big Data", ("Big Data")),
    ("Cloud Computing", ("Cloud Computing")),
    (
        "Computer Vision & Artificial Intelligence",
        ("Computer Vision & Artificial Intelligence"),
    ),
    ("Blockchain", ("Blockchain")),
    ("Operating Systems", ("Operating Systems")),
    ("GAN's", ("GAN's")),
    ("Audio Processing", ("Audio Processing")),
    ("Video Processing", ("Video Processing")),
    ("Cryptography", ("Cryptography")),
]

YEAR_CHOICES = [("FE", ("FE")), ("SE", ("SE")), ("TE", ("TE")), ("BE", ("BE"))]

DIVISON_CHOICES = [("A", ("A")), ("B", ("B"))]


class User(AbstractUser):
    is_contributor = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, related_name="teacher_user", on_delete=models.CASCADE, primary_key=True
    )

    # additional attributes
    subject = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Contributor(models.Model):
    user = models.OneToOneField(
        User,
        related_name="contributor_user",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    project = models.ManyToManyField(Project, related_name="contributors")
    year = models.CharField(
        choices=YEAR_CHOICES, default="None", null=False, blank=False, max_length=3
    )
    divison = models.CharField(
        choices=DIVISON_CHOICES, default="None", null=False, blank=False, max_length=2
    )
    github_id = models.URLField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


# In house Project model
class Project(models.Model):
    # Project title
    title = models.CharField(max_length=100, null=False, blank=False)

    # Id of the teacher mentoring the project
    teacher = models.ForeignKey(
        Teacher, related_name="project", on_delete=models.CASCADE
    )

    # project description
    description = models.TextField(null=False, blank=False)

    # project abstract
    abstract = models.TextField(null=False, blank=False)

    # year published and created will be stored
    # year_created = models.DateField(default=date.today)
    year_created = models.PositiveSmallIntegerField(
        default=int(str(date.today())[:4]), null=False, blank=False
    )

    # Domain list
    domain = models.CharField(
        choices=DOMAIN_CHOICES, default="None", null=False, blank=False, max_length=100
    )

    # PDF to be uploaded
    report = models.FileField(null=True, blank=True)

    # Executable to be uploaded
    executable = models.FileField(null=True, blank=True)

    # GitHub repo link
    github_repo = models.URLField(null=True, blank=True)

    # URL of the video demo
    demo_video = models.URLField(null=True, blank=True)

    # To check whether project is approved or not
    approved = models.BooleanField(default=False)

    # Boolean field to check whether the project is inhouse or outhouse
    is_inhouse = models.BooleanField(default=True)

    is_hackathon_project = models.BooleanField(default=False)

    awards = models.TextField(blank=True, default="None")

    # Property of an outhouse project
    company = models.CharField(max_length=100, blank=True, default="None")

    supervisor = models.CharField(max_length=100, blank=True, default="None")

    journal = models.CharField(max_length=100, blank=True, default="None")

    def publish(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.title

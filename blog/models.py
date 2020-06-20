from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager


class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts') 
    body = models.TextField() 
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 

    objects = models.Manager()
    published = PublishedManager() 
    tags = TaggableManager()

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Department(models.Model):
    """Department model
    Has many course"""
    # Deparment name.
    name = models.CharField(max_length=225)
    # Department description. Optional
    number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])
    no_courses = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True)
    objects = models.Manager()



    def __str__(self):
        return self.name 

class Courses(models.Model):
    """Course model.
    belong to Department
    """
    COURSES_CODE = (
        ("12101", "TM"), # Technical Mathematics
        ("12102", "PY"), # Physics 
        ("12104", "LG"), # Languages 
        ("12105", "ME"), # Mechanics, Biomechanics and Mechatronics
        ("12110", "IC"), # Instrumentation and Control Engineering
        ("12112", "FT"), # Fluid Dynamics and Thermodynamics
        ("12113", "DM"), # Designing and Machine Components
        ("12115", "EN"), # Energy Engineering
        ("12116", "EE"), # Environmental Engineering
        ("12118", "PE"), # Process Engineering
        ("12120", "AU"), # Automotive, Combustion Engine and Railway Engineering 
        ("12122", "AE"), # Aerospace Engineering
        ("12132", "MT"), # Materials Engineering
        ("12133", "MF"), # Manufacturing Technology
        ("12134", "MP"), # Machining, Process Planning and Metrology
        ("12135", "PM"), # Production Machines and Equipment
        ("12138", "EM"), # Management and Economics
    )
    # Course title. Required
    title = models.CharField(max_length=225)
    # Courses code tags related.
    code = models.CharField(max_length=5, choices=COURSES_CODE, default="12101")

    def __str__(self):
        return f"{self.code} {self.title}"



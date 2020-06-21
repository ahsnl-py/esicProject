from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager


class Department(models.Model):
    """Department model.

    Has many courses
    """

    DEPARTMENT_CODE = (
        ("TM", "12101"), # Technical Mathematics
        ("PY", "12102"), # Physics 
        ("LG", "12104"), # Languages 
        ("ME", "12105"), # Mechanics, Biomechanics and Mechatronics
        ("IC", "12110"), # Instrumentation and Control Engineering
        ("FT", "12112"), # Fluid Dynamics and Thermodynamics
        ("DM", "12113"), # Designing and Machine Components
        ("EN", "12115"), # Energy Engineering
        ("EE", "12116"), # Environmental Engineering
        ("PE", "12118"), # Process Engineering
        ("AU", "12120"), # Automotive, Combustion Engine and Railway Engineering 
        ("AE", "12122"), # Aerospace Engineering
        ("MT", "12132"), # Materials Engineering
        ("MF", "12133"), # Manufacturing Technology
        ("MP", "12134"), # Machining, Process Planning and Metrology
        ("PM", "12135"), # Production Machines and Equipment
        ("EM", "12138"), # Management and Economics
    )
    # Deparment name.
    name = models.CharField(max_length=225)
    # Courses code tags related.
    dept_code = models.CharField(max_length=5, choices=DEPARTMENT_CODE, default="TM")
    # Department description. Optional
    no_courses = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True)


    objects = models.Manager()

    def __str__(self):
        return self.name 

class Courses(models.Model):
    """Course model.

    Belong to a Department
    Has many post
    """
    # Course title. Required
    title = models.CharField(max_length=225)
    # Courses code tags related.
    sub_code = models.CharField(max_length=7)
    # Post primary Key
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    # Department choices
    objects = models.Manager()

    def __str__(self):
        return self.title



class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """Post Model.
    
    Belongs to a course.
    Has many authors 
    """
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
    courses = models.ManyToManyField(Courses)

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






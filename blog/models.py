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
    # Deparment name.
    department_name = models.CharField(max_length=225)
    #department slug for urls
    department_slug = models.CharField(max_length=100)
    # Department description. Optional
    no_subject = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True)
    # dept_code. Optional
    dept_code = models.IntegerField(null=True)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        return self.department_name 

class Subject(models.Model):
    """Course model.

    Belong to a Department
    Has many post
    """
    subject_name = models.CharField(max_length=250)
    # slug subject for url
    subject_slug = models.CharField(max_length=200)
    # foreign key department 
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.subject_name

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
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
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
    image = models.FileField(null=True, blank=True)

    objects = models.Manager()
    published = PublishedManager() 
    tags = TaggableManager()

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title

    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title


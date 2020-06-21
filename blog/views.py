from django.shortcuts import render, get_object_or_404 
from django.shortcuts import render 
from django.core.mail import send_mail
from .models import Post, Department, Courses
from django.contrib import messages
from .share import EmailPostForm


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_share(request, post_id):
    #retrive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submmited
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                                          post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
            messages.success(request, f'E-mail is sent successfully.')
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})

def department(request): 
    """View for department page."""
    dept = Department.objects.all()
    return render(request, 'blog/department.html', {'department': dept})

def course_list(request):
    """View for list of courses"""
    courses = Courses.objects.values_list('title', 'dept_id')
    return render(request, 'blog/course_list.html', {'course': courses})


    

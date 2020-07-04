from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Post, Department, Subject
from django.contrib import messages
from .share import EmailPostForm


def single_slug(request, single_slug):
    departments = [d.department_slug for d in Department.objects.all()]
    object_list = Post.published.all()
    
    # list all the subjects by department 
    if single_slug in departments:
        matching_subjects = Subject.objects.filter(department_name__department_slug=single_slug)
        
        subject_urls = {}
        for m in matching_subjects.all():
            part_one = object_list.filter(subject_name__subject_name=m.subject_name).earliest('publish')
            subject_urls[m] = part_one.slug
        
        return render(request, "blog/departments.html", {'subject_name': matching_subjects, "part_ones": subject_urls})

    # list all the post by the subject 
    post = [p.slug for p in object_list]
    if single_slug in post:
        posts = get_object_or_404(Post, slug=single_slug)
        post_from_subjects = Post.published.filter(subject_name__subject_name=posts.subject_name)
        
        this_post_idx = list(post_from_subjects).index(posts)

        return render(request, 'blog/post/discussion.html', {'post': posts, 'list_post_subjects': post_from_subjects, 'this_post_idx': this_post_idx})

    return HttpResponse(f"'{single_slug}' is not registesred!'")
    
def departments(request):
    departments = Department.objects.all()
    return render(request, 'blog/department.html', {'departments': departments})


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



    

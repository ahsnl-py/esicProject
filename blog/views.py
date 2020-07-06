import os

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.urls import path
from django.views.generic import (
    CreateView, 
    DetailView, 
    UpdateView, 
    DeleteView,
    ListView
    #FormView
)

from .forms import PostModelForm, FileModelForm
from .share import EmailPostForm
from .models import (
    Post, 
    Department, 
    Subject,
    PostImage,
    PostFile
)


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


"""class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subject_name', 'body', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)"""

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subject_name', 'body', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-publish']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.published.filter(author=user).order_by('-publish')

def file_view(request):
    #current_user = request.user_posts
    post = Post.published.all()
    files = PostFile.objects.all() 
    context = {
        'post': post,
        'files': files
    }
    return render(request, 'blog/post_detail.html', context)

def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.android.package-archive")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def post_create(request):
    user = request.user
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=request.user)
        file_form = FileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file') #field name in model
        if form.is_valid() and file_form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.user = user
            post_instance.save()
            for f in files:
                file_instance = PostFile(file=f, post=post_instance)
                file_instance.save()      

    else:
        form = PostModelForm(instance=request.user)
        file_form = FileModelForm()
    return render(request, 'blog/post/post_form.html', {'form': form, 'file_form': file_form})
    



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


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page_obj': page, 'posts': posts})



def post_detail_old(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
    

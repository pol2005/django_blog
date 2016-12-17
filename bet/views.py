# coding=utf-8
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Article,Block,Prognostika,Newsletter
from django.db.models import Count
from .forms import NewsletterForm,LoginForm, UserRegistrationForm,UserEditForm,ContactForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .common.decorators import ajax_required

def index(request):
    block1 = Block.published.filter(sidebar='arxiki1')[:1]
    block2 = Block.published.filter(sidebar='arxiki2')[:1]
    block3 = Block.published.filter(sidebar='arxiki3')[:1]
    return render(request, "index.html",{'block1': block1, 'block2':block2,'block3':block3})

def kouponi(request):
    return render(request, "bet/kouponi.html")

def bonus(request):
    return render(request, "bet/bonus.html")

def tables(request):
    return render(request, "bet/tables.html")

def apodoseis(request):
    return render(request, "bet/apodoseis.html")

def statistika(request):
    return render(request, "bet/statistika.html")

def asianhandicap(request):
    return render(request, "bet/asianhandicap.html")

def tziroi(request):
    return render(request, "bet/tziroi.html")

def livestreaming(request):
    return render(request, "bet/livestreaming.html")

def livescore(request):
    return render(request, "bet/kouponi.html")

class PrognostikaListView(ListView):
    model = Prognostika

def contact(request):
    sent = False
    if request.method == 'POST':
       # Form was submitted
       form = ContactForm(request.POST)
       if form.is_valid():
           # Form fields passed validation
           cd = form.cleaned_data
           subject = '{}  Message from  "{}"'.format(cd['name'], cd['email'])
           message = 'Read  at {}\n\n{}\'s comments: '.format(cd['name'], cd['comments'])
           send_mail(subject, message, cd['email'],['betvisionsports@gmail.com'])
           sent = True
           # ... send email
    else:
       form = ContactForm()
    return render(request, 'bet/contact.html', {'form': form, 'sent':sent})

def post_list(request, tag_slug = None):
    object_list = Article.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 15)  # 2 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'bet/article_list.html', {'page': page, 'posts': posts, 'tag': tag})

def analiseis(request):
    object_list = Article.published.filter(tags__name__in=["Αναλύσεις Βόλλευ","Αναλύσεις Τένις"])
    paginator = Paginator(object_list, 15)  # 2 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'bet/article_analiseis.html', {'page': page, 'posts': posts})

def post_detail(request,post,year,month,day,):
    post = get_object_or_404(Article,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Article.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]
    show_image = post.tags.slugs()
    return render(request, 'bet/article.html', {'post': post, 'similar_posts': similar_posts,'show_image':show_image})


def newsletter(request):
    if request.method == 'POST':
        newsletter = NewsletterForm(data=request.POST)
        if newsletter.is_valid():
            newsletter.save()
            messages.success(request, 'Το email σας προστέθηκε επιτυχώς')
            cssClass = 'success'
            return render(request,'index.html', {'cssClass': cssClass})

    else:
        newsletter = NewsletterForm()
        return redirect('/',request.META.get('HTTP_REFERER'))
    messages.error(request, 'Το email σας υπάρχει ηδη καταχωρημένο')
    cssClass = 'danger'
    return render(request, 'index.html', {'cssClass': cssClass})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Authenticated successfully')
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
   return render(request, 'registration/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
       user_form = UserRegistrationForm(request.POST)
       if user_form.is_valid():
           # Create a new user object but avoid saving it yet
           new_user = user_form.save(commit=False)
           # Set the chosen password
           new_user.set_password(user_form.cleaned_data['password'])
           # Save the User object
           new_user.save()
           return render(request,'registration/register_done.html',{'new_user': new_user})
    else:
       user_form = UserRegistrationForm()
    return render(request,'registration/register.html',{'user_form': user_form})

@login_required
def edit(request):
   if request.method == 'POST':
       user_form = UserEditForm(instance=request.user,
                                data=request.POST)

       if user_form.is_valid():
           user_form.save()
           messages.success(request, 'Profile updated '\
                                         'successfully')
       else:
           messages.error(request, 'Error updating your profile')
   else:
       user_form = UserEditForm(instance=request.user)

   return render(request,
                 'registration/edit.html',
                 {'user_form': user_form,})

@ajax_required
@require_POST
def ajax_newsletter(request):
    post_val = request.POST.get('newsmail')

    if post_val :
        newsletter = Newsletter(newsemail=post_val)
        saving = newsletter.save()
        if saving:
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'false'})
    else:
        return JsonResponse({'status': 'false'})

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect, response
from django.urls import reverse
from .forms import StudentPostForm,CreateUserForm,StudentForm,CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.utils import timezone

@login_required(login_url='login')
def LikeView(request,pk):
    print(pk)
    post=Post.objects.get(id=pk)
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
   # post=get_object_or_404(Post,id=request.POST.get('post_id'))
    #stuff=post.total_likes()
    
    return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))

@login_required(login_url='login')
def PostDetailView(request,pk):
    post=Post.objects.get(id=pk)
    s=Student.objects.get(name=post.name)
    total_likes=post.total_like()
    liked=False
    if(post.likes.filter(id=request.user.id).exists()):
        liked=True
    django_form= CommentForm()
    return render(request,'accounts/post_detail.html',{'s':s,'post':post,'t':total_likes,'liked':liked,'form':django_form})
@unauthenticated_user
def registerPage(request):
    

    form=CreateUserForm()


    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            new_member_name = form.data.get("username")
            new_member_phone = form.data.get("phone")
            new_member_email = form.data.get("email")
            new_member_section = form.data.get("section")
            new_member_branch =form.data.get("branch")
            
           # new_member_Propic = django_form.data.get("email")
        #  new_member_image = django_form.data.get("image")
            
            Student.objects.create(
                name= new_member_name,
                phone = new_member_phone,
                email=new_member_email,
                section=new_member_section,
                branch=new_member_branch,
                
                #image = new_member_image,
                
            )
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for '+user)
            return redirect('login')  
    context={'form':form}
    return render(request,'accounts/register.html',context)


@unauthenticated_user
def loginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password )
        if(user is not None):
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'username or password incorrect')
            return render(request,'accounts/login.html')
    context={}
    return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
   
    posts=Post.objects.order_by('-id')
    
    return render(request,'accounts/dashboard.html',{'posts':posts})
def testimonials(request):
    return render(request,'accounts/testimonials.html')

    
@login_required(login_url='login')
def students(request):
    st=Student.objects.get(name=str(request.user))
    s=Student.objects.get(id=st.id)
    sp=s.student_post_set.all()
    post_count=sp.count()
    c={'s':s,'sp':sp,'post_count':post_count}
    return render(request,'accounts/students.html',c)

@login_required(login_url='login')
def createPost(request):
    context={}
    django_form= StudentPostForm()
    if request.method =='POST':
        django_form= StudentPostForm(request.POST)
        if django_form.is_valid():
            new_member_title = django_form.data.get("title")
            new_member_desc = django_form.data.get("desc")
            
          #  new_member_image = django_form.data.get("image")
           
            st=Student.objects.get(name=str(request.user))
            Post.objects.create(
                # student=st.id,
                name=str(request.user),
                title = new_member_title,
                desc = new_member_desc,
                pub_date=timezone.localtime(),
                #image = new_member_image,
                
               )
            
               
            #print( new_member_image)
            # return render(request,'accounts/studentPostForm.html',{'form':django_form})
            context={'form':django_form}
            return HttpResponseRedirect(reverse('home'))
          
    else:
        django_form=StudentPostForm()
   
    return render(request,'accounts/studentPostForm.html',{'form':django_form})

@login_required(login_url='login')
def userPage(request):
    st=Student.objects.get(name=str(request.user))
    s=Student.objects.get(id=st.id)
    sp=Post.objects.filter(name=str(request.user)).order_by('-id')
    post_count=sp.count()
    c={'s':s,'sp':sp,'post_count':post_count}
    return render(request,'accounts/students.html',c)


@login_required(login_url='login')
def userPosts(request):
    
    posts=Post.objects.filter(name=str(request.user)).order_by('-id')
    c={'posts':posts}
    return render(request,'accounts/user.html',c)


@login_required(login_url='login')
def account_info(request):
    
    st=Student.objects.get(name=str(request.user))
    s=Student.objects.get(id=st.id)
    form=StudentForm(instance=s)
    if request.method =='POST':
        form=StudentForm(request.POST,request.FILES,instance=s)
        if(form.is_valid):
            form.save() 
    context={'form':form,'s':s}
    return render(request,'accounts/account_info.html',context)

@login_required(login_url='login')
def addComment(request,pk):
    context={}
    django_form= CommentForm()
    if request.method =='POST':
        django_form= CommentForm(request.POST)
        if django_form.is_valid():
            
            new_member_desc = django_form.data.get("body")
            k=Post.objects.get(id=pk)
          #  new_member_image = django_form.data.get("image")
           
            #st=Student.objects.get(name=str(request.user))
            Comment.objects.create(
                # student=st.id,
                post=Post.objects.get(id=pk),
                name=str(request.user),
                
                body = new_member_desc,
                date_added=timezone.localtime(),
                #image = new_member_image,
                
               )
            
               
            #print( new_member_image)
            # return render(request,'accounts/studentPostForm.html',{'form':django_form})
            context={'form':django_form}
            return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))
          
    else:
        django_form=CommentForm()
    return render(request,'accounts/add_comments.html',{'form':django_form})


def search_company(request):
    if request.method == "POST":
        searched=request.POST['searched']
        post=Post.objects.filter(title__contains=searched)
        return render(request,'accounts/search_company.html',{'searched':searched,'posts':post})
    else:
        return render(request,'accounts/search_company.html',{})

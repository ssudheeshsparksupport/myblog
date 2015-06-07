from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):

        return render(request,'blog/user_login.html')

class UserRegView(View):
    template_name = "blog/user_login.html"
    
    def get(self, request, *args, **kwargs):
        #pass
        print ('DDddd') 
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):       
        
        print ('ccccc')
        username=request.POST['username']
        print ('username>>',username)
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return HttpResponseRedirect('/')
        
        return render(request,self.template_name)
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password )
       
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/blog_post/')
        else:
            error = "Invalid Username or Password"
            return render(request, 'blog/user_login.html', {'error': error})
    else:
        return render(request, 'blog/user_login.html')


def blog_post(request):
    user = request.user
    if request.method == 'POST':
        details=Post()
        details.title=request.POST['title']
        details.author=user#foreign key posting
        details.photo=request.FILES['photo']
        details.content=request.POST['content']
        details.public=request.POST['checks']#checkbox posting
        details.created=request.POST['created']
        details.updated=request.POST['updated']
        details.published=request.POST['published']
        details.save()
        return HttpResponseRedirect('/post_list/')
    else:
        return render(request,'blog/blog_post.html',{'user':user})

class PostListView(View):
   
    def get(self, request):
        user = request.user
        author = Post.objects.filter(author=user)
        return render(request, 'blog/post_list.html', {
            'user' :user,
            'author':author,

        })

def post_view(request, id):
    user = request.user
    post=Post.objects.get(id=id)
    return render(request, 'blog/post_view.html', { 'post': post})


def post_edit(request, id):
    user = request.user
    post=Post.objects.get(id=id)
    if request.method == 'POST':
        post.title=request.POST['title']
        post.author=user
        post.photo=request.FILES['photo']
        post.content=request.POST['content']
        post.public=request.POST['checks']
        post.created=request.POST['created']
        post.updated=request.POST['updated']
        post.published=request.POST['published']
        post.save()
        return HttpResponse('success')

    return render(request, 'blog/post_edit.html', { 'post': post })

def passwordchange(request):
    print('AAAAA')
    return render(request, 'blog/passwordchange.html')

def test(request):
    return HttpResponse('success')

def test1(request):
    return HttpResponse('hello')



def logout_view(request):
    logout(request)
    return redirect('/user_login/')

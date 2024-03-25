from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def about(request):
    return render(request,'about-me.html')

def recent(request):
    return render(request,'recent-posts.html')

def addPost(request):
    return render(request,'add.html')

def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        des = request.POST.get('des')
        image = request.FILES.get('pic')
        if image:
            file_path = f"media/images/{image.name}"
            default_storage.save(file_path, ContentFile(image.read()))
        query = Blog(title= title, description=des, image=image)
        query.save()
        messages.success(request,"Details Added Successfully")
     
    return redirect('home')


def details(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'details.html', {'post': post})

def delete(request,del_id):
    post = get_object_or_404(Blog, id=del_id)
    post.delete()
    return redirect('home')

def edit(request, edit_id):
    obj = get_object_or_404(Blog, id=edit_id)
    if request.method == "POST":
        title = request.POST.get('title')
        des = request.POST.get('des')
        image = request.FILES.get('pic')
        if image:
            file_path = f"media/images/{image.name}"
            default_storage.save(file_path, ContentFile(image.read()))
        obj.title = title
        obj.description = des
        obj.image = image
        obj.save()
        messages.success(request, "Details Updated Successfully")
        return redirect("home")
    return render(request, 'edit.html', {'obj': obj})

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'courses':Course.objects.all()
    }
    return render(request, "index.html", context)


# Create course form
def create_course(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Course.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        create(request)
        return redirect('/')

# Delete course
def delete_page(request, number):
    context={
        'course':Course.objects.get(id=number)
    }
    return render(request, "delete.html", context)

def delete_course(request):
    delete(request)
    return redirect('/')

def comment(request,number):
    context={
        'course':Course.objects.get(id=number),
        'comments':Comment.objects.filter(course=number)
    }
    return render(request, "comment.html", context)

def add_comment(request):
    this_course=create_comment(request)
    return redirect('add_comment', number=this_course.id)
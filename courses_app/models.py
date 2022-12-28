from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) <= 5:
            errors["name"] = "The name should be more than 5 characters."
        if len(postData['description']) <= 15:
            errors["description"] = "Description must be more than 15 characters."
        return errors
class Description(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.OneToOneField(Description,on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()
    
class Comment(models.Model):
    content=models.TextField()
    course=models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def create(request):
    des=Description.objects.create(content=request.POST['description'])
    Course.objects.create(name=request.POST['name'], description=des)

    
def delete(request):
    if request.POST['yes_no']=="yes":
        Course.objects.get(id=request.POST['course_id']).delete()


def create_comment(request):
    this_course=Course.objects.get(id=request.POST['course_id'])
    Comment.objects.create(content=request.POST['comment'], course=this_course)
    return this_course

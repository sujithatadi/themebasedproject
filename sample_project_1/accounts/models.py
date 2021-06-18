from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user= models.ForeignKey(User,null=True,on_delete=models.CASCADE)
   
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200)
    section=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    pro_pic=models.ImageField(default='profile1.png')
    date_created=models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.name




class Post(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=5000)
   # image=models.ImageField(upload_to='static/images/company_images/',null=True)
    pub_date = models.DateTimeField('date published')
    likes=models.ManyToManyField(User,related_name='blog_post')
   # tags=models.ManyToManyField(Tag)
    def total_like(self):
       return self.likes.count()
    def __str__(self):
        return self.title




class Student_post(models.Model):
    student=models.ForeignKey(Student,null=True,on_delete=models.SET_NULL)
    post=models.ForeignKey(Post,null=True,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
   
class Comment(models.Model):
    post= models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)
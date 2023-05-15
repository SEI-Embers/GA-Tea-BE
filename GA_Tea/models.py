from django.db import models

class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField()
    confirm_password = models.CharField()
    github = models.CharField(max_length=250)
    bio = models.TextField()
    linkedin = models.CharField(max_length=250)
    profile_pic = models.ImageField(required = false)




class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=128)
    body = models.TextField()
    tags = models.CharField(max_length=128)
    likes = models.IntegerField()
    pic = models.ImageField(required = false)
    skills_strong = models.CharField(max_length=500)
    skills_weak = models.CharField(max_length=500)
    timeline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")





class Comment(models.Model):
    author = models.CharField(max_length=128)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comments")


class Reply(models.Model):
    author = models.CharField(max_length=30)
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = "replies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "replies")

JOB_STATUS=[
    ('Applied'), 
    ('Interviewed'), 
    ('Accepted'), 
    ('Rejected'),
    ('Interested'),
]
class Career(models.Model):
    company_name = models.CharField(max_length=500)
    status = models.CharField(Choices=JOB_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "careers")


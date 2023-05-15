from django.contrib.postgres.fields import ArrayField
from PIL import Image
from django.db import models
from django.utils import timezone

SKILL_LIST = [
    ('HTML', 'HyperText Markup Language'),
    ('CSS', 'Cascading Style Sheets'),
    ('JS', 'JavaScript'),
    ('React', 'React'),
    ('Next.js', 'Next.js'),
    ('Mongo', 'Mongo'),
    ('Express', 'Express'),
    ('Postgres', 'PostgreSQL'),
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Node', 'Node.js'),
    ('REST', 'REpresentational State Transfer'),
    ('Web APIs', 'Web APIs'),
    ('Git', 'Git'),
    ('Data Structures and Algorithms', 'Data Structures and Algorithms'),
]

class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField()
    confirm_password = models.CharField()
    bio = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    skills_strong = ArrayField(models.CharField(max_length=200), blank=True, choices=SKILL_LIST, null=True)
    skills_weak = ArrayField(models.CharField(max_length=200), blank=True, choices=SKILL_LIST, null=True)
    profile_pic = models.ImageField(default='https://imgur.com/a/2L57GM9')

    def __str__(self):
        return f'{self.username}'
    

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=128)
    body = models.TextField()
    tags = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    likes = models.IntegerField()
    pic = models.ImageField(blank=True)
    skills_req = ArrayField(models.CharField(max_length=200), blank=True, choices=SKILL_LIST, null=True)
    timeline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")
    
    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comments")
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    
    def __str__(self):
        return f'{self.user}'

class Reply(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "replies")
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = "replies")

    def __str__(self):
        return f'{self.user}'

JOB_STATUS=[
    ('Applied', 'Applied'), 
    ('Interviewed', 'Interviewed'), 
    ('Accepted', 'Accepted'), 
    ('Rejected', 'Rejected'),
    ('Interested', 'Interested'),
]

class Career(models.Model):
    company_name = models.CharField(max_length=500)
    status = models.CharField(choices=JOB_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "careers")

    def __str__(self):
        return f'{self.company_name}'
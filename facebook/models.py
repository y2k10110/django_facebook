from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') #foreignkey는 다른 거에 있는걸 가져올 수 있는거
    #cascade 연결돼있는게 지워질 때 같이 지워지도록 하는 속성. related_name 글의 입장에서는 어떤 댓글이 나와 연결이 되어있는지 알려주는거.
    author = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Page(models.Model):
    master = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

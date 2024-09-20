from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    publish_date = models.DateField()
    image_link = models.URLField(default='')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=2000)
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.body[:100]
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1500)
    tags = models.ManyToManyField(Tag,related_name = 'post')

## post = Post.objects.first()
## post.tags.all() ## related_name = 'tags' это название к post.tags.all() ,
# если этого нет то будет post.tags_set.all()



   
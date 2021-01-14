from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Заголовок')
    body = models.TextField(max_length=1500, verbose_name = 'Тело поста')
    tags = models.ManyToManyField(Tag,related_name = 'post', verbose_name = 'Теги')


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

## post = Post.objects.first()
## post.tags.all() ## related_name = 'tags' это название к post.tags.all() ,
# если этого нет то будет post.tags_set.all()



   
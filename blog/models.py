from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        if self.last_name:
            return self.get_full_name()
        else:
            return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(max_length=350)
    image_name = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=160, unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Account(models.Model):


    fullName = models.CharField(max_length=30)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    plaque = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,max_length=150,editable=False)

    def get_slug(self):
        slug = slugify(self.fullName.replace("ı", "i"))
        unique = slug
        number = 1

        #berke-erdem1 #berke-erdem
        while Account.objects.filter(slug = unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    def __str__(self):
        return self.fullName

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(Account, self).save(*args,**kwargs)

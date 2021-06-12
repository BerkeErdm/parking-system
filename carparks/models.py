from django.db import models
from django.utils.text import slugify

class CarParks (models.Model):
    park_name = models.CharField(max_length=100)
    district_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    open_until = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/carparks')
    phone = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=150,editable=False)


    def get_slug(self):
        slug = slugify(self.parkName.replace("ı", "i"))
        unique = slug
        number = 1

        #berke-erdem1 #berke-erdem
        while CarParks.objects.filter(slug = unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1

        return unique

    def __str__(self):
        return self.parkName

    def save(self,*args,**kwargs):
        self.slug = self.get_slug()
        return super(CarParks, self).save(*args,**kwargs)
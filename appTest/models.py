from django.db import models


# Create your models here.

class People(models.Model):
    email = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField()
    job = models.CharField(max_length=100)
    createDate = models.DateTimeField(auto_now=True)
    url = models.URLField()
    text = models.TextField()
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email

    def datas(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
        }

    def supports(self):
        return {
            "url": self.url,
            "text": self.text
        }

    def create(self):
        return {
            "name": self.first_name,
            "job": self.job,
            "id": self.id,
            "createDate": self.createDate
        }

    def update(self):
        return {
            "name": self.first_name,
            "job": self.job,
            "updateDate": self.createDate
        }

    def patch(self):
        return {
            "name": self.first_name,
            "job": self.job,
            "updateDate": self.createDate
        }


class Resource(models.Model):
    id_user = models.IntegerField(blank=True, default="1")
    name = models.CharField(max_length=150)
    year = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    pantone_value = models.CharField(max_length=100)
    url = models.URLField()
    text = models.TextField()

    def __str__(self):
        return self.name

    def res(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "color": self.color,
            "pantone_value": self.pantone_value,
            "id_user": self.id_user
        }

    def supports(self):
        return {
            "url": self.url,
            "text": self.text,

        }

from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=300)
    user_id = models.IntegerField(default=0)

    # def get_id_by_username(self,username):
    #     user_obj = self.objects.get(name=username)
    #     return user_obj.id

class Image(models.Model):
    image_link = models.CharField(max_length=3000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_images_by_user(self, current_user):
        return current_user.image_set.all()

    def __str__(self):
        return str(User.name)





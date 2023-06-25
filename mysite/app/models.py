from django.db import models



class Register(models.Model):

    name=models.CharField(max_length=150,null=False,blank=False)
    email=models.CharField(max_length=150,null=False,blank=False)
    message=models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models
import  uuid


class project(models.Model):
    title = models.CharField(max_length=250,blank=False,null=False)
    description = models.TextField(max_length=2000,blank=True,null=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.title

from django.db import models
import uuid
# Create your models here.
class Base(models.Model):
 is_active = models.BooleanField(default=True)
 created_date = models.DateTimeField(auto_now=True)
 created_date = models.DateTimeField(auto_now_add=True)
 uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 is_state_available = models.BooleanField(default=True)

 
 class Meta:
  abstract = True
 
class Country(Base):
 name = models.CharField(max_length=100,)
 slug = models.SlugField(unique=True)
 code = models.CharField(max_length=10, unique=True)
 flag = models.ImageField(upload_to='flag')

 def __str__(self):
  return self.name
 
class State(Base):
 Country = models.ForeignKey(to=Country, on_delete=models.CASCADE, default=1)
 s_name = models.CharField(max_length=100)
 slug = models.SlugField(unique=True)
 language = models.CharField(max_length=200)
 population = models.IntegerField()

 def __str__(self):
  return self.name
 
class City(Base):
 Country = models.ForeignKey(to=Country, on_delete=models.CASCADE, default=1)
 State = models.ForeignKey(to=State, on_delete=models.SET_NULL, null=True)
 name = models.CharField(max_length=100)
 slug = models.SlugField(unique=True)
 
 def __str__(self):
  return self.name



from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# The following are model classes for the NOTES section
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"


# The following are model classes for the HOMEWORK section
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length = 500)
    title = models.CharField(max_length = 500)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject}, {self.title} -- {self.description}"
    

# The following are model classes for the TO-DO section
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todo"
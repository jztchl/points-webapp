from django.contrib.auth.models import User
from django.db import models

class App(models.Model):
    """
    Represents an Android app that can be added by the admin. 
    Users can earn points by completing tasks related to these apps.
    """
    name = models.CharField(max_length=255)
    app_link = models.URLField(max_length=200, blank=True, null=True)
    app_icon = models.ImageField(upload_to='app_icon/', blank=True, null=True)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    Extends the default Django User model with additional information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class UserTask(models.Model):
    """
    Represents a task that a user has completed related to an app.
    The user uploads a screenshot to confirm task completion.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    points = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"

    def save(self, *args, **kwargs):
        # Automatically update the user's total points when the task is completed
        if self.completed:
            self.user.userprofile.total_points += self.points
            self.user.userprofile.save()
        super().save(*args, **kwargs)

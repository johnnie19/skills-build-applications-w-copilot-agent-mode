from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    class Meta:
        abstract = True

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)
    class Meta:
        abstract = True

class Activity(models.Model):
    user = models.EmbeddedField(model_container=User)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    class Meta:
        abstract = True

class Leaderboard(models.Model):
    user = models.EmbeddedField(model_container=User)
    score = models.IntegerField()
    class Meta:
        abstract = True

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    class Meta:
        abstract = True

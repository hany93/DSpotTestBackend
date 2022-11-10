from django.db import models
from model_utils import Choices


class Profile(models.Model):
    statuses = Choices(
        (0, "Developing something amazing"),
        (1, "This could be interesting...."),
        (2, "Man, life is so good"),
        (3, "There is nothing quite like a good friend"),
        (4, "Take a look around you, everything is awesome"),
        (5, "What is the point of all of this"),
        (6, "At Work"),
        (7, "Hangout out by the pool"),
        (8, "At NG Conf!"),
        (9, "Designing beatiful things")
    )
    #todo Profile Image
    photo = models.ImageField(blank=True, null=True)
    #todo Profile Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    bio = models.CharField(max_length=300)
    #todo Profile Status
    status = models.IntegerField(choices=statuses, default=0)
    available = models.BooleanField(default=False)
    #todo Profile Friends
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class ProfilePhoto(models.Model):
    #todo Profile Relationship
    profile = models.ForeignKey(Profile, related_name='profilephotos', on_delete=models.CASCADE)
    #todo Photos List
    photo = models.ImageField()

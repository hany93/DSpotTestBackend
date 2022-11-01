from django.db import models
from model_utils import Choices


class Profile(models.Model):
    statuses = Choices(
        (0, "Developing something amazing"),
        (1, "This could be interesting...."),
        (2, "Man, life is so good"),
        (3, "There is nothing quite like a good friend"),
        (4, "Take a look around you, everything is awesome"),
        (5, "What is the point of all of this")
    )
    photo = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    bio = models.CharField(max_length=300)
    status = models.IntegerField(choices=statuses, default=0)
    available = models.BooleanField(default=False)

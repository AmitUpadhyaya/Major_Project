from django.db import models
class Restaurants(models.Model):
    verbose_name = "Restaurant"
    image = models.ImageField(upload_to='images/', null=True)
    name = models.CharField(max_length=50, unique=False)
    cuisine = models.CharField(max_length=50, unique=False)
    rating = models.IntegerField()



    class Meta:  # In order to change the model name in the admin portal
        verbose_name = "Fast Food Restaurant"

    def __str__(self):
        return self.name
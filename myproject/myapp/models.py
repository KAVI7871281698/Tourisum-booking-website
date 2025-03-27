from django.db import models

# Create your models here.
class register_page(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

class package(models.Model):
    package_name = models.CharField(max_length=50)
    package_price = models.FloatField()
    package_description = models.TextField()
    place_name = models.CharField(max_length=50)
    package_image = models.ImageField(upload_to='uploads/')

class booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    book_now = models.ForeignKey(package, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    journey_date = models.DateField()
    total_persons = models.IntegerField()
    pickup_location = models.CharField(max_length=50)
    pickup_time = models.TimeField()
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)

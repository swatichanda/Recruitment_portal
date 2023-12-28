from django.db import models

# Create your models here.
class Job(models.Model):
    JOB_TYPES = (
        ('SE', 'Software Engineer'),
        ('PM', 'Product Manager'),
        ('DS', 'Data Scientist'),
        # Add more job types here
    )

    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=2, choices=JOB_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # user = models.OneToOneField('auth.User')
    biography = models.TextField()
    # image = models.ImageField(upload_to='profile-images/', blank=True)
    email = models.EmailField(("email"), max_length=254)
    # website = models.URLField(blank=True)
    phone_number = models.IntegerField(null=False)
    address = models.CharField(max_length=500, null=False)
    city = models.CharField(max_length=30, default='')
    state = models.CharField(max_length=30,default='', help_text="Enter the State name")
    country = models.CharField(max_length=40, default="")
    zipcode = models.CharField(max_length=6, default="",help_text="Enter Zip code of Address")

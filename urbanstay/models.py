from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Flat(models.Model):
    BHK_CHOICES = [
        (1, '1 BHK'),
        (2, '2 BHK'),
        (3, '3 BHK'),
        (4, '4 BHK'),
        (5, '5 BHK or more'),
    ]

    FURNISHING_CHOICES = [
        ('unfurnished', 'Unfurnished'),
        ('semi-furnished', 'Semi-Furnished'),
        ('fully-furnished', 'Fully Furnished'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    bhk = models.PositiveSmallIntegerField(choices=BHK_CHOICES)
    bathrooms = models.PositiveSmallIntegerField(default=1)
    furnishing = models.CharField(max_length=20, choices=FURNISHING_CHOICES, default='unfurnished')
    area_sqft = models.PositiveIntegerField(help_text="Total area in square feet")
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_from = models.DateField()
    is_available = models.BooleanField(default=True)

    # Location details
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    # Amenities
    parking = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    power_backup = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=True)

    # Media
    image = models.ImageField(upload_to='flat_images/', blank=True, null=True)

    # Ownership
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    listed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-listed_on']

    def __str__(self):
        return f"{self.title} - {self.city}, {self.state}"

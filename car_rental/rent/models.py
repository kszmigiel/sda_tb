from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class BaseModel(models.Model):
    """Base model."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""

        abstract = True


class Car(BaseModel):
    """Car model."""

    brand = models.CharField(max_length=64, null=False)
    model = models.CharField(max_length=64, null=False)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2010), MaxValueValidator(2023)], null=False)
    deposit = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)

    def __str__(self):
        """Return name of car."""
        return self.brand + " " + self.model + " " + str(self.year)


class Client(BaseModel):
    """Client model."""

    name = models.CharField(max_length=64, null=False)
    surname = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=False)
    phone = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)

    def __str__(self):
        """Return name of client."""
        return self.name + " " + self.surname


class Rental(BaseModel):
    """Rental model."""

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals', null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rentals', null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)

    def __str__(self):
        """Return name of rental."""
        return str(self.car) + " " + str(self.client) + " " + str(self.start_date) + " " + str(self.end_date)

    def save(self, *args, **kwargs):
        """Save method."""

        if not self.pk:
            self.price = self.car.price * (self.end_date - self.start_date).days

        super(Rental, self).save(*args, **kwargs)

from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()

    def __str__(self):
        return f"{self.first_name} on {self.reservation_date} at {self.reservation_slot}"

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title

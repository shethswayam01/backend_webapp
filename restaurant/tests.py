from django.test import TestCase
from .models import Booking, Menu
from datetime import date, time

class BookingTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            first_name="TestUser",
            reservation_date=date.today(),
            reservation_slot=time(hour=18, minute=0)
        )
        self.assertEqual(booking.first_name, "TestUser")

class MenuTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(
            title="Pizza",
            price=12.99,
            inventory=10
        )
        self.assertEqual(item.title, "Pizza")

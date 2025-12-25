from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# Booking API views
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Always start from fresh queryset
        qs = Booking.objects.all()
        date = self.request.query_params.get('date')
        if date:
            qs = qs.filter(reservation_date=date)
        return qs

    def perform_create(self, serializer):
        date = serializer.validated_data['reservation_date']
        slot = serializer.validated_data['reservation_slot']
        if Booking.objects.filter(reservation_date=date, reservation_slot=slot).exists():
            raise serializers.ValidationError("Slot already booked")
        serializer.save()

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Menu API views
class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

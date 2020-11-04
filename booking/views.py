from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from order.models import OrderItem
from django.core.exceptions import PermissionDenied


def register_booking(request, pk):
    order_item = OrderItem.objects.get(pk=pk)
    if request.user.is_admin:
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.buyer = request.user
                booking.order = order_item
                booking.save()
                return redirect('my_bookings')
        else:
            form = BookingForm()
        context = {
            'form': form
        }
        return render(request, 'register_booking.html', context)
    elif request.user.is_shopper:
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.buyer = request.user
            booking.save()
            return redirect('my_bookings')
        else:
            form = BookingForm()
        context = {
            'form': form
        }
        return render(request, 'register_booking.html', context)
    else:
        raise PermissionDenied


def all_bookings(request):
    bookings = Booking.objects.all().order_by('-date_created').select_related('user')
    context = {
        'bookings': bookings
    }
    return render(request, 'all_bookings.html', context)


def view_booking(request, pk):
    if request.user.is_shipper is True:
        booking = get_object_or_404(Booking, pk=pk)
        context = {
            'booking': booking
        }
        return render(request, 'view_booking.html', context)
    else:
        raise PermissionDenied


def booking_picked(request, pk):
    if request.user.is_shipper is True:
        picked_booking = get_object_or_404(Booking, pk=pk)
        picked_booking.is_picked = True
        picked_booking.shipper = request.user
        picked_booking.save()
        order_item = OrderItem.objects.get(pk=picked_booking.pk)
        order_item.picked = True
        order_item.save()
        return redirect('my_booking')
    else:
        raise PermissionDenied


def booking_delivered(request, pk):
    if request.user.is_shipper is True:
        picked_booking = get_object_or_404(Booking, pk=pk)
        picked_booking.is_delivered = True
        picked_booking.shipper = request.user
        picked_booking.save()
        order_item = OrderItem.objects.get(pk=picked_booking.pk)
        order_item.delivered = True
        order_item.save()
        return redirect('my_booking')
    else:
        raise PermissionDenied


def my_bookings(request):
    bookings = Booking.objects.filter(shipper=request.user).order_by('-date').select_related('shipper')
    context = {
        'bookings': bookings
    }
    return render(request, 'my_bookings.html', context)


def all_delivered_booking(request):
    bookings = Booking.objects.filter(is_delivered=True, shipper=request.user).order_by('-date_created')\
               .select_related('shipper')
    context = {
        'bookings': bookings
    }
    return render(request, 'delivered_bookings.html', context)


def all_picked_booking(request):
    bookings = Booking.objects.filter(is_picked=True, shipper=request.user).order_by('-date_created')\
               .select_related('shipper')
    context = {
        'bookings': bookings
    }
    return render(request, 'delivered_bookings.html', context)

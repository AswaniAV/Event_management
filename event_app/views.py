from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .models import Event, feedback
from .forms import bookingform, feedbackform
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request, 'contact.html')    

def about(request):
    return render(request, 'about.html') 

def events(request):
    event = Event.objects.all()
    context = {
        'event': event
    }
    return render(request, 'events.html', context)

def booking(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        form = bookingform(request.POST)
        if form.is_valid():
            form.instance.event = event
            form.save()
            messages.success(request, 'Successfully booked')
            # Redirect with the event_id parameter
            return redirect('booking', event_id=event_id)
        else:
            # If form is not valid, handle the error
            messages.error(request, 'Form is not valid')
    else:
        form = bookingform()
    
    dic_event = {'form': form, 'event': event}
    return render(request, 'booking.html', dic_event)

def contact_view(request):
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('contact') 
    else:
        form = feedbackform()
    
    return render(request, 'contact.html', {'form': form})



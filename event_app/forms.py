from django import forms
from .models import Booking
from .models import feedback

class bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'book_date': forms.DateInput(
                attrs={'type': 'date'}
                ),    
        }
        labels ={
            'customer_name' : 'CustomerName',
            'customer_phone' : 'CustomerPhone',
            'name' : 'SelectEventName',
            'book_date' : 'BookingDate',
            'book_on' : 'BookingOn'   
        }

    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('name')
        book_date = cleaned_data.get('book_date')
        if Booking.objects.filter(name=event, book_date=book_date).exists():
            raise forms.ValidationError('This event is already booked for the selected date')
        return cleaned_data

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['customer_name', 'email', 'subject', 'message']
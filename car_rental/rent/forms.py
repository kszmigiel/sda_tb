from django.forms import Form, DateField, ValidationError, ModelChoiceField
from .models import Rental, Car, Client


class RentalForm(Form):
    car = ModelChoiceField(queryset=Car.objects)
    client = ModelChoiceField(queryset=Client.objects)
    start_date = DateField()
    end_date = DateField()

    def clean(self):
        data = self.cleaned_data
        if data['start_date'] > data['end_date']:
            raise ValidationError('Start date must be before end date')
        return data

    def save(self):
        data = self.cleaned_data
        rental = Rental.objects.create(
            car=data['car'],
            client=data['client'],
            start_date=data['start_date'],
            end_date=data['end_date'],
        )
        return rental
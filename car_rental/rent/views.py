from .models import Car, Client, Rental
from django.views.generic import FormView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RentalForm


class RentalListView(ListView):
    template_name = 'rentals_list.html'
    model = Rental


class RentalDetailView(DetailView):
    template_name = 'rental.html'
    model = Rental

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = Car.objects.get(rentals=self.object)
        context['client'] = Client.objects.get(rentals=self.object)
        return context


class RentalCreateView(LoginRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = RentalForm
    success_url = '/rent/rentals/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RentalUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Rental
    fields = '__all__'
    success_url = '/rent/rentals/'


class RentalDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Rental
    success_url = '/rent/rentals/'
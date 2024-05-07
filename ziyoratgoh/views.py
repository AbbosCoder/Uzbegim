from django.views.generic import ListView,DetailView,TemplateView
from .models import Ziyoratgoh,Region,Carusel
from django.views import View
from xabar.forms import XabarForm
from django.shortcuts import render, redirect
from xabar.utils import send_telegram_message 

class ZiyoratgohHomeView(ListView):
    model = Ziyoratgoh
    template_name = 'ziyoratgoh_list.html'
    context_object_name = 'ziyoratgohlar'

    def get_queryset(self):
        # Fetch all Ziyoratgoh instances
        return Ziyoratgoh.objects.all()
    
class ZiyoratgohDetailView(DetailView):
    model = Ziyoratgoh
    template_name = 'ziyoratgoh_detail.html'
    context_object_name = 'ziyoratgoh'


class HomePageView(View):
    template_name = 'home.html'

    
    def get(self, request, *args, **kwargs):
        # Get the latest 3 Ziyoratgoh instances
        latest_ziyoratgohlar = Ziyoratgoh.objects.order_by('-id')[:3]

        # Get all unique viloyatlar (regions)
        viloyatlar = Region.objects.all()
        carusel_items = Carusel.objects.all()[:5]
        # Group Ziyoratgoh instances by viloyat (region)
        viloyat_ziyoratgohlar = {}
        for viloyat in viloyatlar:
            viloyat_ziyoratgohlar[viloyat.name] = Ziyoratgoh.objects.filter(viloyat=viloyat)

        context = {
            'latest_ziyoratgohlar': latest_ziyoratgohlar,
            'viloyat_ziyoratgohlar': viloyat_ziyoratgohlar,
            'carusel_items': carusel_items,
        }

        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = XabarForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = XabarForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('contact')  # Redirect to the same page or another success page
        return render(request, self.template_name, {'form': form})



class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        form = XabarForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = XabarForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            # Compose a message to send to Telegram
            xabar = form.instance
            telegram_message = f"<b>{xabar.name}</b>dan yangi xabar.\nEmail: {xabar.email}\nPhone: <code>{xabar.phone_number}</code>\nMessage: \n  <b><i>{xabar.message}</i></b>"

            # Send the message to Telegram
            status, response = send_telegram_message(telegram_message)

            if status == 200:
                print("Adminga xabar yuborildi")
            else:
                print("Adminga xabar yuborishda xatolik", response)

            return redirect('contact')  # Redirect after submission
        return render(request, self.template_name, {'form': form})

from django.shortcuts import render
from .models import Ziyoratgoh
from .forms import ZiyoratgohSearchForm

def ziyoratgoh_list_view(request):
    form = ZiyoratgohSearchForm(request.GET)  # Bind the form with GET parameters
    
    queryset = Ziyoratgoh.objects.all()  # Start with all instances

    if form.is_valid():
        # Filter by title if provided
        title = form.cleaned_data['title']
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        # Filter by viloyat if selected
        viloyat = form.cleaned_data['viloyat']
        if viloyat:
            queryset = queryset.filter(viloyat=viloyat)
    
    context = {
        'form': form,
        'ziyoratgohlar': queryset,
    }

    return render(request, 'ziyoratgoh_list.html', context)



class AboutUsView(TemplateView):
    template_name = 'about.html' 
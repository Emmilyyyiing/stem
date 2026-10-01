from django.shortcuts import get_object_or_404, render, redirect
from .forms import ContactForm, ApplicationForm
from .models import Job, Service, Testimonial
from django.contrib.auth.views import LoginView, LogoutView


def home(request):
    return render(request, 'HRservices/home.html')

def about(request):
    return render(request, 'HRservices/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('contact')  
    else:
        form = ContactForm()
    return render(request, 'HRservices/contact.html', {'form': form})

def apply_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job  # 👈 Assign job before saving
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()

    return render(request, 'HRservices/job_detail.html', {'form': form, 'job': job})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'HRservices/job_list.html', {'jobs': jobs})

class AdminLoginView(LoginView):
    template_name = 'HRservices/login.html'

class AdminLogoutView(LogoutView):
    pass


def home(request):
    testimonials = Testimonial.objects.order_by('-date')[:6]  # latest 6
    return render(request, 'HRservices/home.html', {'testimonials': testimonials})


def services_page(request):
    services = Service.objects.all()
    return render(request, 'HRservices/services.html', {
        'services': services
    })

from django.contrib.auth.views import LoginView, LogoutView
from .forms import StyledLoginForm


class AdminLoginView(LoginView):
    template_name = 'HRservices/login.html'
    authentication_form = StyledLoginForm


class AdminLogoutView(LogoutView):
    pass
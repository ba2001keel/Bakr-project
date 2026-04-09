from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def portfolio_view(request):
    return render(request, 'portfolio/portfolio.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

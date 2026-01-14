from django.shortcuts import render

def home(request):
    context = {
        'site_name': 'Django Portfolio',
        'page_title': 'Home'
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'site_name': 'Django Portfolio',
        'page_title': 'About'
    }
    return render(request, 'main/about.html', context)

def projects(request):
    context = {
        'site_name': 'Django Portfolio',
        'page_title': 'Projects'
    }
    return render(request, 'main/projects.html', context)

def contact(request):
    context = {
        'site_name': 'Django Portfolio',
        'page_title': 'Contact'
    }
    return render(request, 'main/contact.html', context)

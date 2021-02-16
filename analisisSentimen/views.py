from django.shortcuts import render

def dashboard(request):
    judul = ["Analisis Sentimen", "Twitter", "Covid-19"]

    konteks = {
        'title' : judul
    }
    return render(request, 'dashboard.html', konteks)

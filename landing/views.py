from django.shortcuts import render
from django.views import View
from .models import Faq, Subject, Road
class Land(View):
    def get(self, request, *args, **kwargs):
        faq = Faq.objects.all()
        subjects = Subject.objects.filter(home=True)
        road = Road.objects.all()
        context = {
            "faq": faq,
            "sub": subjects,
            "road": road,
        } 
        return render(request, "landing/land.html", context)
    
class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/about.html")
    
class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/contact.html")

class Research(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/research.html")

class Apply(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/apply.html")
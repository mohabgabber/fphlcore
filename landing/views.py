from django.shortcuts import render
from django.views import View

class Land(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/land.html")
    
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
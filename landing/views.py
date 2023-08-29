from django.shortcuts import render
from django.views import View
from .models import Faq, Subject, Road, Team
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
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
        team = Team.objects.all()
        context = {"team": team,}
        return render(request, "landing/about.html", context)
    
class Contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/contact.html")
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        temp = render_to_string("landing/contact-us-submission.html", {'name': name, 'email': email, 'subject': subject, 'message': message,})
        send_mail("New Contact Us Submission", temp, "forensicphonetician@gmail.com",
                      ['forensicphonetician@gmail.com'], fail_silently=True)
        messages.success(request, "تم ارسال رسالتك بنجاح")
        return render(request, "landing/contact.html")

class Research(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/research.html")

class Apply(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/apply.html")

class Subjects(View):
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        context = {"sub": subjects,}
        return render(request, "landing/subjects.html", context)
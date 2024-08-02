from django.shortcuts import redirect, render
from django.views import View
from .models import Faq, Subject, Road, Team, Research, Event
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import CaptchaForm


class Land(View):
    def get(self, request, *args, **kwargs):
        faq = Faq.objects.all()
        subjects = Subject.objects.filter(home=True)
        road = Road.objects.all()
        try:
            event = Event.objects.all().order_by('-adddate')[0]
        except:
            event = False
        context = {
            "faq": faq,
            "sub": subjects,
            "road": road,
            "event": event,
        }
        return render(request, "landing/land.html", context)


class About(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.all()
        context = {"team": team, }
        return render(request, "landing/about.html", context)


# class Contact(View):
#     def get(self, request, *args, **kwargs):
#         captcha = CaptchaForm()
#         context = {"captcha": captcha, }
#         return render(request, "landing/contact.html", context)

#     def post(self, request, *args, **kwargs):
#         captcha = CaptchaForm(request.POST)
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#         if captcha.is_valid():

#             temp = render_to_string("landing/contact-us-submission.html", {
#                                     'name': name, 'email': email, 'subject': subject, 'message': message, })
#             send_mail("New Contact Us Submission", temp, "forensicphonetician@gmail.com",
#                       ['forensicphonetician@gmail.com'], fail_silently=True)
#             messages.success(request, "تم ارسال رسالتك بنجاح")
#         else:
#             captcha = CaptchaForm()
#             messages.warning(request, "Captcha Is Invalid")
#         context = {"captcha": captcha, }
#         return render(request, "landing/contact.html", context)


class ResearchView(View):
    def get(self, request, *args, **kwargs):
        searches = Research.objects.all()
        context = {"research": searches, }
        return render(request, "landing/research.html", context)


class ResearchDetail(View):
    def get(self, request, pk, *args, **kwargs):
        if Research.objects.filter(id=pk).exists():
            r = Research.objects.get(id=pk)
            context = {"r": r, }
        else:
            return redirect("home")
        return render(request, "landing/research-detail.html", context)


class Apply(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/apply.html")


class Study(View):
    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.all()
        context = {"sub": subjects, }
        return render(request, "landing/study.html", context)


class Events(View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all().order_by("-adddate")
        context = {
            "events": events,
        }
        return render(request, "landing/events.html", context)


class EventDetail(View):
    def get(self, request, id, *args, **kwargs):
        event = Event.objects.get(id=id)
        context = {
            "event": event,
        }
        return render(request, "landing/event-detail.html", context)

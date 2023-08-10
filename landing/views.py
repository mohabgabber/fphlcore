from django.shortcuts import render
from django.views import View

class Land(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing/land.html")
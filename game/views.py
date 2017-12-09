from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        try:
            del request.session['name']
            del request.session['id']
            del request.session['status']
            return render(request, template_name="index.html")
        except:
            return render(request, template_name="index.html")

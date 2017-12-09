from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")

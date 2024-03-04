from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        img_file = request.FILES["image"]
        print(img_file)
        return HttpResponseRedirect("/profiles")
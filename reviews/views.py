from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })  

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })  

    
def review(request):
    if request.method == "POST":
        #for updating a specific data entry
        # existing_model = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=existing_model)
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'],
            #                 review_text=form.cleaned_data['review_text'],
            #                 rating=form.cleaned_data['rating']
            #                 )
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    #     entered_username = request.POST['user']
    #     if entered_username == "" and len(entered_username) >= 100:
    #         return render(request, "reviews/review.html", {
    #             "has_error": True
    #         })
    #     print("username: ", entered_username)
    else: 
        form = ReviewForm()
    
    return render(request, "reviews/review.html", {
        # "has_error": False
        "form": form
    })    

    

def thank_you(request):
    return render(request, "reviews/thank_you.html")
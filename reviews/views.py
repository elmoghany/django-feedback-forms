from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
#UpdateView, DeleteView
# Create your views here.

class AddFavoriteView(View):
    def post(request, self):
        review_id = request.POST['review_id']
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
    
    

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    #labels not supported here
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    #saved automatically
    
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })  

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })  

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    #to pass variables => use get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'this works'
        return context
    # def get(self, request):
    #     return render(request, "reviews/thank_you.html")

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review # object_list
    context_object_name = "reviews"

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context['is_favorite'] = favorite_id == str(loaded_review.id)
        return context


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk=review_id)
#         context['review'] = selected_review
#         return context
#     # def get_queryset(self):
#     #     base_query = super().get_queryset()
#     #     data = base_query.filter(rating__gt=4)
#     #     return data




# def review(request):
#     if request.method == "POST":
#         #for updating a specific data entry
#         # existing_model = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_model)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'],
#             #                 review_text=form.cleaned_data['review_text'],
#             #                 rating=form.cleaned_data['rating']
#             #                 )
#             # review.save()
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#     #     entered_username = request.POST['user']
#     #     if entered_username == "" and len(entered_username) >= 100:
#     #         return render(request, "reviews/review.html", {
#     #             "has_error": True
#     #         })
#     #     print("username: ", entered_username)
#     else: 
#         form = ReviewForm()
    
#     return render(request, "reviews/review.html", {
#         # "has_error": False
#         "form": form
#     })    

    

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")
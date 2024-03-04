from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     #models.Charfield => create text field in the model & database
#     #forms.Charfield  => no impact on db but will later create a text input field in the form which we are going to render
#     user_name = forms.CharField(label="Your Name", required=True, max_length=100, error_messages={
#         "required": "your name must not be empty",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="your ratings", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            'user_name': "your name",
            "review_text": "your feedback",
            "rating": "your rating"
        }
        error_messages = {
            "user_name": {
                "required": "your name must not be empty",
                "max_length": "please use a shorter name"
            }
        }
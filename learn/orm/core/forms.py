from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    

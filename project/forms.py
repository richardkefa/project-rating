from django import forms
from .models import Ratings,RATE_CHOICES

class RatingsForm(forms.ModelForm):
  design = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
  usability = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
  content = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)
  comment = forms.CharField(max_length=300,widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False)

  class Meta:
    model = Ratings
    fields = ['design','usability','content','comment']
    
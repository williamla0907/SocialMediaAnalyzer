from django import forms

class keywordForm(forms.Form):
    keyword = forms.CharField(label='keyword', max_length=140)

class locationForm(forms.Form):
    location = forms.CharField(label='location', max_length=100)
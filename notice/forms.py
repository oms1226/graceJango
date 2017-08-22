from django import forms

class NoticeSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')


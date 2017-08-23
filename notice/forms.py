from django import forms
from django.forms import inlineformset_factory

from notice.models import Notice


class NoticeSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class NoticeAddContentForm(forms.Form):
    class Meta:
        model = Notice
        fields = ['image']
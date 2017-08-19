from sermon.models import SermonType, Content
from django.forms.models import inlineformset_factory

ContentInlineFormSet = inlineformset_factory(SermonType, Content,
    fields = ['title', 'description'],
    extra = 2)


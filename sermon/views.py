# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.views.generic import ListView, DetailView
from sermon.models import SermonType, Content

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.
class SermonTypeLV(ListView):
    model = SermonType

class SermonTypeDV(DetailView):
    model = SermonType

class ContentDV(DetailView):
    model = Content

#--- Add/Change/Update/Delete for Content
class ContentCreateView(LoginRequiredMixin, CreateView):
    model = Content
    fields = ['sermon_type', 'title', 'image', 'description']
    success_url = reverse_lazy('content:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ContentCreateView, self).form_valid(form)

class ContentChangeLV(LoginRequiredMixin, ListView):
    template_name = 'content/content_change_list.html'

    def get_queryset(self):
        return Content.objects.filter(owner=self.request.user)

class ContentUpdateView(LoginRequiredMixin, UpdateView) :
    model = Content
    fields = ['sermon_type', 'title', 'image', 'description']
    success_url = reverse_lazy('content:index')

class ContentDeleteView(LoginRequiredMixin, DeleteView) :
    model = Content
    success_url = reverse_lazy('content:index')

#--- Add/Change/Update/Delete for SermonType
#--- Change/Delete for SermonType
class SermonTypeChangeLV(LoginRequiredMixin, ListView):
    template_name = 'content/sermon_type_change_list.html'

    def get_queryset(self):
        return SermonType.objects.filter(owner=self.request.user)

class SermonTypeDeleteView(LoginRequiredMixin, DeleteView) :
    model = SermonType
    success_url = reverse_lazy('content:index')


#--- InlineFormSet View
#--- Add/Update for SermonType
from django.shortcuts import redirect
from sermon.forms import ContentInlineFormSet

class SermonTypeCV(LoginRequiredMixin, CreateView):
    model = SermonType
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(SermonTypeCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ContentInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = ContentInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for contentform in formset:
            contentform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('content:sermon_type_detail', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class SermonTypeUV(LoginRequiredMixin, UpdateView):
    model = SermonType
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super(SermonTypeUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ContentInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['formset'] = ContentInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

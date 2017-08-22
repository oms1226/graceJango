# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from notice.models import Notice
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from notice.forms import NoticeSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

#--- TemplateView
class TagTV(TemplateView) :
    template_name = 'tagging/tagging_cloud.html'

#--- ListView
class NoticeLV(ListView) :
    model = Notice
    template_name = 'notice/notice_all.html'
    context_object_name = 'notices'
    paginate_by = 2

class NoticeTOL(TaggedObjectList) :
    model = Notice
    template_name = 'tagging/tagging_notice_list.html'

#--- DetailView
class NoticeDV(DetailView) :
    model = Notice

#--- ArchiveView
class NoticeAV(ArchiveIndexView) :
    model = Notice
    date_field = 'modify_date'

class NoticeYAV(YearArchiveView) :
    model = Notice
    date_field = 'modify_date'
    make_object_list = True

class NoticeMAV(MonthArchiveView) :
    model = Notice
    date_field = 'modify_date'

class NoticeDAV(DayArchiveView) :
    model = Notice
    date_field = 'modify_date'

class NoticeTAV(TodayArchiveView) :
    model = Notice
    date_field = 'modify_date'

#--- FormView
class SearchFormView(FormView):
    form_class = NoticeSearchForm
    template_name = 'notice/notice_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        notice_list = Notice.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = notice_list

        return render(self.request, self.template_name, context)

#--- Bootstrap Search Result
class BstrapSearchLV(ListView) :
    template_name = 'notice/notice_bstrap_search.html'

    def get_queryset(self):
        schWord = '%s' % self.request.GET['search']
        notice_list = Notice.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        self.search_term = schWord
        self.count = notice_list.count()
        return notice_list

    def get_context_data(self, **kwargs):
        context = super(BstrapSearchLV, self).get_context_data(**kwargs)
        context['search_term'] = self.search_term
        context['search_count'] = self.count
        return context

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('notice:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NoticeCreateView, self).form_valid(form)

class NoticeChangeLV(LoginRequiredMixin, ListView):
    template_name = 'notice/notice_change_list.html'

    def get_queryset(self):
        return Notice.objects.filter(owner=self.request.user)

class NoticeUpdateView(LoginRequiredMixin, UpdateView) :
    model = Notice
    fields = ['title', 'slug', 'description', 'content', 'tag']
    success_url = reverse_lazy('notice:index')

class NoticeDeleteView(LoginRequiredMixin, DeleteView) :
    model = Notice
    success_url = reverse_lazy('notice:index')


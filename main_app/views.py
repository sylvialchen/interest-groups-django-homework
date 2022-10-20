from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import School, Chapter
from .forms import EventForm
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    # print(request)
    return render(request, "about.html")


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)
    event_form = EventForm()
    chapters_unvisited = Chapter.objects.exclude(
        id__in=school.can_visit.all().values_list('id'))
    return render(request, 'schools/detail.html', {
        'school': school,
        'event_form': event_form,
        'chapters': chapters_unvisited,
    })


def add_event(request, school_id):
    form = EventForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_event = form.save(commit=False)
        new_event.school_id = school_id
        new_event.save()
    return redirect('detail', school_id=school_id)


def visited_chapter(request, school_id, chapter_id):
    # Note that you can pass a toy's id instead of the whole object
    School.objects.get(id=school_id).can_visit.add(chapter_id)
    return redirect('detail', school_id=school_id)


class SchoolList(ListView):
    model = School


class SchoolCreate(CreateView):
    model = School
    fields = ['name', 'school_name', 'school_state',
              'group_pillars', 'group_social_media', 'contact_emails']
    # success_url = '/schools/'


class SchoolUpdate(UpdateView):
    model = School
  # Let's disallow the renaming of a school by excluding the name field!
    fields = ['name', 'school_name', 'school_state',
              'group_pillars', 'group_social_media', 'contact_emails']


class SchoolDelete(DeleteView):
    model = School
    success_url = '/schools/'


class ChapterCreate(CreateView):
    model = Chapter
    fields = ('name', 'chapter_school', 'city_state',
              'original_founding_date')


class ChapterUpdate(UpdateView):
    model = Chapter
    fields = ('name', 'chapter_school', 'city_state',
              'original_founding_date')


class ChapterDelete(DeleteView):
    model = Chapter
    success_url = '/chapters/'


class ChapterDetail(DetailView):
    model = Chapter
    template_name = 'chapters/detail.html'


class ChapterList(ListView):
    model = Chapter
    template_name = 'chapters/index.html'

from django.urls import path
from . import views
from . views import SchoolList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schools/', SchoolList.as_view(), name='index'),
    path('schools/<int:school_id>/', views.school_detail, name='detail'),
    path('schools/create/', views.SchoolCreate.as_view(), name='school_create'),
    path('schools/<int:pk>/update/',
         views.SchoolUpdate.as_view(), name='school_update'),
    path('schools/<int:pk>/delete/',
         views.SchoolDelete.as_view(), name='school_delete'),
    path('schools/<int:school_id>/add_event/',
         views.add_event, name='add_event'),
    path('chapters/', views.ChapterList.as_view(), name='chapters_index'),
    path('chapters/<int:pk>/', views.ChapterDetail.as_view(), name='chapter_detail'),
    path('chapters/create/', views.ChapterCreate.as_view(), name='chapter_create'),
    path('chapters/<int:pk>/update/',
         views.ChapterUpdate.as_view(), name='chapter_update'),
    path('chapters/<int:pk>/delete/',
         views.ChapterDelete.as_view(), name='chapter_delete'),
    path('schools/<int:school_id>/chapter/<int:chapter_id>/',
         views.visited_chapter, name='visited_chapter')
]

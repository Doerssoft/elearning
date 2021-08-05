from django.urls import path

from . import views

urlpatterns = [
    path('', views.grades, name='grades'),
    path('grade/<int:grade_id>', views.grades_subjects, name='grades_subjects'),
]
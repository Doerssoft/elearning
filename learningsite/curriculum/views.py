from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade,Subject
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def grades(request):
    template_name = 'curriculum/grades.html'
    context = Grade.objects.all()
    return render(request, template_name, {'context': context})

@login_required(login_url='login')
def grades_subjects(request, grade_id):
    template_name = 'curriculum/grade-subject.html'
    grade= Grade.objects.get(id=grade_id)
    subjects= Subject.objects.filter(grade=grade_id)
    return render(request, template_name, {'context': subjects, 'grade':grade})
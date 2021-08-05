from django.db import models
from ckeditor.fields import RichTextField

class Grade(models.Model):
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade


class Subject(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, null=True)
    subject_name = models.CharField(max_length=200)
    syllabus = RichTextField()

    def __str__(self):
        return self.subject_name

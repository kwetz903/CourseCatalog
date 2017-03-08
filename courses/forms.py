from django import forms
from django.forms.widgets import RadioSelect
from django.db import models
#from models import Post
from courses.models import Course			

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title', 'description','instructor','duration', 'art',]
		
		widgets = {
			'duration': RadioSelect(),
			#'description': StyledTextBox(),
			'art': forms.FileInput()
		}				
		
		labels = {
			'title': ('Course Title'),
			'duration': ('Course Duration'),
		}

		help_texts = { 'description': ('</br><div id="helptext">Provide some information about what students will learn.</div>')}
	
		methods = {
			'art' : ('post'),
		}

		enctypes = {
			'art': ('multipart/form-data'),
		}

		
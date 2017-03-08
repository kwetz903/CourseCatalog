from django.http import HttpResponseRedirect 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from courses.models import Course
from courses.forms import CourseForm


class IndexView(generic.ListView):
	template_name = 'courses/index.html'
	model = Course

class DetailView(generic.DetailView):
	model = Course
	template_name = 'courses/detail.html'

class CourseCreate(CreateView):
	form_class = CourseForm
	template_name = 'courses/add.html'
	success_url = reverse_lazy('courses:index')
	
	def get_success_url(self):
		return reverse_lazy('courses:index')

class CourseEdit(UpdateView):
	form_class = CourseForm
	model = Course
	template_name = 'courses/add.html'


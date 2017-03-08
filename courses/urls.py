from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views

app_name = 'courses'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^add/$', views.CourseCreate.as_view(), name='add'),
	url(r'^(?P<pk>[0-9]+)/change/$', views.CourseEdit.as_view(), name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
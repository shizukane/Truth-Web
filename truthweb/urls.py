from audioop import reverse
from importlib.resources import path 
from django.urls import include , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'truthweb'
urlpatterns = [
    re_path('', views.homepage, name= 'homepage'),
    re_path('search/', views.search_projects, name='search_results'),
    re_path('project/(\d+)', views.get_project, name='project_results'),
    # re_path('new_project/$', views.new_project, name='new_project'),
    re_path('accounts/profile/$', views.user_profiles, name='profile'),
    re_path('api/projects/$', views.ProjectList.as_view()),
    re_path('api/profiles/$', views.ProfileList.as_view()),
    reverse('new_project/$', views.new_project, name='new_project')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
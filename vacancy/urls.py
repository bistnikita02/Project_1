from django.urls import path
from vacancy.views import  VacancyDetailView,VacancyCreateView,HomeView,about, home,searchview,applyview
#from.views import PostlistView

urlpatterns = [
   path('',  home, name='home'),
   path('vacancy/',HomeView.as_view(), name='vacancy-home'),
   #path('', PostlistView.as_views(), name='vacancy-home'),
   path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name = 'vacancy-detail'),
   path('vacancy/new/',VacancyCreateView.as_view(), name = 'vacancy-create'),
   path('about/', about, name='vacancy-about'),
   path('search/',searchview.as_view(), name='search'),
   path('apply/<int:pk>/', applyview.as_view(), name = 'apply')
   

]

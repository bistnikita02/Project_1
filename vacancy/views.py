from django.shortcuts import render
from vacancy.models import Vacancy
from django.views.generic import  DetailView,CreateView,ListView
from django.db.models import Value,IntegerField
from vacancy.cosine_similarity import cosine_similarity, vectorize


posts=  [
    {
        'company': 'Nabina',
        'title': 'job 1',
        'content': 'first job content',
        'date_posted': 'august 27, 2023'


    },
    {
        'company': 'sushil',
        'title': 'job 2',
        'content': 'second job content',
        'date_posted': 'august 28, 2023'
    }
        
        
]
"""
Listview: 
    - methods: GET
    Display data in list. 
    <Modelname>.objects.all()
    - No pk
CreateView:
    - methods: POST (to create and save data in database)
                GET (If there is errors in form it will display those data )
    - Create a single data 
    - Form -> model 


DetailView:
    - methods: GET 
    - Display detail of single data.
    - it needs pk to identify data (from url).
    <modelname>.objects.get(pk=<pk from url>)

DeleteView:
    - methods: POST
    - no template required (template may require for users confirmations)

How django class based view read template by default:
    - <appname>/{modelname}_{action}
    for eg:
        for vacancy detailview template name to lookup will be 
        vacancy_detail.html
"""
class HomeView(ListView):
    model = Vacancy
    context_object_name = 'vacancies'
    template_name = 'vacancy/home.html'

    def  get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:            
            try:
                if self.request.user.companyprofile:
                    queryset = queryset.filter(company=self.request.user)
            except:
                pass 

        return queryset
        
class VacancyDetailView(DetailView):
    model = Vacancy

class VacancyCreateView(CreateView):
    model = Vacancy
    fields = ['title','skill','content']

    def form_valid(self,form):
        form.instance.company = self.request.user
        return super().form_valid(form)
    




def about(request):
    return render(request, 'vacancy/about.html',{'title': 'About'})
   
class searchview(ListView):
    model=Vacancy
    template_name='vacancy/search.html' 
    context_object_name='vacancies'

    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.filter(skill__name__icontains=self.request.GET.get('search'))
        return qs

class applyview(DetailView):
    model= Vacancy
    template_name= 'vacancy/apply.html'        


def home(request):
    return render(request, 'vacancy/home2.html',{'title': 'Home'})
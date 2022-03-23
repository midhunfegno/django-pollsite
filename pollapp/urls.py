from django.urls import path
from pollapp import views

app_name = "pollapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('results/<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
]

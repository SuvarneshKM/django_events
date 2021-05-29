from django.urls import path
# from . import views
from .views import HomeView, EventDetailView

urlpatterns = [
   # path('', views.home, name="home"),
   path('', HomeView.as_view(), name="home"),
   path('event/<int:pk>', EventDetailView.as_view(), name="event-detail" ),
]

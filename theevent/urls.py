from django.urls import path
# from . import views
from .views import HomeView, EventDetailView, AddEventView

urlpatterns = [
   # path('', views.home, name="home"),
   path('', HomeView.as_view(), name="home"),
   path('event/<int:pk>', EventDetailView.as_view(), name="event-detail" ),
   path('add_event/', AddEventView.as_view(), name="add_event"),
]

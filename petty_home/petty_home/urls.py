from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from animals.views import HomePageView, AnimalsPageView, AnimalPageView, ContactsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('animals/', AnimalsPageView.as_view()),
    path('animal/<int:pk>/', AnimalPageView.as_view()),
    path('contacts/', ContactsView.as_view())
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
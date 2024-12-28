from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),  # Replace 'feedback_app' with your app name
    path('', RedirectView.as_view(url='/feedback/', permanent=True)),  # Redirect root to feedback/
]


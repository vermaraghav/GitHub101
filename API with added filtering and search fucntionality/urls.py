from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapp.views import TaskViewSet
from restapp import views
from django.conf.urls.static import static
from django.conf import settings
import os

router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register('task',views.TaskViewSet)
#router.register('completed_task',views.CompletedTaskViewSet)
#router.register('due_task',views.DueTaskViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from rest_framework.routers import SimpleRouter,DefaultRouter
from django.urls import path, include
from .views import ShowAllTv
from django.conf.urls.static import static
from django.conf import settings
router = DefaultRouter()
router.register('tv', ShowAllTv)
# router.register('all', ShowAllContent)
urlpatterns = [
    # path('home1/<int:id>',DetailsShowContent.as_view())
    path('content', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
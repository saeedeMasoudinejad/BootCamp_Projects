from django.urls import path
from .views import*
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('user/<str:username>', csrf_exempt(UserViews.as_view())),
    path('my news/<str:username>', csrf_exempt(UserViews.as_view())),
    path('show/', csrf_exempt(NewsViews.as_view())),
    path('show/<int:year>', csrf_exempt(NewsViews.as_view())),
    path('show/<int:year>/<int:month>', csrf_exempt(NewsViews.as_view())),
    path('show/<int:year>/<int:month>/<int:day>', csrf_exempt(NewsViews.as_view())),
    path('update/<str:username>/<int:id_news>', csrf_exempt(NewsViews.as_view())),
    path('delete/<str:username>/<int:id_news>', csrf_exempt(NewsViews.as_view()))
]
from django.conf.urls import url, include
from rest_framework import routers
from movierater.api import views
from movierater.api.views import CustomObtainAuthToken
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'ratings', views.RatingViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', CustomObtainAuthToken.as_view()),
]
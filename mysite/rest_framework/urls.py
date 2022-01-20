from django.urls import path, include
from mysite.photos.models import Photo
from rest_framework import routers, serializers, viewsets

app_name = 'api'

# Serializers define the API representation.
class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['file', 'title', 'uploaded_at']


# ViewSets define the view behavior.
class RestView(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotosSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'files', RestView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

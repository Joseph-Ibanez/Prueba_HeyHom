from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'api/properties', PropertyViewSet, basename='property')

#urlpatterns = [
urlpatterns = router.urls + [
    path('api/properties/listing/', PropertyViewSet.as_view({'get' : 'list_all_properties'}), name='list_all_properties'),
    path('api/properties/<int:pk>/retrieve_property/', PropertyViewSet.as_view({'get': 'retrieve_single_property'}), name='retrieve_single_property'),
    path('api/properties/create/', PropertyViewSet.as_view({'post': 'create_property'}), name='create_property'),
    path('api/properties/<int:pk>/update/', PropertyViewSet.as_view({'put': 'update_property'}), name='update_property'),
    path('api/properties/<int:pk>/delete/', PropertyViewSet.as_view({'delete': 'delete_property'}), name='delete_property'),
]
    #path('api/properties/<int:id_property>/delete_property/', DeletePropertyView.as_view(), name='delete_property'),


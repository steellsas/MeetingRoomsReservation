from django.urls import path
from accounts.views import UserViewSet

app_name = 'accounts'

urlpatterns = [
    path('user/register/', UserViewSet.as_view({'post': 'create'}), name='user_register'),
    path('user/all/', UserViewSet.as_view({'get': 'list'}, name='user_list')),
    path('user/detail/<int:pk>', UserViewSet.as_view({'get': 'retrieve', 'put':'update'}, name='user_detail'))

]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterVendorView, ShopListCreateView, ShopRetrieveUpdateDeleteView, NearbyShopsView, LogoutView

urlpatterns = [
    path('register/', RegisterVendorView.as_view(), name='register_vendor'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shops/', ShopListCreateView.as_view(), name='shop_list_create'),
    path('shops/<int:pk>/', ShopRetrieveUpdateDeleteView.as_view(), name='shop_detail'),
    path('shops/nearby/', NearbyShopsView.as_view(), name='nearby_shops'),
]
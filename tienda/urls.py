from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductoViewSet, RegisterView, CarritoView,
    agregar_al_carrito, crear_pedido, ListaPedidosUsuario
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/carrito/', CarritoView.as_view(), name='carrito'),
    path('api/carrito/agregar/', agregar_al_carrito, name='agregar-al-carrito'),
    path('api/pedido/crear/', crear_pedido, name='crear-pedido'),
    path('api/pedidos/', ListaPedidosUsuario.as_view(), name='lista-pedidos'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
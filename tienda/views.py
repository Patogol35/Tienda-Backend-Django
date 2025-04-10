from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Producto, Carrito, ItemCarrito, Pedido, ItemPedido
from .serializers import (
    ProductoSerializer,
    CarritoSerializer,
    UserSerializer,
    ItemCarritoSerializer,
    PedidoSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def agregar_al_carrito(request):
    producto_id = request.data.get('producto_id')
    cantidad = int(request.data.get('cantidad', 1))
    try:
        producto = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto,
        defaults={'cantidad': cantidad}
    )
    if not creado:
        item.cantidad += cantidad
        item.save()
    serializer = ItemCarritoSerializer(item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
class CarritoView(generics.RetrieveAPIView):
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        carrito, _ = Carrito.objects.get_or_create(usuario=self.request.user)
        return carrito
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_pedido(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    if not items:
        return Response({'error': 'El carrito está vacío'}, status=400)
    total = sum([item.producto.precio * item.cantidad for item in items])
    pedido = Pedido.objects.create(usuario=request.user, total=total)
    for item in items:
        # Descontar stock
        producto = item.producto
        if producto.stock < item.cantidad:
            return Response({'error': f'Stock insuficiente para {producto.nombre}'}, status=400)
        producto.stock -= item.cantidad
        producto.save()
        ItemPedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=item.cantidad,
            precio_unitario=producto.precio
        )
    # Vaciar carrito
    items.delete()
    serializer = PedidoSerializer(pedido)
    return Response(serializer.data, status=201)
class ListaPedidosUsuario(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
       return Pedido.objects.filter(usuario=self.request.user).order_by('-fecha')


 
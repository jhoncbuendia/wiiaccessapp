from rest_framework.serializers import ModelSerializer
from directory.models import Empresa, Taladro, Extension, Proveedor, UsuarioApp, AlertaPanico, ProveedorGlobal, Favorito


class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        field = ('id', 'nombre')

class TaladroSerializer(ModelSerializer):
    class Meta:
        model = Taladro
        field = ('id', 'telefono_ppal', 'correo_ppal', 'correo_sec', 'empresa', 'favorito')

class ExtensionSerializer(ModelSerializer):
    class Meta:
        model = Extension
        field = ('id', 'nro_extension', 'responsable', 'taladro')

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        field = ('id', 'nombre', 'telefono', 'correo_contacto', 'empresa', 'favorito')

class UsuarioAppSerializer(ModelSerializer):
    class Meta:
        model = UsuarioApp
        field = ('id', 'user', 'correo_contacto', 'empresa')

class AlertaPanicoSerializer(ModelSerializer):
    class Meta:
        model = AlertaPanico
        field = ('id', 'email', 'usuario')

class ProveedorGlobalSerializer(ModelSerializer):
    class Meta:
        model = ProveedorGlobal
        field = ('id', 'nombre', 'telefono', 'correo_contacto')

class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        field = ('nombre', 'direccion','id', 'telefono', 'correo', 'usuario','tipo')



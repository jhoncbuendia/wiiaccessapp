from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http.response import HttpResponse, Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from directory.models import Empresa, Taladro, Extension, Proveedor, UsuarioApp, AlertaPanico, ProveedorGlobal, Favorito
from directory.serializers import EmpresaSerializer, TaladroSerializer, ExtensionSerializer, ProveedorSerializer, \
    UsuarioAppSerializer, AlertaPanicoSerializer, ProveedorGlobalSerializer, FavoritoSerializer


# ---Inicio Servicio Empresa
class EmpresaList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = EmpresaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = EmpresaSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = EmpresaSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
EmpresaList = EmpresaList.as_view()
EmpresaDetail = EmpresaDetail.as_view()

#---Fin Servicio Empresa


#----------------------------------------------------------



#---Inicio Servicio Taladro
class TaladroList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        q = request.GET.get("sorting", False)
        e = request.GET.get("empresa", False)
        top = request.GET.get("top", False)

        skip = request.GET.get("top", None)

        if (q != "undefined") and (top != False):


            sorting = request.GET.get('sorting')
            sorting = sorting.split();
            print sorting[1]
            top = request.GET.get("top", None)
            skip = request.GET.get("top", None)
            if sorting[1] == "ASC":
                taladros = Taladro.objects.filter(empresa__id = e).order_by(sorting[0])

                paginator = Paginator(taladros, top)
                page = paginator.page(1)
                serializer = TaladroSerializer(page.object_list, many=True)

                return Response(serializer.data)
            else:
                print "ordenando desc " + str(sorting[0])
                taladros = Taladro.objects.filter(empresa__id = e).order_by("-" + sorting[0])
                paginator = Paginator(taladros, top)
                page = paginator.page(1)
                serializer = TaladroSerializer(page.object_list, many=True)
                return Response(serializer.data)
        if top:
            taladros = Taladro.objects.filter(empresa__id = e)
            paginator = Paginator(taladros, top)
            page = paginator.page(1)
            serializer = TaladroSerializer(page.object_list, many=True)
            return Response(serializer.data)

        if e:

            taladros = Taladro.objects.filter(empresa = e)
            serializer = TaladroSerializer(taladros, many=True)
            return Response(serializer.data)


        taladros = Taladro.objects.all()
        serializer = TaladroSerializer(taladros, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        q = request.GET.get("single", False)
        print q
        if q == '1':
            #print 1
            serializer = TaladroSerializer(data=request.DATA)
        else:
            #print 0
            serializer = TaladroSerializer(data=request.DATA, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaladroDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Taladro.objects.get(pk=pk)
        except Taladro.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = TaladroSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = TaladroSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
TaladroList = TaladroList.as_view()
TaladroDetail = TaladroDetail.as_view()

#---Fin Servicio Taladro

#---Inicio Servicio Extension
class ExtensionList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        extensiones = Extension.objects.all()
        serializer = ExtensionSerializer(extensiones, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = ExtensionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExtensionDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Extension.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ExtensionSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ExtensionSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
ExtensionList = ExtensionList.as_view()
ExtensionDetail = ExtensionDetail.as_view()

#---Fin Servicio Extension

#---Inicio Servicio Proveedor
class ProveedorList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        q = request.GET.get("sorting", False)
        top = request.GET.get("top", False)
        e = request.GET.get("empresa", False)

        skip = request.GET.get("top", None)

        if (q != "undefined") and (top != False):


            sorting = request.GET.get('sorting')
            sorting = sorting.split();
            print sorting[1]
            top = request.GET.get("top", None)
            skip = request.GET.get("top", None)
            if sorting[1] == "ASC":

                proveedores = Proveedor.objects.filter(empresa__id = e).order_by(sorting[0])

                paginator = Paginator(proveedores, top)
                page = paginator.page(1)

                serializer = ProveedorSerializer(page.object_list, many=True)

                return Response(serializer.data)
            else:
                print "ordenando desc " + str(sorting[0])
                proveedores = Proveedor.objects.filter(empresa__id = e).order_by("-" + sorting[0])
                paginator = Paginator(proveedores, top)
                page = paginator.page(1)
                serializer = ProveedorSerializer(page.object_list, many=True)
                return Response(serializer.data)
        if top:

            proveedores = Proveedor.objects.filter( empresa__id = e)

            paginator = Paginator(proveedores, top)
            page = paginator.page(1)
            serializer = ProveedorSerializer(page.object_list, many=True)
            print serializer.data
            return Response(serializer.data)

        if e:
            proveedores = Proveedor.objects.filter(empresa = e)
            serializer = ProveedorSerializer(proveedores, many=True)
            return Response(serializer.data)


        proveedores = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        q = request.GET.get("single", False)
        #print q
        if q == '1':
            #print 1
            serializer = ProveedorSerializer(data=request.DATA)
        else:
            #print 0
            serializer = ProveedorSerializer(data=request.DATA, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ProveedorSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ProveedorSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
ProveedorList = ProveedorList.as_view()
ProveedorDetail = ProveedorDetail.as_view()

#---Fin Servicio Proveedor


#---Fin Servicio Extension

#---Inicio Servicio UsuarioApp
class UsuarioAppList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        usuariosapp = UsuarioApp.objects.all()
        serializer = UsuarioAppSerializer(usuariosapp, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = UsuarioAppSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioAppDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return UsuarioApp.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = UsuarioAppSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = UsuarioAppSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
UsuarioAppList = UsuarioAppList.as_view()
UsuarioAppDetail = UsuarioAppDetail.as_view()

#---Fin Servicio UsuarioApp


#---Inicio Servicio AlertaPanico
class AlertaPanicoList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        alertas = AlertaPanico.objects.all()
        serializer = AlertaPanicoSerializer(alertas, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = AlertaPanicoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlertaPanicoDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return AlertaPanico.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = AlertaPanicoSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = AlertaPanicoSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
AlertaPanicoList = AlertaPanicoList.as_view()
AlertaPanicoDetail = AlertaPanicoDetail.as_view()

#---Fin Servicio UsuarioApp



#---Inicio Servicio ProveedorGlobal
class ProveedorGlobalList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        proveedor = ProveedorGlobal.objects.all()
        serializer = ProveedorGlobalSerializer(proveedor, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = ProveedorGlobalSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProveedorGlobalDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return ProveedorGlobal.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ProveedorGlobalSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ProveedorGlobalSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
ProveedorGlobalList = ProveedorGlobalList.as_view()
ProveedorGlobalDetail = ProveedorGlobalDetail.as_view()

#---Fin Servicio ProveedorGloba



#---Inicio Servicio Favorito
class FavoritoList(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        favoritos = Favorito.objects.all()
        serializer = FavoritoSerializer(favoritos, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = FavoritoSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoritoDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Favorito.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = FavoritoSerializer(survey, data=request.DATA)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = FavoritoSerializer(survey, data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---Definicion Vistas
FavoritoList = FavoritoList.as_view()
FavoritoDetail = FavoritoDetail.as_view()

#---Fin Servicio Favorito


def createTokens(request):
    usuarios = User.objects.all()

    for u in usuarios:
        token = Token.objects.create(user=u)
        print token.key

    return HttpResponse('ok')




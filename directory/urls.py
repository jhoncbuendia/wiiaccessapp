from django.conf.urls import patterns, include, url
from directory.views import EmpresaList, EmpresaDetail, TaladroList, TaladroDetail, ExtensionList, ExtensionDetail, \
    ProveedorList, ProveedorDetail, UsuarioAppList, UsuarioAppDetail, AlertaPanicoList, AlertaPanicoDetail, \
    ProveedorGlobalList, ProveedorGlobalDetail, FavoritoList, FavoritoDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wiiaccessapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #urls Empresa

    url(r'^empresa/list/', EmpresaList),
    url(r'^empresa/detail/(?P<pk>[0-9]+)/', EmpresaDetail),



    #urls Taladro
    url(r'^taladro/list/', TaladroList),
    url(r'^taladro/detail/(?P<pk>[0-9]+)/', TaladroDetail),

    #urls Extension
    url(r'^extension/list/', ExtensionList),
    url(r'^extension/detail/(?P<pk>[0-9]+)/', ExtensionDetail),

    #urls Proveedor
    url(r'^proveedor/list/', ProveedorList),
    url(r'^proveedor/detail/(?P<pk>[0-9]+)/', ProveedorDetail),
    
    #urls UsuarioApp
    url(r'^usuarioapp/list/', UsuarioAppList),
    url(r'^usuarioapp/detail/(?P<pk>[0-9]+)/', UsuarioAppDetail),

    #urls AlertaPanico
    url(r'^alertapanico/list/', AlertaPanicoList),
    url(r'^alertapanico/detail/(?P<pk>[0-9]+)/', AlertaPanicoDetail),

    #urls Proveedor Global
    url(r'^proveedorglobal/list/', ProveedorGlobalList),
    url(r'^proveedorglobal/detail/(?P<pk>[0-9]+)/', ProveedorGlobalDetail),

    #urls Favorito
    url(r'^favorito/list/$', FavoritoList),
    url(r'^favorito/detail/(?P<pk>[0-9]+)/', FavoritoDetail),


)
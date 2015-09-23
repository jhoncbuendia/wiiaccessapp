from django.contrib import admin

# Register your models here.
from directory.models import Extension, Taladro, Proveedor, Favorito, AlertaPanico, UsuarioApp, Empresa, ProveedorGlobal

class AdminEmpresa(admin.ModelAdmin):
	list_display = ('nombre', 'id')
	list_filter = ('nombre', 'id')
	search_fields = ('nombre', 'id')

class AdminExtension(admin.ModelAdmin):
	list_display = ('nro_extension','responsable','taladro',)
	list_filter = ('nro_extension','responsable','taladro',)
	search_fields = ('nro_extension','responsable','taladro',)

class AdminTaladro(admin.ModelAdmin):
	list_display = ('nombre','telefono_ppal','correo_ppal','correo_sec','empresa','favorito')
	list_filter = ('nombre','telefono_ppal','correo_ppal','correo_sec','empresa', 'favorito')
	search_fields = ('nombre','telefono_ppal','correo_ppal','correo_sec','empresa', 'favorito')

class AdminFavorito(admin.ModelAdmin):
	list_display = ('nombre', 'direccion','telefono','correo','usuario','tipo', )
	list_filter = ('nombre', 'direccion','telefono','correo','usuario','tipo',)
	search_fields = ('nombre', 'direccion','telefono','correo','usuario','tipo',)

class AdminAlertaPanico(admin.ModelAdmin):
	list_display = ('email','usuario',)
	list_filter = ('email','usuario',)
	search_fields = ('email','usuario',)

class AdminProveedor(admin.ModelAdmin):
	list_display = ('nombre','telefono','correo_contacto','empresa', 'favorito')
	list_filter = ('nombre','telefono','correo_contacto','empresa', 'favorito')
	search_fields = ('nombre','telefono','correo_contacto','empresa', 'favorito')

class AdminProveedorGlobal(admin.ModelAdmin):
	list_display = ('nombre','telefono','correo_contacto',)
	list_filter = ('nombre','telefono','correo_contacto',)
	search_fields = ('nombre','telefono','correo_contacto',)

class AdminUsuarioApp(admin.ModelAdmin):
	list_display = ('empresa','user','correo_contacto',)
	list_filter = ('empresa','user','correo_contacto','empresa',)
	search_fields = ('empresa','user','correo_contacto','empresa',)


admin.site.register(Extension, AdminExtension)
admin.site.register(Taladro, AdminTaladro )
admin.site.register(Favorito, AdminFavorito)
admin.site.register(AlertaPanico, AdminAlertaPanico)
admin.site.register(Proveedor, AdminProveedor)
admin.site.register(Empresa,AdminEmpresa)
admin.site.register(ProveedorGlobal, AdminProveedorGlobal)
admin.site.register(UsuarioApp, AdminUsuarioApp)

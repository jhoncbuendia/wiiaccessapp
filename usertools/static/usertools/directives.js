/**
 * Created by jhon on 26/11/14.
 */

app.directive('notificacionEstado', function ($compile, notificacionService){
    return {
        scope:true,
        restrict: 'E',//<dir-template></dir-template> hace referencia a un elemento/etiqueta html
        template: '<li class="notificacion" ng-repeat="n in notificaciones"><a href="#" id="[[n.id]]" class="[[n.id]]" ng-click="cambiarEstado(n.id)">[[n.nombre]]</a></li>',
        link: function (scope,element){
            for (var n in notificacionService.getAll()){
                console.log(n);
                if(notificacionService.getAll()[n].estado == 1) {
                      //console.log(notificacionService.getAll());
                      cambiarColorActivado(n);
                      habilitarNotifacion(n);
                  }else{

                      notificacionService.getAll()[n].estado = 0;
                     // console.log(notificacionService.getAll());
                      cambiarColorDesactivado(n);
                      desabilitarNotifacion(n);
                 }
            }

        }
    };
});
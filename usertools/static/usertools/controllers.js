var empresa;
app.controller('startApp', ['$scope', 'defaultService', function ($scope, notificacionService, ContenidoNotificacionesService, defaultService) {
    empresa = $("#empresa").attr("value");
    //console.log(empresa);
    $scope.setFile = function () {
        $scope.csv = false;
        // The event listener for the file upload
        document.getElementById('txtFileUpload').addEventListener('change', upload, false);

        // Method that checks that the browser supports the HTML5 File API
        function browserSupportFileUpload() {
            var isCompatible = false;
            if (window.File && window.FileReader && window.FileList && window.Blob) {
                isCompatible = true;
            }
            return isCompatible;
        }

        // Method that reads and processes the selected file
        function upload(evt) {
            if (!browserSupportFileUpload()) {
                alert('The File APIs are not fully supported in this browser!');
            } else {
                var data = null;
                var file = evt.target.files[0];
                var reader = new FileReader();
                reader.readAsText(file);
                reader.onload = function (event) {
                    var csvData = event.target.result;
                    data = $.csv.toArrays(csvData);
                    if (data && data.length > 0) {
                        //alert('Imported -' + data.length + '- rows successfully!');
                        console.log(data);
                        $scope.csv = data;

                        //alert($scope.csv);
                    } else {
                        alert('No data to import!');
                    }
                };
                reader.onerror = function () {
                    alert('Unable to read ' + file.fileName);
                };
            }
        };

    }

    $scope.setFile();


}]);


app.controller('serviceController', ['$scope', 'defaultService', function ($scope, defaultService) {

}]);

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


function parseQueryString(queryString) {

    var params = {}, queries, temp, i, l;

    // Split into key/value pairs
    queries = queryString.split("&");

    // Convert the array of strings into an object
    for (i = 0, l = queries.length; i < l; i++) {
        temp = queries[i].split('=');
        params[temp[0]] = temp[1];
    }

    return params;
};


/*Inicio metodos ajax proveedores */
function getProveedores(postData, jtParams) {

    //console.log(jtParams);
    var ret;
    var query = "/directory/proveedor/list?sorting=" + jtParams['jtSorting'] + "&skip=" + jtParams.jtStartIndex + "&top=" + jtParams.jtPageSize + "&empresa=" + empresa ;
    //+ "&$format=json" //give me json... will be used in newer OData
    //+ "&$callback=callback"; //this is my callback for future
    return $.Deferred(function ($dfd) {
        $.ajax({
            url: query,
            type: 'GET',
            dataType: 'json',
            data: postData,
            success: function (data) {
                ret = {
                    'Result': "OK",
                    'Records': data,
                    'TotalRecordCount': 500

                };
                //console.log(data);
                $dfd.resolve(ret);
            },
            error: function () {
                $dfd.reject();
            }
        });
    });

}




function updateProveedor(item) {

    var id = parseQueryString(item)['id'];
    console.log(id);

    var ret;
    return $.Deferred(function ($dfd) {
        $.ajax({
            url: '/directory/proveedor/detail/' + id,
            type: 'PUT',
            dataType: 'json',
            data: item,
            success: function (data) {
                ret = {
                    'Result': "OK",
                    'Record': data
                };
                $dfd.resolve(ret);
            },
            error: function () {
                $dfd.reject();
            }
        });
    });
}

function deleteProveedor(item) {

    return $.Deferred(function ($dfd) {
        $.ajax({
            url: '/directory/proveedor/detail/' + item['id'],
            type: 'DELETE',
            dataType: 'json',
            data: item,
            success: function (data) {
                $dfd.resolve({ 'Result': "OK" });
            },
            error: function () {
                $dfd.reject();
            }
        });
    });
}

/*Fin  metodos ajax proveedores */


/*Inicio metodos ajax taladros */
function getTaladros(postData, jtParams) {
    console.log(jtParams);
    var ret;
    var query = "/directory/taladro/list/?sorting=" + jtParams['jtSorting'] + "&skip=" + jtParams.jtStartIndex + "&top=" + jtParams.jtPageSize + "&empresa=" + empresa;
    //+ "&$format=json" //give me json... will be used in newer OData
    //+ "&$callback=callback"; //this is my callback for future
    return $.Deferred(function ($dfd) {
        $.ajax({
            url: query,
            type: 'GET',
            dataType: 'json',
            data: postData,
            success: function (data) {
                ret = {
                    'Result': "OK",
                    'Records': data,
                    'TotalRecordCount': 500

                };
                console.log(data);
                $dfd.resolve(ret);
            },
            error: function () {
                $dfd.reject();
            }
        });
    });

}




function updateTaladro(item) {

    var id = parseQueryString(item)['id'];
    console.log(id);

    var ret;
    return $.Deferred(function ($dfd) {
        $.ajax({
            url: '/directory/taladro/detail/' + id,
            type: 'PUT',
            dataType: 'json',
            data: item,
            success: function (data) {
                ret = {
                    'Result': "OK",
                    'Record': data
                };
                $dfd.resolve(ret);
            },
            error: function () {
                $dfd.reject();
            }
        });
    });
}


function deleteTaladro(item) {

    return $.Deferred(function ($dfd) {
        $.ajax({
            url: '/directory/taladro/detail/' + item['id'],
            type: 'DELETE',
            dataType: 'json',
            data: item,
            success: function (data) {
                $dfd.resolve({ 'Result': "OK" });
            },
            error: function () {
                $dfd.reject();
            }
        });
    });
}

/*Fin metodos ajax taladros */

app.controller('accionesController', ['$scope', 'defaultService', function ($scope, defaultService) {

    $scope.crearProveedor = function(){
        var data = [];
        var proveedor = {};


        proveedor['nombre'] = $scope.prov_nombre;
        proveedor['telefono'] = $scope.prov_telefono;
        proveedor['correo_contacto'] = $scope.prov_correo;
        proveedor['empresa'] = empresa;


        data.push(proveedor);
        defaultService.post('/directory/proveedor/list/', data, function(){alert('Proveedor creado con exito'); $('#table_proveedor').jtable('load');}, function(data){alert('error al crear proveedor'); console.log(data)})

        console.log(data);
    }

    $scope.crearTaladro = function(){
        var data = [];
        var taladro = {};
        taladro['nombre'] = $scope.tal_nombre;
        taladro['telefono_ppal'] = $scope.tal_telefono;
        taladro['correo_ppal'] = $scope.tal_correo;
        taladro['correo_sec'] = $scope.tal_correo_sec;
        taladro['empresa'] = empresa;
        data.push(taladro);
        //console.log(data);
        defaultService.post('/directory/taladro/list/', data, function(){alert('Taladro creado con exito');  $('#table_taladro').jtable('load');}, function(data){alert('error al crear taladro'); console.log(data)})
        //$scope.administrarTaladros();
        console.log(data);
    }

    $scope.administrarProveedores = function () {
        $scope.tipo_csv = 1;
        $("#dvImportSegments").css("display", "inline");
        $("#crear_taladro").css("display", "none");
        $("#crear_proveedores").css("display", "inline");
        $('#table_container').html("");
        $('#table_container').html("<div id='table_proveedor'></div>");

        $('#table_proveedor').jtable({
            title: 'Edicion De Proveedores',
            sorting: true, //Enable sorting
            paging: true,
            pageSize: 10,
            sorting: true,
            multiSorting: true,

            actions: {
                listAction: getProveedores,
                updateAction: updateProveedor,
                deleteAction: deleteProveedor
            },
            fields: {
                id: {
                    key: true,
                    list: false
                },
                nombre: {
                    title: 'Nombre',
                    width: '40%',

                },
                telefono: {
                    title: 'Telefono',
                    width: '20%',

                },
                correo_contacto: {
                    title: 'Correo Contacto',
                    width: '30%',


                },
                    empresa: {
                        title: 'Empresa',
                        width: '30%',
                        list: false,
                        key: true,
                        edit :false



                    }
            },

            formCreated: function (event, data) {
                data.form.find('input[name="nombre"]').addClass(
                  'validate[required]');
                data.form.find('input[name="telefono"]').addClass(
                  'validate[required]')
                data.form.find('input[name="correo_contacto"]').addClass(
                  'validate[required,,custom[email]]]')
                data.form.find('input[name="empresa"]').addClass(
                  'validate[required]')

                data.form.validationEngine();
            },
            formSubmitting: function (event, data) {
                return data.form.validationEngine('validate');
            },
            formClosed: function (event, data) {
                data.form.validationEngine('hide');
                data.form.validationEngine('detach');
            }

        });


        $('#table_proveedor').jtable('load');

    }

    $scope.administrarTaladros = function () {
        //$('#table_proveedor').hide();
        $("#crear_taladro").css("display", "inline");
        $("#crear_proveedores").css("display", "none");
        $scope.tipo_csv = 2;
        $("#dvImportSegments").css("display", "inline");
        $('#table_container').html("");
        $('#table_container').html("<div id='table_taladro'></div>");
        $('#table_taladro').jtable({
            title: 'Edicion De Taladros',
            sorting: true, //Enable sorting
            paging: true,
            pageSize: 10,
            sorting: true,
            multiSorting: true,

            actions: {
                listAction: getTaladros,
                updateAction: updateTaladro,
                deleteAction: deleteTaladro
            },
            fields: {
                id: {
                    key: true,
                    list: false
                },
                nombre: {
                    title: 'Nombre',
                    width: '20%',

                },
                telefono_ppal: {
                    title: 'Telefono',
                    width: '20%',

                },
                correo_ppal: {
                    title: 'Correo Principal',
                    width: '25%',


                },
                correo_sec: {
                    title: 'Correo secundario',
                    width: '25%',

                },

                empresa: {
                    title: 'Empresa',
                    width: '35%',
                    list: false,
                    key: true,
                    edit :false



                }
            },

            formCreated: function (event, data) {
                data.form.find('input[name="nombre"]').addClass(
                  'validate[required]');
                data.form.find('input[name="telefono_ppal"]').addClass(
                  'validate[required]');
                data.form.find('input[name="correo_ppal"]').addClass(
                  'validate[required,,custom[email]]]');
                data.form.find('input[name="correo_sec"]').addClass(
                  'validate[required,,custom[email]]]');
                data.form.find('input[name="empresa"]').addClass(
                  'validate[required]')

                data.form.validationEngine();
            },
            formSubmitting: function (event, data) {
                return data.form.validationEngine('validate');
            },
            formClosed: function (event, data) {
                data.form.validationEngine('hide');
                data.form.validationEngine('detach');
            }

        });


        $('#table_taladro').jtable('load');


    }

    $scope.cargarDatos = function () {
        if ($scope.csv) {
            //console.log($scope.csv);
            //console.log($scope.tipo_csv);
            //console.log($scope.csv);
            //tipocsv 1 = proveedor, 2 = taladro
            if ($scope.tipo_csv == 1) {
                //alert($scope.csv);
                var dt = [];
                var aux = {};
                for (f in $scope.csv) {
                    //console.log($scope.csv[f]);

                    //console.log(fila);

                    aux['nombre'] = $scope.csv[f][0];
                    aux['telefono'] = $scope.csv[f][1];
                    aux['correo_contacto'] = $scope.csv[f][2];
                    aux['empresa'] = empresa;
                    console.log(aux);
                    dt.push(aux);
                    aux = {};
                    //$scope.csv.length = 0;
                    console.log(dt)

                }
                //$('#txtFileUpload').value('');

                defaultService.post('/directory/proveedor/list/', dt, function (d) {
                    alert('Datos cargados con exito');
                    error = false;
                    console.log(d);
                    //console.log(data);
                    //$scope.csv.length = 0
                    $("#txtFileUpload").replaceWith($("#txtFileUpload").clone());
                    $scope.setFile();
                    $('#table_proveedor').jtable('load');

                }, function (d) {
                    alert('Error cargando datos, revise el formato del archivo');
                    //$scope.csv.length = 0
                    $("#txtFileUpload").replaceWith($("#txtFileUpload").clone());
                    $scope.setFile();

                });


            }
            if ($scope.tipo_csv == 2) {
                //alert($scope.csv);
                var dt = [];
                var aux = {};
                for (f in $scope.csv) {
                    //console.log($scope.csv[f]);

                    //console.log(fila);

                    aux['nombre'] = $scope.csv[f][0];
                    aux['telefono_ppal'] = $scope.csv[f][1];
                    aux['correo_ppal'] = $scope.csv[f][2];
                    aux['correo_sec'] = $scope.csv[f][3];
                    aux['empresa'] = empresa;
                    console.log(aux);
                    dt.push(aux);
                    aux = {};
                    //$scope.csv.length = 0;
                    console.log(dt)

                }
                //$('#txtFileUpload').value('');

                defaultService.post('/directory/taladro/list/', dt, function (d) {
                    alert('Datos cargados con exito');
                    error = false;
                    console.log(d);
                    //console.log(data);
                    //$scope.csv.length = 0
                    $("#txtFileUpload").replaceWith($("#txtFileUpload").clone());
                    $scope.setFile();
                    $('#table_taladro').jtable('load');

                }, function (d) {
                    alert('Error cargando datos, revise el formato del archivo');
                    //$scope.csv.length = 0
                    $("#txtFileUpload").replaceWith($("#txtFileUpload").clone());
                    $scope.setFile();
                });


            }


        } else {
            alert("seleccione un archivo");
        }

    }


}]);










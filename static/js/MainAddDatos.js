// Obtener el token CSRF desde la cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica si este cookie comienza con el nombre dado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken');

// Configurar jQuery para enviar el token CSRF automáticamente
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
        }
    }
});

$(document).ready(function () {
    console.log('jQuery MainAddDatos Activo')
    const addDatosUrl = $('#add-datos-url').val();
    const deleteDatoUrl = $('#delete-marca-url').val();
    const csrfToken = $('#csrf-token').val();

    $('#marcaForm').on('submit', function (e) {
        e.preventDefault();  
        let formData = $(this).serialize();  

        $.ajax({
            type: 'POST',
            url: addDatosUrl,
            data: formData,
            success: function (response) {
                console.log('Success response:', response);  

                if (response.success) {
                    // Mostrar mensaje de éxito
                    $('#successMessage').text('Marca añadida correctamente.');
                    $('#successMessage').show();

                    // Limpiar los campos del formulario
                    $('#marcaForm')[0].reset();

                    // Agregar la nueva marca a la lista en el modal
                    $('#marcaContainer').append(
                        `<div class="container p-2 col-lg-6" style="display: flex; justify-content: space-evenly;">
                            <h3>${response.new_marca.name}</h3>
                            <button class="btn btn-danger delete-marca" id="marca-${response.new_marca.id}" data-id="${response.new_marca.id}" data-type="marca">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>`
                    );

                    // Reasignar el evento de eliminar marca
                    assignDeleteMarcaEvent();

                    // Ocultar mensaje después de un tiempo
                    setTimeout(function () {
                        $('#successMessage').fadeOut('slow');
                    }, 2000);
                } else {
                    console.log('Errors:', response.errors);
                }
            },
            error: function () {
                $('#successMessage').text('Ocurrió un error. Inténtalo de nuevo.');
                $('#successMessage').css('color', 'red');
                $('#successMessage').show();

                setTimeout(function () {
                    $('#successMessage').fadeOut('slow');
                }, 2000);
            }
        });
    });

    $('#form-add-liga').on('submit', function(e){
        e.preventDefault();
        let formData = $(this).serialize();
        $.ajax ({
            type : 'POST',
            url : addDatosUrl,
            data : formData,
            success : function(response){
                if (response.success){
                    $('#successMessageLiga').text('Liga añadida correctamente');
                    $('#successMessageLiga').show();
                    $('#form-add-liga')[0].reset();
                    $('#ligaContainer').append(
                        `<div class="container p-2 col-lg-6" style="display: flex; justify-content: space-evenly;">
                            <h3>${response.new_liga.name}</h3>
                            <button class="btn btn-danger delete-liga" id="liga-${response.new_liga.id}" data-id="${response.new_liga.id}" data-type="liga">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>`
                    )
                    assignDeleteMarcaEvent();
                    setTimeout(function(){
                        $('#successMessageLiga').fadeOut('slow');
                    },2000);
                } else {
                    console.log('Errors: ', response.errors);
                }
            },
            error: function () {
                $('#successMessageLiga').text('Ocurrió un error. Inténtalo de nuevo.');
                $('#successMessageLiga').css('color', 'red');
                $('#successMessageLiga').show();

                setTimeout(function () {
                    $('#successMessageLiga').fadeOut('slow');
                }, 2000);
            }
        })
    });

    $('#form-add-equipos').on('submit', function(e){
        e.preventDefault();
        let formData = $(this).serialize();
        $.ajax ({
            type : 'POST',
            url : addDatosUrl,
            data : formData,
            success : function(response){
                console.log('succes response equipos', response);

                if (response.success){
                    $('#successMessageEquipo').text('Equipo añadido correctamente');
                    $('#successMessageEquipo').show();

                    $('#form-add-equipos')[0].reset();

                    $('#EquipoContainer').append(
                        `
                        <div class="container p-2 col-lg-6" style="display: flex; justify-content: space-evenly;">
                            <h3>${response.new_equipo.name}</h3>
                            <p>${response.new_equipo.categoria_name}</p>
                            <button class="btn btn-danger delete-equipo" id="equipo-${response.new_equipo.id}" data-id="${response.new_equipo.id}" data-type="equipo">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>
                        `
                    )

                    assignDeleteMarcaEvent();

                    setTimeout(function(){
                        $('#successMessageEquipo').fadeOut('slow');
                    },2000);
                } else {
                    console.log('Errors: ', response.errors);
                }
            },
            error: function () {
                $('#successMessageEquipo').text('Ocurrió un error. Inténtalo de nuevo.');
                $('#successMessageEquipo').css('color', 'red');
                $('#successMessageEquipo').show();

                setTimeout(function () {
                    $('#successMessageEquipo').fadeOut('slow');
                }, 2000);
            }
        })
    });

    $('#form-add-tallas').on('submit', function(e){
        e.preventDefault();
        let formData = $(this).serialize();
        $.ajax ({
            type : 'POST',
            url : addDatosUrl,
            data : formData,
            success : function(response){
                console.log('succes response talla', response);

                if (response.success){
                    $('#successMessageTalla').text('Talla añadido correctamente');
                    $('#successMessageTalla').show();
                    $('#form-add-tallas')[0].reset();
                    $('#TallaContainer').append(
                        `<div class="container p-2 col-lg-6">
                            <h3>${response.new_talla.name}</h3>
                            <button class="btn btn-danger delete-talla" id="talla-${response.new_talla.id}" data-id="${response.new_talla.id}" data-type="talla">
                                <i class="bi bi-trash"></i>
                            </button>
                        </div>`
                    )

                    assignDeleteMarcaEvent();

                    setTimeout(function(){
                        $('#successMessageTalla').fadeOut('slow');
                    },2000);
                } else {
                    console.log('Errors: ', response.errors);
                }
            },
            error: function (xhr, status, error) {
                console.log('Error response:', xhr.responseText);
                $('#successMessageTalla').text('Ocurrió un error. Inténtalo de nuevo.');
                $('#successMessageTalla').css('color', 'red');
                $('#successMessageTalla').show();

                setTimeout(function () {
                    $('#successMessageTalla').fadeOut('slow');
                }, 2000);
            }
        })
    });

    // Función para asignar el evento de eliminar
    function assignDeleteMarcaEvent() {
        // Usa `.off()` para eliminar eventos previos
        $(document).off('click', '.delete-marca').on('click', '.delete-marca', function () { 
            let marcaId = $(this).data('id'); 
            let Type = $(this).data('type'); 
            let deleteUrl = deleteDatoUrl.replace('/0/', '/' + marcaId + '/');
    
            $.ajax({
                type: 'POST',
                url: deleteUrl,
                data: {
                    'id-dato-delete': Type,
                    'csrfmiddlewaretoken':csrfToken
                },
                success: function (response) { 
                    if (response.success) {
                        $('#marca-' + marcaId).parent().remove();
                        $('#successMessages').text('Marca Eliminada');
                        $('#successMessages').show();
                        setTimeout(function () {
                            $('#successMessages').fadeOut('slow');
                        }, 2000);
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function (xhr, status, error) { 
                    alert('Ocurrió un error al intentar eliminar la marca.');
                }
            });
        });

        $(document).off('click', '.delete-liga').on('click', '.delete-liga', function () { 
            let ligaId = $(this).data('id'); 
            let Type = $(this).data('type');
            let deleteUrl = deleteDatoUrl.replace('/0/', '/' + ligaId + '/');
    
            $.ajax({
                type: 'POST',
                url: deleteUrl,
                data: {
                    'id-dato-delete': Type,
                    'csrfmiddlewaretoken':csrfToken
                },
                success: function (response) {
                    if (response.success) {
                        $('#liga-' + ligaId).parent().remove();
                        $('#successMessagesLiga').text('Liga Eliminada');
                        $('#successMessagesLiga').show();
                        setTimeout(function () {
                            $('#successMessagesLiga').fadeOut('slow');
                        }, 2000);
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function () {  
                    alert('Ocurrió un error al intentar eliminar la liga.');
                }
            });
        });

        $(document).off('click', '.delete-equipo').on('click', '.delete-equipo', function () { 
            let equipoId = $(this).data('id'); 
            let Type = $(this).data('type');
            let deleteUrl = deleteDatoUrl.replace('/0/', '/' + equipoId + '/');
    
            $.ajax({
                type: 'POST',
                url: deleteUrl,
                data: {
                    'id-dato-delete': Type,
                    'csrfmiddlewaretoken':csrfToken
                },
                success: function (response) { 
                    if (response.success) {
                        $('#equipo-' + equipoId).parent().remove();
                        $('#successMessageEquipo').text('Equipo Eliminada');
                        $('#successMessageEquipo').show();
                        setTimeout(function () {
                            $('#successMessageEquipo').fadeOut('slow');
                        }, 2000);
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function () {
                    alert('Ocurrió un error al intentar eliminar el equipo.');
                }
            });
        });

        $(document).off('click', '.delete-talla').on('click', '.delete-talla', function () {  
            let tallaId = $(this).data('id'); 
            let Type = $(this).data('type');
            let deleteUrl = deleteDatoUrl.replace('/0/', '/' + tallaId + '/');
    
            $.ajax({
                type: 'POST',
                url: deleteUrl,
                data: {
                    'id-dato-delete': Type,
                    'csrfmiddlewaretoken':csrfToken
                },
                success: function (response) { 
                    if (response.success) {
                        $('#talla-' + tallaId).parent().remove();
                        $('#successMessagesTalla').text('Talla Eliminada');
                        $('#successMessagesTalla').show();
                        setTimeout(function () {
                            $('#successMessagesTalla').fadeOut('slow');
                        }, 2000);
                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function () { 
                    alert('Ocurrió un error al intentar eliminar el Talla.');
                }
            });
        });
    }
    assignDeleteMarcaEvent();
});

$(document).ready(function() {
    function checkModalsClosed() {
        // Verifica si ambos modales están cerrados
        if (!$('#exampleModalToggleLigas').hasClass('show') && !$('#exampleModalToggleLigas2').hasClass('show')) {
            location.reload(); // Recargar página si ambos modales están cerrados
        }
    }

    // Evento al cerrar el primer modal (Agregar Ligas)
    $('#exampleModalToggleLigas').on('hidden.bs.modal', function () {
        checkModalsClosed(); // Verifica si ambos modales están cerrados
    });

    // Evento al cerrar el segundo modal (Listado de Ligas)
    $('#exampleModalToggleLigas2').on('hidden.bs.modal', function () {
        checkModalsClosed(); // Verifica si ambos modales están cerrados
    });
});
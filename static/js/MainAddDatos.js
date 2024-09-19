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
    const addDatosUrl = $('#add-datos-url').val();
    const deleteMarcaUrl = $('#delete-marca-url').val();
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
                    $('.modal-body.row').append(
                        `<div class="container p-2 col-lg-6" style="display: flex; justify-content: space-evenly;">
                            <h3>${response.new_marca.name}</h3>
                            <button class="btn btn-danger delete-marca" id="marca-${response.new_marca.id}" data-id="${response.new_marca.id}">
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
                    // Mostrar errores si los hay
                    console.log('Errors:', response.errors);  
                }
            },
            error: function (xhr, status, error) {
                console.log('Error response:', xhr.responseText);  
                // Mostrar mensaje de error si falla
                $('#successMessage').text('Ocurrió un error. Inténtalo de nuevo.');
                $('#successMessage').css('color', 'red');
                $('#successMessage').show();

                setTimeout(function () {
                    $('#successMessage').fadeOut('slow');
                }, 2000);
            }
        });
    });

    // Función para asignar el evento de eliminar
    function assignDeleteMarcaEvent() {
        // Usa `.off()` para eliminar eventos previos
        $(document).off('click', '.delete-marca').on('click', '.delete-marca', function () {  
            let marcaId = $(this).data('id');  
            let deleteUrl = deleteMarcaUrl.replace('/0/', '/' + marcaId + '/');
    
            $.ajax({
                type: 'POST',
                url: deleteUrl,
                data: {
                    'csrfmiddlewaretoken':csrfToken
                },
                success: function (response) {
                    console.log('Delete success response:', response);  
                    if (response.success) {
                        // Eliminar el contenedor de la marca
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
                    console.log('Delete error response:', xhr.responseText);  
                    alert('Ocurrió un error al intentar eliminar la marca.');
                }
            });
        });
    }

    // Asignar el evento de eliminar al cargar la página
    assignDeleteMarcaEvent();
});
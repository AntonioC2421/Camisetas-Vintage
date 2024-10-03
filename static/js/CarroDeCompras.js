function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrfToken = getCookie('csrftoken'); // Asegúrate de que solo aparezca una vez

let total = 0;

function datosCompra() {
    const precios = document.querySelectorAll('.precioItemCart');
    const nombres = document.querySelectorAll('.EquipoItemCart');

    total = 0;
    let listnombres = '';
    let listprecios = '';
    // Recorre todos los inputs y suma sus valores
    precios.forEach(input => {
        total += parseFloat(input.value) || 0; // Convierte a número y suma
    });

    nombres.forEach(input => {
        listnombres += input.value + '<br>';
    });

    precios.forEach(input => {
        listprecios += input.value + '<br>'; // Salto de línea para HTML
    });

    document.getElementById('totalPrecio').textContent = total; // Actualiza el total

    document.getElementById('NombresIndividuales').innerHTML = listnombres;
    document.getElementById('PreciosIndividuales').innerHTML = listprecios;
}
// Ejecuta la función cuando se cargue la página o cada vez que se necesite recalcular
window.onload = datosCompra;

$(document).ready(function () {
    console.log('jQuery de Carro de compras')
    const addItemCartUrl = $('#addItemCart-url').val()
    const deleteItemUrl = $('#delete-item-url').val()
    const validCodUrl = $('#btncodpro').val()

    $('#addToCartButtonn').on('click', function (e) {
        e.preventDefault();

        // Obtener la fecha actual en formato correcto
        const fechaClick = new Date();

        // Capturar los valores de los campos
        const itemIdString = $('#itemId').val();
        const itemIdNumber = parseInt(itemIdString, 10); // Convierte a número entero

        const userIdString = $('#userId').val();
        const userIdNumber = parseInt(userIdString, 10); // Convierte a número entero

        const formData = new FormData($('#addItemCartForm')[0]);
        formData.append('timestamp', fechaClick.toISOString()); // fecha en formato ISO

        // Enviar el formulario vía AJAX
        $.ajax({
            url: addItemCartUrl,
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                if (response.success) {
                    $('#successMessage').text('Añadido a carro de compra');
                    $('#successMessage').show();
                    setTimeout(function () {
                        $('#successMessage').fadeOut('slow');
                    }, 2000);
                    datosCompra(); // Actualiza el total después de añadir un item
                } else {
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.error('Ocurrió un error: ', error);
                console.error('Estado de respuesta: ', xhr.status);
                console.error('Texto de respuesta: ', xhr.responseText);
                alert('Hubo un problema con la solicitud: ' + xhr.status + ' - ' + xhr.responseText);
            }
        });
    });

    $('.delete-item').on('click', function () {
        let id_item = $(this).data('id');
        let deleteUrl = deleteItemUrl.replace('/0', '/' + id_item);

        $.ajax({
            type: 'POST',
            url: deleteUrl,
            data: {
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                if (response.success) {
                    // Elimina la card
                    $('#Item-' + id_item).parent().remove();
                    // Elimina la fila de la tabla
                    $('#row-item-' + id_item).remove(); // Asegúrate de que la fila tenga este ID
                    // Actualiza el total de precios
                    datosCompra(); // función para actualizar el total
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function () {
                alert('Ocurrió un error al intentar eliminar el item de tu carro de compra.');
            }
        });
    });

    // Evento 'submit' solo manejará el envío del formulario, ya sea por 'Enter' o por el botón.
    $('#promoForm').on('submit', function (e) {
        e.preventDefault();

        const codigoPromo = $('#inputCodPromo').val();

        console.log('Envío de código promocional:', codigoPromo);

        let validCod = validCodUrl.replace('cod', codigoPromo);
        console.log(validCod);
        $.ajax({
            type: 'POST',
            url: validCod,
            data: {
                'cod_pro': codigoPromo,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                if (response.success) {
                    $('#successMessages').text('Codigo ingresado correctamente');
                    $('#successMessages').show();
                    setTimeout(function () {
                        $('#successMessages').fadeOut('slow');
                    }, 2000);
                } else {
                    $('#successMessages').text('El codigo promocional no existe');
                    $('#successMessages').css('color', 'red');
                    $('#successMessages').show();

                    setTimeout(function () {
                        $('#successMessages').fadeOut('slow');
                    }, 2000);
                }
            },
            error: function (xhr, error) {
                console.error('Ocurrió un error: ', error);
                console.error('Estado de respuesta: ', xhr.status);
                console.error('Texto de respuesta: ', xhr.responseText);
                alert('Hubo un problema con la solicitud: ' + xhr.status + ' - ' + xhr.responseText);
            }
        });
    });

    // actualizar en tiempo real el precio total (sin codigo promocional)
    $('.precioItemCart').on('input', function () {
        datosCompra(); 
    });
});

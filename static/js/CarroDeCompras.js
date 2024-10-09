//{% csrf_token %}
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
const csrfToken = getCookie('csrftoken');

//Variables globales
let total = 0;
let Descuento = 0;
let totaldescuento = 0;

function datosCompra() {
    const precios = document.querySelectorAll('.precioItemCart');
    const nombres = document.querySelectorAll('.EquipoItemCart');

    total = 0;
    let listnombres = '';
    let listprecios = '';
    // Recorre todos los inputs y suma sus valores
    precios.forEach(input => {
        total += parseFloat(input.value) || 0;
    });

    nombres.forEach(input => {
        listnombres += input.value + '<br>';
    });

    precios.forEach(input => {
        listprecios += input.value + '<br>';
    });

    document.getElementById('totalPrecio').textContent = total;

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
    const VentaUrl = $('#btnVenta').val()
    const UrlItems = $('#btnItemsCart').val()

    
    $('#FormAddVenta').on('submit', function (e) {
        e.preventDefault();
        // Realizar la primera solicitud para obtener los ítems
        $.ajax({
            url: UrlItems,
            type: "GET",
            success: function (response) {
                if (response.success) {
                    console.log('Se recibieron los datos de los items:', response.items);

                    let items_cart = response.items.map(item => {
                        return {
                            id: item.id,
                            id_teams: item.id_teams,
                        };
                    });

                    let precio_venta;
                    
                    if (Descuento) {
                        precio_venta = totaldescuento;
                    } else {
                        precio_venta = total;
                    }
                    const fechaClick = new Date();
                    rutInput = $('#inputRutCliente').val();
                    
                    let datosVenta = {
                        'items_cart' : items_cart,
                        'precio_venta': precio_venta,
                        'timestamp': fechaClick.toISOString(),
                        'rut_Cliente':rutInput,
                    };
                    
                    console.log('Datos enviados a la vista:', datosVenta);
                    
                    $.ajax({
                        url: VentaUrl,
                        type: 'POST',
                        data: JSON.stringify(datosVenta),
                        contentType: 'application/json',
                        headers: {
                            'X-CSRFToken': csrfToken
                        },
                        success: function (response) {
                            console.log('INGRESO ÉXITO:', response);
                        },
                        error: function (error) {
                            console.error('Ocurrió un error: ', error);
                        }
                    });
                } else {
                    console.error('Error al obtener los items: ', response.message);
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


    $('#addToCartButtonn').on('click', function (e) {
        e.preventDefault();

        const fechaClick = new Date();

        const itemIdString = $('#itemId').val();
        const itemIdNumber = parseInt(itemIdString, 10);

        const userIdString = $('#userId').val();
        const userIdNumber = parseInt(userIdString, 10);

        const formData = new FormData($('#addItemCartForm')[0]);
        formData.append('timestamp', fechaClick.toISOString());

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
                    $('#row-item-' + id_item).remove();
                    
                    datosCompra(); // Actualiza el total de precios
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function () {
                alert('Ocurrió un error al intentar eliminar el item de tu carro de compra.');
            }
        });
    });

    $('#promoForm').on('submit', function (e) {
        e.preventDefault();
        const codigoPromo = $('#inputCodPromo').val();
        let validCod = validCodUrl.replace('cod', codigoPromo);

        $.ajax({
            type: 'POST',
            url: validCod,
            data: {
                'cod_pro': codigoPromo,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                if (response.success) {
                    // Mostrar el mensaje de éxito
                    $('#successMessages').text('Código ingresado correctamente');
                    $('#successMessages').css('color', 'green');
                    $('#successMessages').show();

                    Descuento = (total * response.descuentoPorcentaje) / 100;
                    totaldescuento = total - Descuento;

                    $('#containepreciodescuento').html(
                        `<div>
                            <table class="table table-bordered">
                                <tbody>
                                    <tr>
                                        <td><strong>Precio Descuento:</strong></td>
                                        <td>$ <span id="PrecioConDescuento">${totaldescuento}</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>`
                    );

                    $('#containepreciodescuento').show();

                    setTimeout(function () {
                        $('#successMessages').fadeOut('slow');
                    }, 2000);
                } else {
                    Descuento = 0;
                    totaldescuento = 0;

                    $('#successMessages').text('El código promocional no existe');
                    $('#successMessages').css('color', 'red');
                    $('#successMessages').show();

                    // Ocultar y vaciar el contenedor de descuento
                    $('#containepreciodescuento').empty();  // Vaciar el contenido
                    $('#containepreciodescuento').hide();   // Ocultar el contenedor
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

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

    // Recalcular el descuento si ya ha sido aplicado
    if (Descuento > 0) {
        totaldescuento = total - Descuento;
        document.getElementById('PrecioConDescuento').textContent = totaldescuento.toFixed(2);
    }
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
            error: function (error) {
                console.error('Ocurrió un error: ', error);
            }
        });
    });

    $('#FormAddVenta').on('submit', function (e) {
        e.preventDefault();
        // Realizar la primera solicitud para obtener los ítems
        $.ajax({
            url: UrlItems,
            type: "GET",
            success: function (response) {
                if (response.success) {

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
                        'items_cart': items_cart,
                        'precio_venta': precio_venta,
                        'timestamp': fechaClick.toISOString(),
                        'rut_Cliente': rutInput,
                    };

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
            error: function (error) {
                console.error('Ocurrió un error: ', error);
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

                    // Verificar si el mensaje "no hay items" está presente y eliminarlo
                    if ($('#noItemsMessage').length) {
                        $('#noItemsMessage').remove();
                    }

                    setTimeout(function () {
                        $('#successMessage').fadeOut('slow');
                    }, 2000);

                    $('#cardsContainer').append(
                        `<div class="cards m-2">
                            <p class="card-header" style="text-align: center;">${response.item.name}</p>
                            <hr>
                            <div class="card-body d-flex" id="Item-${response.item.Id_Registro}">
                                <div class="d-grid gap-2 m-2" style="width: 50%;">
                                <img src="${response.item.img_Team}" width="100%">
                                    <button class="btn btn-primary delete-item" type="button" data-id="${response.item.Id_Registro}">Quitar</button>
                                </div>
                                <div class="p-2" style="width: 50%;">
                                    <p><strong>$</strong> ${response.item.precio}</p>
                                    <input type="hidden" class="precioItemCart" value="${response.item.precio}">
                                    <p><strong>Equipo:</strong> ${response.item.equipo}</p>
                                    <p><strong>Año:</strong>${response.item.year}</p>
                                    <input type="hidden" class="EquipoItemCart" value="${response.item.equipo}">
                                    <p><strong>Marca: </strong> ${response.item.marca}</p>
                                </div>
                            </div>
                        </div>`
                    )
                    datosCompra();
                    EventDeleteItemCart();

                } else {
                    alert(response.message);
                }
            },
            error: function (error) {
                console.error('Ocurrió un error: ', error);
            }
        });
    });

    $('.delete-item').on('click', function () {
        EventDeleteItemCart();
    });

    $('.precioItemCart').on('input', function () {
        datosCompra();
    });

    function EventDeleteItemCart() {
        $(document).off('click', '.delete-item').on('click', '.delete-item', function () {
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

                        // Recalcular el descuento si está aplicado
                        if (Descuento > 0) {
                            totaldescuento = total - Descuento;
                            document.getElementById('PrecioConDescuento').textContent = totaldescuento.toFixed(2);
                        }

                    } else {
                        alert('Error: ' + response.message);
                    }
                },
                error: function () {
                    alert('Ocurrió un error al intentar eliminar el item de tu carro de compra.');
                }
            });
        })
    }
});

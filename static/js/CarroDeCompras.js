// Este bloque solo debería aparecer una vez
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

$(document).ready(function () {
    console.log('jQuery de Carro de compras')
    const addItemCartUrl = $('#addItemCart-url').val()
    const deleteItemUrl = $('#delete-item-url').val()
    

    $('#addToCartButtonn').on('click', function (e) {
        e.preventDefault();

        // Obtener la fecha actual en formato correcto
        const fechaClick = new Date();
        console.log("Fecha del clic:", fechaClick);

        // Capturar los valores de los campos
        const itemIdString = $('#itemId').val();
        const itemIdNumber = parseInt(itemIdString, 10); // Convierte a número entero

        const userIdString = $('#userId').val();
        const userIdNumber = parseInt(userIdString, 10); // Convierte a número entero

        const formData = new FormData($('#addItemCartForm')[0]);
        formData.append('timestamp', fechaClick.toISOString()); // fecha en formato ISO

        // Enviar el formulario vía AJAX
        $.ajax({
            url:addItemCartUrl,
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

    $(document).off('click', '.delete-item').on('click', '.delete-item', function () {
        let id_item = $(this).data('id');
        let deleteUrl = deleteItemUrl.replace('/0', '/' + id_item);
        console.log('el id del item para eliminar ', id_item)
        console.log(deleteUrl)
        $.ajax({
            type: 'POST',
            url: deleteUrl,
            data: {
                'csrfmiddlewaretoken': csrfToken
            },

            success: function (response) {
                if (response.success) {
                    $('#Item-' + id_item).parent().remove();
                    sumarPrecios(); //función para actualizar el total
                } else {
                    alert('Error: ' + response.message);
                }
            },
            error: function () {
                alert('Ocurrrió un error al intentar eliminar el item de tu carro de compra.');
            }
        })
    });

    
});
function datosCompra() {
    const precios = document.querySelectorAll('.precioItemCart');
    const nombres = document.querySelectorAll('.EquipoItemCart');
    
    let total = 0;
    let listnombres = ''; 
    let listprecios = '';
    // Recorre todos los inputs y suma sus valores
    precios.forEach(input => {
        total += parseFloat(input.value) || 0; // Convierte a número y suma
    });

    nombres.forEach( input => {
        listnombres += input.value +  '<br>';
    });
    
    precios.forEach(input => {
        listprecios += input.value + '<br>'; // Salto de línea para HTML
    });

    console.log("Total precio: desde compra " + total);
    document.getElementById('totalPrecio').textContent = total; // Muestra el total en el DOM
    console.log('Nombres: '+ listnombres);
    document.getElementById('NombresIndividuales').innerHTML = listnombres;

    document.getElementById('PreciosIndividuales').innerHTML = listprecios;
}
// Ejecuta la función cuando se cargue la página o cada vez que se necesite recalcular
window.onload = datosCompra;
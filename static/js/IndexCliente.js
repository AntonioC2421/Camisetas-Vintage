document.addEventListener('DOMContentLoaded', () => {
    console.log('desde el JS De INDEX CLIENTE');

    const prev = document.querySelector('.carousel-control-prev'); // Seleccionamos el botón "prev"
    const next = document.querySelector('.carousel-control-next'); // Seleccionamos el botón "next"
    const slider = document.querySelector('.carousel-inner'); // Seleccionamos el contenedor de los items
    // Agregar evento al botón "prev"
    prev.addEventListener('click', () => {
        slider.scrollLeft -= 550;
    });

    // Agregar evento al botón "next"
    next.addEventListener('click', () => {
        slider.scrollLeft += 550;
    });
});

function toggleBusqueda() {
    const barraBusqueda = document.getElementById('barra_busqueda');
    if (barraBusqueda.style.display === 'none' || barraBusqueda.style.display === '') {
        barraBusqueda.style.display = 'block';
    } else {
        barraBusqueda.style.display = 'none';
    }
}

function Pedidos_Carro(){
    const btnPedidoCarro = document.getElementById('btnPedidos');
    const content = document.getElementById('ContentCarrroPedidos');
    const contentItems = document.getElementById('ContentCarro');
    const btnCarroItems = document.getElementById('btnCarro');
    btnPedidoCarro.addEventListener('click', () => {
        contentItems.style.display = 'none';
        content.style.display = 'block';
    });

    btnCarroItems.addEventListener('click', () => {
        contentItems.style.display = 'block';
        content.style.display = 'none';
    });
}
document.addEventListener('DOMContentLoaded', () => {
    console.log('desde el JS De INDEX CLIENTE');
    const prev = document.querySelector('.prev');
    const next = document.querySelector('.next');
    const slider = document.querySelector('.slider');

    prev.addEventListener('click', () => {
        slider.scrollLeft -= 300;
    });

    next.addEventListener('click', () => {
        slider.scrollLeft += 300;
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
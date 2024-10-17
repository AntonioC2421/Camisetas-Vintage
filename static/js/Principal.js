// Cerrar el offcanvas si la ventana es más grande que 993px
window.addEventListener('resize', function () {
    const offcanvas = document.getElementById('offcanvasDarkNavbar');
    if (window.innerWidth >= 993) {
        const bootstrapOffcanvas = bootstrap.Offcanvas.getInstance(offcanvas);
        if (bootstrapOffcanvas) {
            bootstrapOffcanvas.hide(); // Cerrar el offcanvas
        }
    }
});
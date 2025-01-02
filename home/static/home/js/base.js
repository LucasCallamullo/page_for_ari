// -------------------------------------------------------
// Todo referido al menu desplegable
// -------------------------------------------------------
document.addEventListener("DOMContentLoaded", function() {
    const navBtn1 = document.getElementById("button1");
    const menu = document.getElementById("menu");
    const backToTop = document.querySelector(".back-to-top"); // Declaración única

    // Alternar el estado del menú
    navBtn1.addEventListener("click", function(event) {
        event.stopPropagation();

        // Obtenemos las coordenadas del botón
        const buttonRect = navBtn1.getBoundingClientRect();

        // Colocamos el menú justo debajo del botón
        menu.style.position = "fixed"; // Hacemos que el menú esté en posición fija
        menu.style.top = (buttonRect.bottom) + "px"; // Usamos el borde inferior del botón y desplazamiento de la página
        menu.style.left = 0 + "px"; // Alineamos el menú con el botón a la izquierda

        // Aseguramos que el menú tenga un z-index alto para que esté por encima de otros elementos
        menu.style.zIndex = "9999"; // Asignamos un z-index alto

        navBtn1.classList.toggle("open");
        menu.classList.toggle("open");
    });

    // Cerrar el menú si se hace clic fuera de él
    document.addEventListener("click", function(event) {
        const isClickInsideMenu = menu.contains(event.target) || navBtn1.contains(event.target);
        if (!isClickInsideMenu) {
            navBtn1.classList.remove("open");
            menu.classList.remove("open");
        }
    });

    // Control de visibilidad del botón "Back to Top"
    window.addEventListener("scroll", () => {
        // Mostrar el botón solo si se ha hecho scroll hacia abajo
        if (window.scrollY > 70) {
            backToTop.style.display = "block"; // Muestra el botón
            backToTop.classList.add("visible");
        } else {
            backToTop.classList.remove("visible");
            backToTop.style.display = "none"; // Oculta el botón cuando no se hace scroll
        }

        // El menú se moverá con el scroll
        if (menu.classList.contains("open")) {
            const buttonRect = navBtn1.getBoundingClientRect();
            menu.style.top = (buttonRect.bottom) + "px"; // Actualiza la posición mientras se hace scroll
        }
    });
});
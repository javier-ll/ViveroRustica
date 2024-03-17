window.addEventListener('DOMContentLoaded', function() {
    //Color de fondos y fondo del header
    var fondos = document.getElementById("colorFondos").innerText;
    var inicio= document.getElementById("Inicio");
    var contenedor_imagen_frase = document.querySelector(".contenedor-imagen-frase");
    var carrusell = document.querySelector(".Carrusel");
    var productos = document.getElementById("Productos");
    var quienes_somos = document.getElementById("Quienes_somos");
    var contacto = document.getElementById("Contacto");
    inicio.style.backgroundColor = fondos;
    contenedor_imagen_frase.style.backgroundColor = fondos;
    carrusell.style.backgroundColor = fondos;
    productos.style.backgroundColor = fondos;
    quienes_somos.style.backgroundColor = fondos;
    contacto.style.backgroundColor = fondos;
    var fondo_header = document.getElementById("fondo_header").innerText;
    var headerr = document.querySelector('header');
    headerr.style.backgroundColor = fondo_header;
    //Texto header
    var header_texto = document.getElementById("header_texto_botones").innerText;
    //Color hover
    var hover_header = document.getElementById("hover_header").innerText;
    var hover_carrusel = document.getElementById("hover_carrusel").innerText;
    var hover_productos = document.getElementById("hover_productos").innerText;
    var hover_redes = document.getElementById("hover_redes").innerText;
    var nav_header = document.querySelectorAll("header nav a");
    nav_header.forEach(function(enlace) {
        enlace.style.color = header_texto;
        enlace.addEventListener("mouseover", function() {
            this.style.backgroundColor = hover_header;
        });
        enlace.addEventListener("mouseout", function() {
            this.style.backgroundColor = fondo_header; // Restaura el color original del enlace al dejar de hacer hover
        });
    });
    var nav_carrusel = document.getElementsByClassName("m-btn");
    for (var i = 0; i < nav_carrusel.length; i++) {
        nav_carrusel[i].style.border = `2px solid ${hover_carrusel}`;
        nav_carrusel[i].addEventListener("mouseover", function() {
            this.style.backgroundColor = hover_carrusel;
        });
        nav_carrusel[i].addEventListener("mouseout", function() {
            this.style.backgroundColor = ""; // Restaura el color original del enlace al dejar de hacer hover
        });
    }
    var bordes_carrusel = document.querySelectorAll(".Carrusel .nav-auto div");
    // Iterar sobre cada borde seleccionado y modificar su estilo
    bordes_carrusel.forEach(function(borde) {
        // Modificar los estilos del borde
        borde.style.border = `2px solid ${hover_carrusel}`;
    });
    var producto_hover = document.querySelectorAll(".products-container .product");
    for (var i = 0; i < producto_hover.length; i++) {
        producto_hover[i].style.outline=`.1rem solid ${hover_productos}`;
        producto_hover[i].addEventListener("mouseover", function() {
            this.style.outline=`.2rem solid ${hover_productos}`;
        });
        producto_hover[i].addEventListener("mouseout", function() {
            this.style.outline =`.1rem solid ${hover_productos}`; // Restaura el color original del enlace al dejar de hacer hover
        });
    }

    // Obtener el color del pie de página
    var footer_texto = document.getElementById("footer_texto").innerText;

    // Seleccionar todos los elementos con la clase "redes2"
    var elementos = document.querySelectorAll(".redes2");

    // Iterar sobre cada elemento y aplicar estilos
    elementos.forEach(function(elemento) {
        // Obtener el ícono y el enlace dentro de este elemento
        var icono = elemento.querySelector("i");
        var enlace = elemento.querySelector("a");

        // Aplicar estilo de color del pie de página
        elemento.style.color = footer_texto;

        // Si hay un ícono, aplicar estilo de color del pie de página
        if (icono) {
            icono.style.color = footer_texto;
        }

        // Si hay un enlace, aplicar estilo de color del pie de página
        if (enlace) {
            enlace.style.color = footer_texto;

            // Agregar eventos mouseover y mouseout al enlace
            enlace.addEventListener("mouseover", function() {
                enlace.style.color = hover_redes;
            });

            enlace.addEventListener("mouseout", function() {
                enlace.style.color = footer_texto;
            });
        }

        // Agregar eventos mouseover y mouseout al elemento
        elemento.addEventListener("mouseover", function() {
            elemento.style.color = hover_redes;
            if (icono) {
                icono.style.color = hover_redes;
            }
        });

        elemento.addEventListener("mouseout", function() {
            elemento.style.color = footer_texto;
            if (icono) {
                icono.style.color = footer_texto;
            }
        });
    });
    var face_ins = document.querySelectorAll(".faceins");
    face_ins.forEach(function(facein) {
        facein.style.color = footer_texto;
        facein.addEventListener("mouseover", function() {
            facein.style.color = hover_redes;
        });

        facein.addEventListener("mouseout", function() {
            facein.style.color = footer_texto;
        });
    });
    //Color secciones
    var fondo_secciones = document.getElementById("fondo_secciones").innerText;
    var fondo_producto = document.getElementById("titulo_productos");
    var fondo_quienes = document.querySelector("#Quienes_somos h1");
    var fondo_contacto = document.getElementById("titulo_contacto");
    fondo_producto.style.backgroundColor = fondo_secciones;
    fondo_quienes.style.backgroundColor = fondo_secciones;
    fondo_contacto.style.backgroundColor = fondo_secciones;
    //Color texto de frase principal
    var frase_principal = document.getElementById("frase_principal").innerText;
    var texto_principal = document.querySelector(".frase");
    texto_principal.style.color = frase_principal;
    //Color de fondo de texto y de la fuente del carrusel
    var fondo_carrusel = document.getElementById("carrusel_fondo_texto").innerText;
    var texto_carrusel = document.getElementById("carrusel_texto").innerText;
    var fondo_carrusel_texto = document.querySelectorAll(".Carrusel .texto");
    for (var i = 0; i < fondo_carrusel_texto.length; i++) {
        fondo_carrusel_texto[i].style.backgroundColor=fondo_carrusel;
        fondo_carrusel_texto[i].style.color=texto_carrusel;
    }
    //Color de texto de los titulos
    var texto_titulos = document.getElementById("titulos_secciones").innerText;
    fondo_producto.style.color = texto_titulos;
    fondo_quienes.style.color = texto_titulos;
    fondo_contacto.style.color = texto_titulos;
    //Color de texto de los productos, el texto de quienes y el formulario
    var texto_detalles = document.getElementById("productos_quienes_form_texto_detalles").innerText;
    var nombre_producto = document.querySelectorAll("#Productos h3");
    var precio_producto = document.querySelectorAll("#Productos .price");
    var simbolo_producto = document.querySelectorAll("#Productos .fa-times");
    var parrafo_producto = document.querySelectorAll("#Productos p");
    //Color de fondo de productos y de su vista previa de productos
    var fondo_productos = document.querySelectorAll("#Productos .products-container .product");
    var fondo_previa_producto = document.querySelectorAll("#Productos .products-preview .preview");
    var fondo_previa = document.getElementById("productos_fondo").innerText;
    for (var i = 0; i < nombre_producto.length; i++) {
        nombre_producto[i].style.color = texto_detalles;
        precio_producto[i].style.color = texto_detalles;
        try {
            // Intenta acceder al estilo del elemento
            simbolo_producto[i].style.color = texto_detalles;
            parrafo_producto[i].style.color = texto_detalles;
            fondo_previa_producto[i].style.backgroundColor = fondo_previa;
            fondo_productos[i].style.backgroundColor = fondo_previa;
        } catch (error) {
            // Maneja la excepción si el elemento no está definido
        }
    }
    //Color de botón de formulario y del texto de éste
    var boton_form = document.getElementById("form_boton").innerText;
    var boton_texto = document.getElementById("form_texto_boton").innerText;
    var boton = document.querySelector(".btn-primary");
    boton.style.backgroundColor = boton_form;
    boton.style.color = boton_texto;
});
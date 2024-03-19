// Header
$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 0) {
            $('header').addClass('header2');
        } else {
            $('header').removeClass('header2');
        }
    });
});

// Botones Header
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Carrusel
document.addEventListener('DOMContentLoaded', function() {
    var maxImages = document.querySelectorAll('.slide .st').length; // Obtener la cantidad de imágenes dinámicamente
    var counter = 1;
    var intervalTime = 4000;
    var intervalId;

    function autoNavigation() {
        counter++;
        if (counter > maxImages) {
            counter = 1;
        }
        navigate(counter, false); // Llamamos a navigate con isManual = false
    }

    function manualNavigation(imageNumber) {
        clearInterval(intervalId); // Detener la navegación automática
        navigate(imageNumber, true); // Llamamos a navigate con isManual = true
        startAutoNavigation(); // Reiniciar la navegación automática desde la imagen seleccionada manualmente
    }

    function startAutoNavigation() {
        clearInterval(intervalId); // Limpiar el intervalo existente antes de iniciar uno nuevo
        intervalId = setInterval(autoNavigation, intervalTime);
    }

    function navigate(imageNumber, isManual) {
        counter = imageNumber;
        var radioElement = document.getElementById('radio' + counter);
        if (radioElement) {
            radioElement.checked = true;
        } else {
            console.error("Radio element not found for counter:", counter);
        }
        if (!isManual) { // Verificamos si la navegación es manual
            startAutoNavigation(); // Reiniciar la navegación automática si no es manual
        }
    }

    document.getElementById('radio1').checked = true;
    startAutoNavigation();

    document.querySelectorAll('.m-btn').forEach(function(btn, index) {
        btn.addEventListener('click', function() {
            manualNavigation(index + 1);
        });
    });

    document.querySelectorAll('input[type="radio"]').forEach(function(radio) {
        radio.addEventListener('click', function() {
            clearInterval(intervalId);
            startAutoNavigation();
        });
    });
});


window.addEventListener('DOMContentLoaded', function() {
    var hover_carrusel = document.getElementById("hover_carrusel").innerText;
    var imagenesCantidad = document.querySelectorAll('.slide .st').length;
    var styles = '';

    for (var i = 1; i <= imagenesCantidad; i++) {
        var marginLeft = (i - 1) * -20; // Ajusta esto según tus necesidades

        styles += `
            #radio${i}:checked ~ .first {
                margin-left: ${marginLeft}%;
            }
        `;

        // Opcional: estilos para los botones de navegación automática
         styles += `
             #radio${i}:checked ~ .nav-auto .a-b${i} {
                 background-color: ${hover_carrusel};
             }
        `;
    }

    var styleElement = document.createElement('style');
    styleElement.textContent = styles;
    document.head.appendChild(styleElement);
});

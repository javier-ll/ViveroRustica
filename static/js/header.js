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
var counter = 1;
var maxImages = 3;
//var maxImages = document.querySelectorAll('.slide .st').length; // Obtener la cantidad de imágenes dinámicamente
var intervalTime = 4000;
var isManual = false;
var intervalId;

function autoNavigation(manualCounter) {
    if (manualCounter !== null) {
        counter = manualCounter;
    } else {
        counter++;
        if (counter > maxImages) {
            counter = 1;
        }
    }
    document.getElementById('radio' + counter).checked = true;
}

function manualNavigation(imageNumber) {
    isManual = true;
    manualCounter = imageNumber; // Actualiza el contador manual
    counter = imageNumber; // Actualiza el contador principal
    clearInterval(intervalId); // Detiene la navegación automática al hacer clic en un botón manual
    document.getElementById('radio' + counter).checked = true;
}

function startAutoNavigation() {
    intervalId = setInterval(autoNavigation, intervalTime);
}

// Iniciar la navegación automática al cargar la página
startAutoNavigation();

// Event listener para los botones de navegación manual
document.querySelectorAll('.m-btn').forEach(function(btn, index) {
    btn.addEventListener('click', function() {
        manualNavigation(index + 1);
    });
});

// Event listener para restablecer el modo automático cuando se selecciona una imagen manualmente
document.querySelectorAll('input[type="radio"]').forEach(function(radio) {
    radio.addEventListener('click', function() {
        isManual = false;
        startAutoNavigation(); // Restablecer la navegación automática después de seleccionar una imagen manualmente
    });
});
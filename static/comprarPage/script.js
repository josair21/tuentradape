ScrollReveal().reveal('.header', { delay: 1000 });
ScrollReveal().reveal('#tituloPrincipal', { delay: 1000 });
ScrollReveal().reveal('#subTitulo1', { delay: 1000 });
ScrollReveal().reveal('.horizontal-line', { delay: 1000 });
ScrollReveal().reveal('#containerEntradas', { delay: 1000 });


document.getElementById("comprarForm").addEventListener("submit", function (event) {
    event.preventDefault();  // Evita que la página se refresque al enviar el formulario

    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();

    xhr.open("POST", "{% url 'comprarPage' %}");  // Reemplaza "{% url 'comprarPage' %}" con la URL correcta
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

    xhr.onload = function () {
        if (xhr.status === 200) {
            // La solicitud fue exitosa
            console.log("Solicitud POST enviada con éxito");
            // Realiza cualquier acción adicional o actualiza partes específicas de la página
        } else {
            // La solicitud no fue exitosa
            console.error("Error al enviar la solicitud POST");
        }
    };

    xhr.onerror = function () {
        // Manejar errores de red
        console.error("Error de red al enviar la solicitud POST");
    };

    xhr.send(formData);
});

function disminuirFila(fila) {
    var element = document.getElementById(fila);
    var numero = parseInt(element.innerText);
    if (numero > 0) numero--;
    element.innerText = numero.toString().padStart(2, '0');
    montoTotal();
}

function aumentarFila(fila) {
    var element = document.getElementById(fila);
    var numero = parseInt(element.innerText);
    if (numero < 99) numero++;
    element.innerText = numero.toString().padStart(2, '0');
    montoTotal();
}

function montoTotal() {
    var total = 0;
    total = parseInt(document.getElementById("entradasFila1").innerText) * parseInt(document.getElementById("montoFila1").innerText.substring(4)) +
        parseInt(document.getElementById("entradasFila2").innerText) * parseInt(document.getElementById("montoFila2").innerText.substring(4)) +
        parseInt(document.getElementById("entradasFila3").innerText) * parseInt(document.getElementById("montoFila3").innerText.substring(4)) +
        parseInt(document.getElementById("entradasFila4").innerText) * parseInt(document.getElementById("montoFila4").innerText.substring(4));
    var element = document.getElementById("montoTotal");
    element.innerText = "S/. " + total.toString();
    var element2 = document.getElementById("monto");
    element2.value = total

    /*if (total > 0) {
        var contenedor = document.getElementById("regionObligatoria")
        contenedor.hidden = false;
    }
    else {
        var contenedor = document.getElementById("regionObligatoria")
        contenedor.hidden = true;
    }*/
}

function soloNumeros(event) {
    var charCode = event.which ? event.which : event.keyCode;
    if (charCode < 48 || charCode > 57) {
        event.preventDefault();
        return false;
    }
    return true;
}

function medioPagoElegido(checkbox) {
    var element;
    switch (checkbox) {
        case "yapeCheckBox":
            element = document.getElementById("plinCheckBox");
            element.checked = false;
            element = document.getElementById("bcpCheckBox");
            element.checked = false;
            break;

        case "plinCheckBox":
            var element = document.getElementById("yapeCheckBox");
            element.checked = false;
            element = document.getElementById("bcpCheckBox");
            element.checked = false;
            break;

        case "bcpCheckBox":
            var element = document.getElementById("plinCheckBox");
            element.checked = false;
            element = document.getElementById("yapeCheckBox");
            element.checked = false;
            break;
    }
}

function enviarPost() {
    var celularValue = document.getElementById("celular").value;
    var codigoValue = document.getElementById("codigo").value;
    var formData = new FormData();
    formData.append("celular", celularValue);
    formData.append("codigo", codigoValue);
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch(comprarPageUrl, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData,

    })
        .then(response => {
            if (response.ok) {
                // La solicitud fue exitosa
                console.log("Solicitud POST enviada con éxito");
                // Realiza cualquier acción adicional o redirige a otra página
            } else {
                // La solicitud no fue exitosa
                console.error("Error al enviar la solicitud POST");
            }
        })
        .catch(error => {
            // Manejar errores
            console.error(error);
        });
}
function setBotonValue(value) {
    document.getElementById('boton').value = value;
}

function validarCelular(event) {
    var celularInput = document.getElementById("celular");
    var celularValue = celularInput.value.trim();
    if (celularValue.length !== 9) {
        alert("El número de celular debe tener 9 dígitos.");
        return false; // Evita que el formulario se envíe
    }
    event.preventDefault();
    var formData = new FormData(celularInput);
    fetch(form.action, {
        method: form.method,
        body: formData
    })
        .then(response => {
            if (response.ok) {
                console.log("Solicitud POST enviada con éxito");
                // Realiza cualquier acción adicional o redirige a otra página
                document.getElementById('botonVerificar').disabled = false;
            } else {
                console.error("Error al enviar la solicitud POST");
            }
        })
        .catch(error => {
            console.error(error);
        });

}
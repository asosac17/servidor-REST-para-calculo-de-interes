document.getElementById('interesForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

    // Obtener los valores del formulario
    const principal = parseFloat(document.getElementById('principal').value);
    const tasa_anual = parseFloat(document.getElementById('tasa_anual').value) / 100; // Convertir a decimal
    const periodos = parseFloat(document.getElementById('periodos').value);

    // Crear el objeto con los datos
    const data = {
        principal: principal,
        tasa_anual: tasa_anual,
        periodos: periodos
    };

    // Enviar la solicitud POST al servidor
    fetch('http://localhost:8080/calcular-intereses', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Mostrar el resultado en la página
        const resultadoDiv = document.getElementById('resultado');
        if (result.error) {
            resultadoDiv.textContent = `Error: ${result.error}`;
        } else {
            resultadoDiv.innerHTML = `
                <strong>Monto Total:</strong> ${result.monto_total.toFixed(2)}<br>
                <strong>Detalles:</strong><br>
                - Principal: ${result.detalles.principal}<br>
                - Tasa Anual: ${(result.detalles.tasa_anual * 100).toFixed(2)}%<br>
                - Periodos: ${result.detalles.periodos}
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultado').textContent = 'Hubo un error al calcular el interés.';
    });

    console.log('Datos enviados:', data);
});

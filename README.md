## **Documentación del Proyecto: Calculadora de Interés Compuesto**

### **Tabla de Contenidos**
1. [Descripción](#descripción)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Requisitos](#requisitos)
4. [Instalación y ejecución](#instalación-y-ejecución)
5. [Uso](#uso)
   - [Endpoints](#endpoints)
   - [Ejemplos de Solicitudes](#ejemplos-de-solicitudes)

---

## **Descripción**
Este proyecto es un servidor REST desarrollado en Python que permite calcular el interés compuesto de una deuda. El servidor acepta solicitudes HTTP POST y devuelve el monto total después de aplicar el interés compuesto.

El servidor está diseñado para ser simple y fácil de usar, ideal para aplicaciones que necesiten realizar cálculos financieros básicos.

---

## **Tecnologías Utilizadas**

- **Frontend**:
  - HTML
  - CSS
  - JavaScript
- **Backend**:
  - Python (http.server) 

---

## **Requisitos**
Para ejecutar este proyecto, necesitas:

- **Python 3.x**: El servidor está desarrollado en Python.
- **Módulos de la biblioteca estándar de Python**: No se requieren dependencias externas, ya que el servidor utiliza los módulos `http.server` y `json`.

---

## **Instalación y ejecución**
### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Ejecutar el servidor Python:

Navega a la carpeta del proyecto y ejecuta el servidor Python:

```bash
python servidor.py
```
El servidor estará disponible en http://localhost:8080.

### 3. Abrir la interfaz web:

Abre el archivo index.html en tu navegador.

### 4. Usar la calculadora

Ingresa los valores en los campos del formulario:

- **Principal**: El monto inicial de la inversión.
- **Tasa Anual**: La tasa de interés anual (en porcentaje).
- **Periodos**: El número de años.

Haz clic en "Calcular" para ver el monto total y los detalles del cálculo.


## **Uso**
## **Endponits**
El servidor tiene un único endpoint:

- **POST /calcular-intereses**
  - **Descripción:** Calcula el interés compuesto.
  - **Parámetros (JSON):**
    - `principal`: Monto principal de la deuda.
    - `tasa_anual`: Tasa de interés anual (en decimal, por ejemplo, `0.05` para 5%).
    - `periodos`: Tiempo en años.

- **Respuesta (JSON):**
  ```json
  {
      "monto_total": 1157.63,
      "detalles": {
          "principal": 1000,
          "tasa_anual": 0.05,
          "periodos": 3
      }
  }

---

## **Ejemplos de Solicitudes**

### **Ejemplo 1: Solicitud con `curl`**
```bash
curl -X POST http://localhost:8080/calcular-intereses \
-H "Content-Type: application/json" \
-d '{"principal": 1000, "tasa_anual": 0.05, "periodos": 3}'
```

- **Respuesta (JSON):**
  ```json
  {
      "monto_total": 1157.63,
      "detalles": {
          "principal": 1000,
          "tasa_anual": 0.05,
          "periodos": 3
      }
  }

### **Ejemplo 2: Solicitud desde JavaScript (Fetch API)**

```javascript
Copy
fetch('http://localhost:8080/calcular-intereses', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        principal: 2000,
        tasa_anual: 0.1,
        periodos: 5
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

- **Respuesta (JSON):**
  ```json
    {
        "monto_total": 3221.02,
        "detalles": {
            "principal": 2000,
            "tasa_anual": 0.1,
            "periodos": 5
        }
    }

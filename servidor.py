from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Responder a la solicitud de preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # Permitir cualquier origen
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')  # Métodos permitidos
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Encabezados permitidos
        self.end_headers()

    def do_POST(self):
        if self.path == '/calcular-intereses':
            try:
                # Obtener la longitud del cuerpo de la solicitud
                content_length = int(self.headers['Content-Length'])
                print("Longitud del contenido:", content_length)  # Log de depuración

                # Leer el cuerpo de la solicitud
                post_data = self.rfile.read(content_length)
                print("Datos recibidos (crudos):", post_data)  # Log de depuración

                # Convertir el cuerpo de la solicitud a JSON
                data = json.loads(post_data.decode('utf-8'))
                print("Datos recibidos (JSON):", data)  # Log de depuración

                # Validar que los datos necesarios estén presentes
                required_fields = ['principal', 'tasa_anual', 'periodos']  # Eliminamos 'frecuencia'
                if not all(field in data for field in required_fields):
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')  # CORS
                    self.end_headers()
                    response = {'error': f'Faltan datos necesarios: {required_fields}'}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return

                # Obtener los valores del JSON
                principal = float(data['principal'])
                tasa_anual = float(data['tasa_anual'])
                periodos = float(data['periodos'])

                # Validar que los valores sean positivos
                if principal <= 0 or tasa_anual <= 0 or periodos <= 0:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')  # CORS
                    self.end_headers()
                    response = {'error': 'Todos los valores deben ser positivos'}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return

                # Calcular el interés compuesto (sin frecuencia)
                monto_total = principal * (1 + tasa_anual) ** periodos

                # Preparar la respuesta
                response = {
                    'monto_total': monto_total,
                    'detalles': {
                        'principal': principal,
                        'tasa_anual': tasa_anual,
                        'periodos': periodos
                    }
                }

                # Enviar respuesta
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')  # CORS
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))

            except Exception as e:
                print("Error en el servidor:", str(e))  # Log de depuración
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')  # CORS
                self.end_headers()
                response = {'error': f'Error interno del servidor: {str(e)}'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # CORS
            self.end_headers()
            response = {'error': 'Ruta no encontrada'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor iniciado en el puerto {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
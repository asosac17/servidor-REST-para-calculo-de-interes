import json
from io import BytesIO

class SimpleHTTPRequestHandler:
    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server

    def handle_request(self, environ, start_response):
        try:
            # Configurar los encabezados CORS
            headers = [
                ('Access-Control-Allow-Origin', '*'),  # Permitir cualquier origen
                ('Access-Control-Allow-Methods', 'POST, OPTIONS'),  # Métodos permitidos
                ('Access-Control-Allow-Headers', 'Content-Type'),  # Encabezados permitidos
            ]

            # Manejar solicitudes OPTIONS (preflight)
            if environ['REQUEST_METHOD'] == 'OPTIONS':
                start_response('204 No Content', headers)
                return []

            # Obtener la longitud del cuerpo de la solicitud
            content_length = int(environ.get('CONTENT_LENGTH', 0))
            post_data = environ['wsgi.input'].read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            # Validar que los datos necesarios estén presentes
            required_fields = ['principal', 'tasa_anual', 'periodos']
            if not all(field in data for field in required_fields):
                start_response('400 Bad Request', headers + [('Content-Type', 'application/json')])
                return [json.dumps({'error': f'Faltan datos necesarios: {required_fields}'}).encode('utf-8')]

            # Calcular el interés compuesto
            principal = float(data['principal'])
            tasa_anual = float(data['tasa_anual'])
            periodos = float(data['periodos'])
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

            # Devolver la respuesta con los encabezados CORS
            start_response('200 OK', headers + [('Content-Type', 'application/json')])
            return [json.dumps(response).encode('utf-8')]

        except json.JSONDecodeError:
            start_response('400 Bad Request', headers + [('Content-Type', 'application/json')])
            return [json.dumps({'error': 'JSON inválido'}).encode('utf-8')]

        except Exception as e:
            start_response('500 Internal Server Error', headers + [('Content-Type', 'application/json')])
            return [json.dumps({'error': f'Error interno del servidor: {str(e)}'}).encode('utf-8')]
import boto3
from datetime import datetime

# Crear una sesión de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Definir la tabla
table = dynamodb.Table('pipeline-config')

# Función para registrar un log
def registrar_log(id_pipeline, status):
    try:
        # Obtener el timestamp actual
        timestamp = datetime.utcnow().isoformat()

        # Insertar el log en DynamoDB
        response = table.put_item(
            Item={
                'id_pipeline': id_pipeline,  # La clave primaria
                'status': status,             # El estado del log
                'timestamp': timestamp        # Timestamp del log
            }
        )
        print(f"Log registrado: {response}")
    except Exception as e:
        print(f"Error al registrar log: {e}")

# Ejemplo de uso de la función
id_pipeline = 'pipeline_001'
status = 'Success'
registrar_log(id_pipeline, status)
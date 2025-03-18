# PROYECTO PIPELINES DE AWS

- Configuramos el entorno local e instalamos las dependencias de python, boto3, AWS CLI, Git

# PRIMER PASO

- Subir el archivo CSV de los datos en AWS S3 (Data lake)
  Los datos son:

```
    id_cliente, nombre_cliente, plan, fecha_inicio, fecha_fin, monto
    -1, Cliente A, Plan Básico,2024-01-01,2024-12-31,25
    -2, Cliente B, Plan Premium,2024-02-01,2024-12-31,50
```

# SEGUNDO PASO

-En AWS GLUE se crea un Crawler y se crea una base de datos
-se le da los permisos de IA de: AdministratorAccess / AmazonS3FullAccess / AWSGlueConsoleFullAccess

- Se busca el archivo subido con el url (Clientes.csv)
- ponemos crear Crawler y luego ejecutamos hasta que el crawler creado se este ejecutando
- Vamos a Jobs de AWS Glue creamos una catalogo de datos, con la conexión s3 en Sources(Fuentes) y en Targets(objetivo).
  Le damos el url de s3 para buscar el archivo que vamos a necesitar y le asignamos el formato que tiene el archivo que en este caso es CSV; le asignamos un nombre al catalogo y guardamos y luego ejecutamos

# PASO TRES

En AWS Athena hacemos la consulta para ver si los datos están asociados

```
SELECT * FROM clientes.csv
```

Los datos tendrían que visualizarse en la ventana si esta todo bien

# TERCER PASO

- Vamos Amazon Redshift creamos y creamos el cluster
- Creamos la base de datos y la tabla con las columnas.

```
CREATE TABLE telecom_transformed (
 id_cliente INT,
nombre_cliente VARCHAR(256),
plan VARCHAR(255),
fecha_inicio DATE,
fecha_fin DATE,
monto DECIMAL(19, 2),
monto_total DECIMAL(10, 2)
);
```

Lo ejecutamos y nos aparecerá q se ha ejecutado de manera exitosa

# CUARTO PASO Configurar DynamoDB

- Vamos a AWS DynamoDB y creamos una tabla llamada "pipeline-config" con clave primaria "id_pipeline"
- Registramos en logs en DynamoDB usando el script en python (https://github.com/Silberth90/AWS-proyectopipelines/blob/main/telecon-pipeline/scripts/dynamodb_logger.py)

# Quinto paso subir el proyecto a github

o Creamos un nuevo repositorio don de vamos a cargar los archivos del proyecto con el nombre "teleco-data-engineering-Project"
o Pasamos la estructura del proyecto

```
├── README.md
├── telecom-pipeline
	├──scripts/
		├── dynamodb_logger.py
		├── glue_etl_script.py
	├── data/
├──clientes.csv
```

## problemas que tube durante el proyecto

- En Amazon Redshift por que nunca me conectaba con la base de datos de AWS Glue y el problema era que la versión V2 no me dejaba conectar los servicios cosa que con la versión V1 conecto de forma eficaz. no se si es por el control de versiones que todavía no me dejaba darle los permisos de IA
- ya solucionado esto crea la base de datos y el usuario con los permisos
- y segui con el proyecto

# Usa la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Expone el puerto 5000 para que la aplicación Flask sea accesible desde fuera del contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación Flask cuando se inicie el contenedor
CMD ["python", "run.py"]



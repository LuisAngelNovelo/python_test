# 2019.02.19 By Servando Herrrera
# Objetivos:
#     1. Montar una API, tipicamente py flask en un puerto predefinido
#     2. El montaje debe ser al recibir un Push al repositorio asociado a la instancia
# Como:
#     1. Creando un directorio contenedor para las fuentes python
#     2. Copiando las fuentes al directorio contenedor
#     3. Instalando las dependencia declaradas por el programador en requirements.txt
#     4. Creando un cargador de la aplicación implementando gevent

# Definicion de parametros

# $1 Directorio destino
# $2 Nombre del stack virtual
# $3 Directorio de codigo fuente
# $4 clase de la app a montar
# $5 numero de puerto

# Creacion del directorio para el ambiente virtual
mkdir $1
cd $1

# Creacion del ambiente virtual
python3 -m venv $2

# TODO: Corregir tema de vigencia de componente.
#WARNING: the pyenv script is deprecated in favour of `python3.6 -m venv`
#./virtual-me.sh: línea 4: vir/bin/activate: No such file or directory

# Activacion del ambiente virtual
source  $2/bin/activate

# Obtener el código fuente
cp -pr  $3/* .

# Instalación de requerimientos
pip3 install --upgrade pip
pip3 install --verbose -r requirements.txt

# Generar el launcher
echo '# Laucher' > launcher.py
echo 'from gevent.pywsgi import WSGIServer' >> launcher.py
echo 'from ' $4 ' import app' >> launcher.py
echo '' >> launcher.py
echo 'http_server = WSGIServer(("''",' $5 '), app)' >> launcher.py
echo 'http_server.serve_forever()' >> launcher.py

# iniciamos el server

python3 launcher.py &








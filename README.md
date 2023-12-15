# Prueba_HeyHom
Se realizó una API de prueba usando Django y Django REST Framework bajo las indicaciones enviadas. 

Para hacer la prueba es necesario clonar el repositorio. 
Desde terminal:
```bash
git clone https://github.com/Joseph-Ibanez/Prueba_HeyHom.git
cd Prueba_HeyHom
```
Enseguida se debe crear un entorno virtual, éste se hará con python mediante:
```bash
python -m venv NombreDelEntornoVirtual
```
Para activar el entorno virutal, desde terminal ejecutamos:
```bash
NombreDelEntornoVirtual\Scripts\activate.bat
```
Una vez dentro del entorno virtual, ejecutamos el siguiente comando:
```bash
pip install -r requirements.txt
```
Este comando instalará todas las dependencias necesarias para ejecutar la API.
Corremos las migraciones para que al correr el servidor éstas se vean.
```bash
py manage.py migrate
```
Y finalmente corremos el proyecto mediante
```bash
py manage.py runserver
```
Visitando http://localhost:8000/api/properties tendremos la lista de propiedades.


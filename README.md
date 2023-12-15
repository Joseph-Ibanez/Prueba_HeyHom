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
py manage.py makemigrations
py manage.py migrate
```
Y finalmente corremos el proyecto mediante
```bash
py manage.py runserver
```
Visitando http://localhost:8000/api/properties tendremos la lista de propiedades.

## Ejemplos de API Requests and Responses
Para **listar todas las propiedades** en la base de datos, es necesario escribir en el navegador, 
con servidor encendido, lo siguiente:
http://localhost:8000/api/properties/listing/
Y obtendremos una respuesta del siguiente tipo
```json
[
    {
        "id": 6,
        "title": "Casa",
        "description": "Casa 2",
        "price": "100000.00",
        "location": "No sé",
        "property_type": "HOS",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 1200,
        "available": true
    },
    {
        "id": 7,
        "title": "Apartamento",
        "description": "Es un apartamento",
        "price": "100000.00",
        "location": "Pos a lado",
        "property_type": "APM",
        "bedrooms": 5,
        "bathrooms": 3,
        "square_feet": 121212,
        "available": false
    }
]
```

Para **devolver una sola propiedad**, se puede hacer mediante el siguiente Request, mediante el id que se desee:
http://localhost:8000/api/properties/id_propiedad/retrieve_property/
Usando de ejemplo el id = 6, la respuesta sería del tipo:
```json
 {
        "id": 6,
        "title": "Casa",
        "description": "Casa 2",
        "price": "100000.00",
        "location": "No sé",
        "property_type": "HOS",
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 1200,
        "available": true
  }
```
Podemos ver que aquí se llamó solo a un elemento del arreglo que llamamos en el request anterior. 

Para **crear** una nueva propiedad debemos escribir:
http://localhost:8000/api/properties/create/
Y nos arrojará en el navegador las características a rellenar para la creación de la nueva propiedad. 

Para **actualizar** una propiedad debemos de escribir:
http://localhost:8000/api/properties/id_propiedad/update/
Donde nos aparecerán todos los campos para actualizar la propiedad terminando con un POST al final de la página. 

Por último para **eliminar** una propiedad es necesario escribir:
http://localhost:8000/api/properties/id_propiedad/delete/
Y nos aparecerá una página donde debemos de elegir **DELETE** y nos lanzará una ventana donde confirmaremos que queremos eliminar esa propiedad. 
(Aquí el único problema es que no he logrado que en la ventana aparezcan los campos de la propiedad a eliminar, por lo que debemos elegir cuidadosamente el id al momento de escribir el url).

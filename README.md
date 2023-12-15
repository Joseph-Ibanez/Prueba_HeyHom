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

## Ejemplos de API Requests and Responses
Un ejemplo de request (estando en el entorno virtual), se da mediante:
```bash
curl http://localhost:8000/api/properties/
```
Y obtendremos una respuesta del siguiente tipo
```json
[
  {
    "id": 1,
    "title": "Departamento bonito",
    "description": "Un departamente hermoso y espacioso en un lugar cotizado",
    "price": 160000.00,
    "location": "Centro de la ciudad",
    "property_type": "apartment",
    "bedrooms": 3,
    "bathrooms": 2,
    "square_feet": 1000,
    "available": true
  },
]
```

Para devolver una sola propiedad, se puede hacer mediante el siguiente Request, modificando el 1 por el número de propiedad que se desee:
```bash
curl http://localhost:8000/api/properties/1/
```
Y la respuesta sería del tipo:
```json
 {
    "id": 1,
    "title": "Departamento bonito",
    "description": "Un departamente hermoso y espacioso en un lugar cotizado",
    "price": 160000.00,
    "location": "Centro de la ciudad",
    "property_type": "apartment",
    "bedrooms": 3,
    "bathrooms": 2,
    "square_feet": 1000,
    "available": true
  }
```
Podemos ver que aquí se llamó solo a un elemento del arreglo que llamamos en el request anterior. 

Mediante una petición **POST** podemos crear una nueva propiedad:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "Nueva Casa", "description": "Casa nueva con arquitectura moderna", "price": 250000.00, "location": "Afueras de la ciudad", "property_type": "HOS", "bedrooms": 4, "bathrooms": 3, "square_feet": 2000, "available": true}' http://localhost:8000/api/properties/
```
Y obtenemos una respuesta del tipo:
```json
{
    "id": 2,
    "title": "Nueva Casa",
    "description": "Casa nueva con arquitectura moderna",
    "price": 250000.00,
    "location": "Afueras de la ciudad",
    "property_type": "HOS",
    "bedrooms": 4,
    "bathrooms": 3,
    "square_feet": 2000,
    "available": true
}
```

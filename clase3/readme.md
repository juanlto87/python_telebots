# Clase 3 – APIs y Consumo de Datos en Python

## 🎯 Objetivo:
Aprender a consumir APIs públicas en Python, manipular datos JSON y mostrar información de forma útil en consola.

---

## 📋 Instrucciones:

1. Crea una carpeta `clase_3` y dentro un archivo `nombre_apellido.py`.
2. Asegúrate de tener instalada la librería `requests` (`pip install requests`).
3. Realiza los ejercicios propuestos a continuación.
4. Guarda los cambios, haz commit y push a tu fork del repositorio.
5. Crea un Pull Request con el título: `"Clase 3 - TuNombre TuApellido"`
---

## 📌 Requisitos:

1. Instalar virtualenv: pip install virtualenv​
2. Crear entorno virtual: python -m venv venv​   virtual enviroment
3. Activar entorno:​ en la carpeta raiz de todas las clases 
  - Mac source  venv\bin\activate
  - Windows: venv\Scripts\activate 
4. Instalar Flask: pip install flask​
5. Crear una carpeta con nombre_apellido  en la carpeta clase3
6. cd clase3/nombre_apellido
5. Ejecutar app: python app.py
pip freeze > requirements.txt
pip3 install -r requirements.txt 
deactivate
---

## 🧪 Ejercicio 1 – Explorando la PokéAPI

Utiliza la [PokeAPI](https://pokeapi.co) para mostrar información de un Pokémon ingresado por el usuario.

### Requisitos:
- Muestra los datos de 9 pokemons con paginado
  (Para evitar un renderizado lento de la pagina traer de 9 en 9 por cada pagina los datos de cada pokemon)
- Solicita al usuario el nombre de un Pokémon.
- Usa la API para obtener al menos unos 10 datos relevantes de la api por cada pokemon:
  - Su número en la Pokédex.
  - Sus tipos (fire, water, etc.).
  - Una imagen (url del sprite).
  - etc...

---

## 🧪 Ejercicio 2 – API de chistes

Consume la API pública: https://official-joke-api.appspot.com/jokes/random

### Requisitos:
- Esto lo pueden hacer en consola o con flask
- Muestra el `setup` y `punchline` del chiste.
- El programa debe ejecutarse cada vez que el usuario presione Enter.
- Finaliza si el usuario escribe “salir”.

---

## 💡 Recomendaciones:
- Usa `try-except` para manejar errores de red o errores de API.
- Imprime los resultados de forma clara y amigable.
- Puedes probar con otras APIs públicas si deseas practicar más.

---

## ✅ Bonus:
- Crea una función que obtenga 3 Pokémon al azar y muestre sus nombres y tipos.

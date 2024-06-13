
Tabla de Contenido
================
* [Chatbot-Cocina](#Chatbot-Cocina)
  * [Descripción](#descripción)
  * [Librerias](#Librerias)
  * [Libros](#Libros)
  * [Pruebas](#Pruebas)
  * [Streamlit](#streamlit)
  * [Discusión](#discusión)
  * [Creditos](#creditos)
  * [Licensing](#licensing)
  * [Autor](#Autor)

# Chatbot-Cocina
Este es un proyecto de desarrollo de un Asistente de Cocina en forma de Chatbot.

## Descripción
This is the continuation of a project developed at the [CRI](https://cri-paris.org/en) Université de Paris in the second semester of the Master of Digital Science( May 2021), within the [Challenge Hub](https://master.cri-paris.org/en/challenge-hub) program.
It is a way of presenting the information regarding what has happened with the vaccination campaign in Italy through the streamlit tool, which allows the user to interact with the information in a friendly and close way.
See the previous [analysis](https://github.com/Eli-2020/Italy_vaccination_campaign).

## Librerias 

If you use pip, you can install: 

   * pip install langchain=0.2.3
   * pip install langchain-community=0.2.4
   * pip install langchain-cohere=0.1.7
   * pip install chromadb=0.5.0
   * pip install pypdf=4.2.0
   * pip install streamlit=1.35.0
    
## Libros

Para este proyecto se descargaron ocho libros via internet. 

Cuatro libros fueron financiados con estidades del estado y son de circulación gratuita.
Un libro fue financiado por una organización internacional y es de circulación gratuita. 
Un libro fue financiado por la cámara de Comercio de Bogotá y es de circulación gratuita.
Dos son recetarios de empresas comerciales que buscan promocionar un producto no las recetas y son de circulación gratuita.

## Pruebas

Se hacen pruebas para solucionar problemas como los siguientes:
 * Solucionar problemas de sesgo de genero, se mejoro mediante el prompt la posible pregunta de mujeres chef. 
 * Recetas que incluyan alcohol en sus ingredientes que deben incluir una advertencia para menores de edad y su consumo en exceso.
 * Recetas que incluyan animales en peligro de extinción dentro de sus ingredientes. 

## Streamlit
Para correr el archivo en streamlit debe descargar el arhivo app.py
se recomienda usar vsc con python >3.10 y en la terminal escribir
streamlit run mas la ruta de la ubicación del archivo app.py en su computador 

## Discusión
- Se plantea una discusión entorno al idioma del chatbot, se decide desde el principio tenerlo habilitado en idioma español y en caso de tener pregutnas en otro idioma se debe contestar en español, la razón de esta decisión es porque los usuarios seran en su mayoria usuarios de habla española y la segunda es que todos los libros estan el español y no se puede asegurar que las traduciones de los ingredientes sean exactas.

## Creditos
- El proyecto fue desarrollado por **Eliseo Baquero** [@Eliseo-AI](https://github.com/Eliseo-AI)
- El archivo de codigo esta en formato jupiternotebook  
- "Chatbot-Cocina.pynb"

## Licensing
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Authors:
* **Eliseo Baquero** [@Eliseo-AI](https://github.com/Eliseo-AI)

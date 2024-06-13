import streamlit as st
from langchain.embeddings.cohere import CohereEmbeddings
from langchain.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.retrievers import TFIDFRetriever
from langchain.memory import ConversationBufferMemory
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Plantilla de prompt

prompt_template = """
Instrucciones
Escribe tú prompt según tus intereses y gustos
Question:{question}

Documents: {context}
"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# Ruta para carga de documentos
loader = PyPDFDirectoryLoader("/Ruta donde guarda los archivos/")
docs = loader.load()

# División de texto
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(docs)

# Configuración de embeddings
cohere_api_key = 'su api key'
embeddings = CohereEmbeddings(
    model="embed-multilingual-v3.0", cohere_api_key=cohere_api_key
)

# Configuración de retriever
db = TFIDFRetriever.from_documents(texts)

# Configuración de QA
qa = RetrievalQA.from_chain_type(llm=Cohere(model="command-nightly", temperature=0, cohere_api_key=cohere_api_key, max_tokens=1000),
                                 chain_type="stuff",
                                 retriever=db,
                                 verbose=False,
                                 chain_type_kwargs={"verbose": False, "prompt": PROMPT,
                                                    "memory": ConversationBufferMemory(
                                                        memory_key="history",
                                                        input_key="question"),
                                                    })

# Lista para almacenar respuestas
answers = []

# Función para manejar la lógica de la aplicación
def main():
     st.title("👩‍🍳Asistente de Cocina enfocado en Comida Colombiana👨🏿‍🍳")
     st.markdown("Bienvenido a este tú  Asistente de cocina (Chatbot) que responde ❓❓❓ preguntas, dudas e inquietudes relacionadas con la gastronomía Colombiana.")
     st.subheader("Información relevante sobre el Asistente de Cocina")

     with st.expander("📚 Tipos de Recetas"):
              st.markdown('''Esta herramienta culinaria cuenta con recetas de platos tradicionales, así como: 
                      🍛entradas, 🍪postres, bizcochos, colaciones, amasijos, ☕bebidas, 🍹cocteles, aperitivos, 
                      🍲caldos y sopas. Por último, se puede preguntar por una receta con un ingrediente específico 
                      o por el nombre de una receta conocida, por lo mismo se quiere llegar a todo público, 
                      por lo cual se cuenta con otros tipos de recetas, por ejemplo recetas vegetarianas y de ensalada.''''')

     with st.expander("🇨🇴 Regiones"):
            st.markdown('''Incluye recetas de la gastronomía Colombiana de la siguiente forma: \n
                  Regiones 
                  1. Costa Pacífica. 
                  2. Antioquia y Viejo Caldas.
                  3. Llanos y Amazonia. 
                  4. Valle, Cauca y Nariño. 
                  5. Santanderes. 
                  6. Costa Atlántica. 
                  7. Tolima y Huila. 
                  8. Boyacá y Cundinamarca.  

                  Otros
                  Además se incluye un Recetario de comida Santafereña.  
                  Un Recetario de comida Raizal del Archipiélago de San Andrés, 
                  Providencia y Santa Catalina.
                  Dos recetarios especiales, uno con recetas campesinas Y otro 
                  con productos de zonas que están en proceso de Paz. ''')       
         
     with st.expander("⚠️ Advertencias"):
              st.markdown('''Aunque cuenta con información de Chef reconocidos que practican la cocina 
                      Colombiana y de algunos restaurantes famosos, se le recomienda al usuario interesado 
                      en esos puntos específicos hacer una búsqueda más exhaustiva en otros medios, 
                      como en páginas especializadas, libros de cocina, o en las redes sociales de los chef 
                      y/o restaurantes para encontrar las respuestas que se están buscando.''')
     question = st.text_area("Haz tu pregunta relacionada con la gastronomía Colombiana") 

     if st.button("Obtener Respuesta"):
                    if question.strip() == "":
                        st.write("Por favor, ingrese una pregunta antes de enviar.")
                    else:
                        answer = qa.run({"query": question})
                        answers.append(answer)
                        st.write(answer)

     if len(answers) >= 10:
        st.subheader("Respuestas anteriores:")
        for i, ans in enumerate(answers[-10:]):
            st.write(f"Pregunta {i+1}: {ans}")

     st.subheader("🤖Chatbot\nDesarrollado por [Eliseo Baquero](https://github.com/Eliseo-AI/Eliseo-AI)\n\n[Bootcamp Inteligencia Artificial Nivel Avanzado](https://talentotechbogota.co/#bootcamps)")
# Ejecutar la aplicación Streamlit
if __name__ == "__main__":
    main()

# python -m venv .venv
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1
# python -m streamlit hello
# python -m streamlit run PC4_trio.py

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

### Opción 1: Menú vertical
#with st.sidebar:
   # opciones = option_menu("Selecciona una sección: ",['Presentación', 'Experiencia', 'Gráficos'] , 
       # icons=['0-circle','1-circle', '2-circle'], menu_icon="filetype-py", default_index=0)

### Opción 2: Menú horizontal
opciones_2 = option_menu(
    menu_title="Selecciona una sección: ", 
    options=['Presentación', 'Experiencia', 'Gráficos'], 
    icons=['0-circle','1-circle', '2-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones == 'Presentaciones':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre del blog</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("ellie.png", caption='Ellie', width=300)

    texto = """
    Aquí escribe una presentación creativa sobre ti.
    Mi Nombre es Mayte Montalva, tengo 24 años y soy de de Lima, Peru, ademas estudio publicidad en la PUCP. 
    Lo que mas me gusta de mi carrera es como idear propuestas las marcas o empresas puedan acercarse a sus consumidores, haciendolo ademas de una manera creativa
    y llamativa para diferenciarse de las demas opciones. en un futuro me gustria hacer una maestria en el extranjero, preferiblemente China, para especializarme en 
    tecnicas publicitaria alineadas al marketing digital. En mi tiempo libre me gusta leer y escuchar musica.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Alumno b
    col1, col2 = st.columns(2)
    
    texto_2 = """
    Hola, mi nombre es Gabriela, pero puedes decirme Gabi. Soy de Moyobamba, de la selva y me mude a Lima hace 4 años. 
    Estudio comunicación para el desarollo en la PUCP.
    Lo que me encanta de mi carrera es que es que busca generar cambios sociales, ya sea en temas de salud, educación o incluso cultura creando campañas y proyectos de desarrollo.
    En el futuro me encantaría hacer proyectos de investigación y hacer trabajo de campo con las comunidades
    En mi tiempo libre me gustar escuchar música, leer y pintar.
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)
    
    col2.image("ellie.png", caption='Ellie', width=300)

    # Alumno c
    col1, col2 = st.columns(2)
    
    col1.image("ellie.png", caption='Ellie', width=300)
    
    texto_3 = """
    Hola!!! Me llamo Matias, actualmente temgo 19 años, nací en febrero y eso me convierte en Acuario :). Nací en Lima, Perú y
    estudio la carrera de publicidad en la PUCP, lo que más me gusta de mi carrera es las herramientas que te brinda la publicidad
    para influir en el comportamiento de las personas para que prefieran tu producto o servicio frente a otros. Es interesante cómo
    somo seres bastante influyentes. No me cierro a ninguna posibilidad que me pueda abrir mi carrera, ya que existen varias áreas, pero
    siempre me voy a inclinar por el lado más creativo y todo lo que temga que ver con eso, me encantaría estar en vuelto en campañas
    super disruptivas. Una de las cosas que más me gusta hacer es editar videos, siento que es una actividad que me permite recargarme, por
    así decirlo, de creatividad.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)
    
elif  opciones == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """

    En cuanto a mi experiencia con la programacion, llevé unas cuantas clases en mi último año de secundaria, aunque la verdad no aprendi mucho, 
    asi que considero que esta clase es mi primera eperiencia en programacion. Al inicio me sentia bastante nerviosa ya que los programas y codigos
    se ven intimidandes al inicio. Sin embargo, con el transcurso de las clases considero que fui tomando confianza. La programamcion me ha enseñado
    a ser bastante minuciosa y estar pendiente a los detalles, ya que un solo error malogra todo tu codigo. Me parece bastante interesante descubrir
    como se crean las funciones de laspaginas web que utilizamos dia a dia. Por ultimo, siento que esta herrmienta puede ser de gran utilida para crear 
    paginas web para empresas, por lo que es un gran aporte para mi CV en futuros trabajos
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio? 
    ¿Qué te ha enseñado la programación? 
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )

    # Alumno b
    texto_5 = """
    Aquí escribe tu experiencia aprendiendo a programar. 
    ¿Cómo te sentiste al principio?
    ¿Qué te ha enseñado la programación?
    ¿Qué te gusta de programar? 
    ¿Qué te gustaría hacer con la programación en el futuro?
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Practica calificada 1-Gabi")
    st.video("https://youtu.be/V-dHuWXDq74?feature=shared")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    st.subheader("🎥 Practica calificada 2-Gabi")
    st.video("https://youtu.be/ip_kpPUUpWA?feature=shared")

    # Alumno c
    texto_6 = """
  Es mi primera vez programando. 
    Al principio pensé que era muy difcil aprenderse todos los códigos, librerías, etc. pero en el transcurso del curso me di cuenta que si tiene su grado de dificultad, pero es posible aprender.
    La programación me ha enseñado a ver el transfondo y funcionamiento de muchos programas.
    La verdad no me gusta mucho la programación, pero considero que cuando programas con temas que te gustan se hace más divertida la experiencia.
    En el futuro quisiera que la programación me ayude a completar investigaciones. ya que creo que hace más practico el manejo de datos.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_6}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Título apropiado video 1")
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
        
    # Formato Google Drive
    st.subheader("🎥 Título apropiado video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:  
        st.link_button("🎥 Texto del botón",
                       "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link",
                       use_container_width=True
            )
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = ['Gráfico_1', 'Gráfico_2', 'Mapa_1'] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'Gráfico_1':
        st.subheader("📊 Gráfico 1: Lenguas aisladas")
        texto_7 = """
        Interpretación del Gráfico 1
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("aisladas_base_datos.png", width=800)

    elif grafico_seleccionado == 'Gráfico_2':
        st.subheader("📊 Gráfico 2: Familias lingüísticas")
        texto_8 = """
        Interpretación del Gráfico 2
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("lengua_familia_GB.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_9 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        with open("mapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    

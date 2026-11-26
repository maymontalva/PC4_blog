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
    options=['Presentaciones', 'Experiencia', 'Gráficos'], 
    icons=['0-circle','1-circle', '2-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if opciones_2 == 'Presentaciones':
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: pink'>Nombre del blog</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("May.jpg", caption='Mayte', width=300)

    texto = """
    Aquí escribe una presentación creativa sobre ti.
    Mi Nombre es Mayte Montalva, tengo 24 años y soy de de Lima, Peru. Además estudio publicidad en la PUCP. 
    Lo que mas me gusta de mi carrera es como idear propuestas las marcas o empresas puedan acercarse a sus consumidores, haciendolo ademas de una manera creativa
    y llamativa para diferenciarse de las demas opciones. En un futuro me gustria hacer una maestria en el extranjero, preferiblemente China, para especializarme en 
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
    
    col2.image("IMG_0843.JPG", caption='Gabriela', width=300)

    # Alumno c
    col1, col2 = st.columns(2)
    
    col1.image("IMG_7672.PNG", caption='Matias', width=300)
    
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
    
elif  opciones_2 == 'Experiencia':

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: black'>Nombre a la sección de experiencia 💻</h1>", unsafe_allow_html=True)

    # Alumno a
    texto_4 = """

    En cuanto a mi experiencia con la programacion, llevé unas cuantas clases en mi último año de secundaria, aunque la verdad no aprendi mucho, 
    asi que considero que esta clase es mi primera experiencia en programacion. Al inicio me sentia bastante nerviosa ya que los programas y codigos
    se ven intimidandes al inicio. Sin embargo, con el transcurso de las clases considero que fui tomando confianza. La programacion me ha enseñado
    a ser bastante minuciosa y estar pendiente a los detalles, ya que un solo error malogra todo tu codigo. Me parece bastante interesante descubrir
    como se crean las funciones de las paginas web que utilizamos dia a dia. Por ultimo, siento que esta herramienta puede ser de gran utilidad para crear 
    paginas web para empresas, por lo que es un gran aporte para mi CV en futuros trabajos.
    Aquí escribe tu experiencia aprendiendo a programar. 
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    
    # Formato YouTube
    st.subheader("🎥 Mayte video 1")
    st.video("https://youtu.be/TC1kO4Qa8T4")
    
    
    col1, col2, col3 = st.columns([1, 2, 1])

    st.subheader("🎥 Mayte video 2")
    st.video("https://youtu.be/TC1kO4Qa8T4")
            

    # Alumno b
    texto_5 = """
    Es mi primera vez programando. 
    Al principio pensé que era muy difcil aprenderse todos los códigos, librerías, etc. pero en el transcurso del curso me di cuenta que si tiene su grado de dificultad, pero es posible aprender.
    La programación me ha enseñado a ver el transfondo y funcionamiento de muchos programas.
    La verdad no me gusta mucho la programación, pero considero que cuando programas con temas que te gustan se hace más divertida la experiencia.
    En el futuro quisiera que la programación me ayude a completar investigaciones. ya que creo que hace más practico el manejo de datos.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_5}</div>", unsafe_allow_html=True)
        
    # Formato YouTube
    st.subheader("🎥 Practica calificada 1-Gabi")
    st.video("https://youtu.be/V-dHuWXDq74?feature=shared")
        
    # Formato Google Drive
    #st.subheader("🎥 Título apropiado video 2")
    
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
    st.subheader("🎥 Matias video 1")
    st.video("https://youtu.be/eE7hFwfy8g8?si=X5Aw_EzsirED0W7j")
        
    # Formato Google Drive
    #st.subheader("🎥 Matias video 2")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    st.subheader("🎥 Matias video 2")
    st.video("https://youtu.be/RTVwgBjDewU?si=EGDu6QW29c7BNyER")
            
else:

    st.markdown("<h1 style='text-align: center;font-size: 50 px; color: black'>Nombre a la sección</h1>", unsafe_allow_html=True)
    
    # Aquí todos los integrantes deben poner sus 3 gráficos y su mapa en la lista 
    # y aumentar la estructura condicional como sea necesaria
    graficos = [ "barras.png", "histograma_1.png", 'mapa_pucp.html', "mapa_vettel_raikkonen.html", "pastel.png", "wordcloud.png", 
    "maywordcloud.png", "maybarras.png", "maymapa.html", "mayhistograma.png", "maypastel.png", "grafico_de_barras_gabi.png",
    "histograma_abi.png", "nube_de_gabi.png", "grafico_pastel_gabi.png" ] 
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)
    
    if grafico_seleccionado == 'maybarras.png':
        st.subheader("📊 Grafico de barras Mayte: Tarjetas rojas del Girona")
        texto_7 = """
        El gráfico muestra el promedio de tarjetas rojas recibidas por los equipos jugando como locales. 
        Se observa que el Girona presenta el promedio más alto, con aproximadamente 0,37 tarjetas rojas,
        seguido del Real Madrid y el Oviedo. En cambio, equipos como el Barcelona, Betis y Valencia no registran tarjetas rojas en los datos representados.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_7}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
                st.image("maybarras.png", width=800)

    elif grafico_seleccionado == 'maypastel.png':
        st.subheader("📊 Gráfico pastel Mayte: Goles Girona")
        texto_8 = """
        El gráfico muestra que el Girona, jugando como local durante la temporada 2025-2026, ha obtenido un mayor porcentaje de derrotas, con un 36,8 % de los partidos. 
        Por otro lado, el 31,6 % de los encuentros terminaron en victoria y el mismo porcentaje en empate. 
        Estos resultados reflejan que el equipo ha tenido un rendimiento irregular en casa, ya que las derrotas superan ligeramente a las victorias y los empates.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("maypastel.png", width=800)
    elif grafico_seleccionado == 'mayhistograma.png':
        st.subheader("📊 Histograma Mayte: Goles Girona")
        texto_8 = """
       Este gráfico muestra que el Girona, jugando como local, suele anotar entre 1 y 2 goles por partido, siendo esta la frecuencia más habitual.
       También se observa que en algunos encuentros marca 0, 3 o 4 goles, aunque estos resultados son menos frecuentes. 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("mayhistograma.png", width=800)
    elif grafico_seleccionado == 'maymapa.png':
        st.subheader("📊 Wordcloud Mayte: Risas y Cultura")
        texto_8 = """
       Esta nube de palabras resalta el contenido del 1er capitulo del libro "Risas y Cultura", escrito por luis peirano. En este libose hace un analisi de
       los personaes y dinamicas de famoso programa televisivo de los 90 "Risas y Cultura" de panamericana television, asi como su impacto en la sociedad peruana
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("maywordcloud.png", width=800)
    
    else:
        st.subheader("🗺️ Mapa 1: Distribución geográfica")
        texto_9 = """
        Interpretación del mapa
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        with open("maymapa.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    

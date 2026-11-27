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
    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: pink'>Blogcito <3</h1>", unsafe_allow_html=True)

    # Alumno a
    col1, col2 = st.columns(2)
    
    col1.image("May.jpg", caption='Mayte', width=300)

    texto = """
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

    st.markdown("<h1 style='text-align: center; font-size: 50 px; color: blue'>Experiencia 💻</h1>", unsafe_allow_html=True)

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
    Cuando empecé a programar me sentí un poco intimidado, porque la verdad creí que iba a ser algo complicado y bastante laborioso (lo cual sí es),
    pero he aprendido a manejar (hasta cierto punto) un nuevo programa como Colab y las funciones que existen, es muy interesante como con ciertos códigos podemos
    simplificar tareas como depurar un texto, o jugar con las condicionales. Lo que me gusta de programar es que hay un código para todo y que, sí es cierto, que al final
    puede
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
        st.subheader("📊 Gráfico pastel Mayte: Resultados Girona")
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
       El primer gráfico muestra que el Girona, jugando como local, suele anotar entre 1 y 2 goles por partido, siendo esta la frecuencia más habitual.
       También se observa que en algunos encuentros marca 0, 3 o 4 goles, aunque estos resultados son menos frecuentes. Por otro lado, el segundo gráfico indica que,
       como visitante, el Girona recibe principalmente 1 o 2 goles por partido, destacando especialmente los encuentros en los que recibe 1 gol. Sin embargo, existen 
       algunos partidos en los que ha recibido 0, 3 o incluso 5 goles. Al comparar ambos gráficos, se aprecia que
       el Girona presenta una tendencia ofensiva relativamente constante como local, mientras que su rendimiento defensivo como visitante muestra cierta irregularidad.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("mayhistograma.png", width=800)
    elif grafico_seleccionado == 'maywordcloud.png':
        st.subheader(" Wordcloud Mayte: Risas y Cultura")
        texto_8 = """
       Esta nube de palabras resalta el contenido del 1er capitulo del libro "Risas y Cultura", escrito por Luis Peirano. En este libro se hace un analisis de
       los personajes y dinamicas de famoso programa televisivo de los 90 "Risas y Cultura" de Panamericana television, asi como su impacto en la sociedad peruana.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("maywordcloud.png", width=800)
    elif grafico_seleccionado == 'grafico_de_barras_gabi.png':
        st.subheader("📊 Grafico de Barras Gabi: Tarjetas amarillas liga")
        texto_8 = """
      Gráfico de barras: El gráfico de barras presenta el promedio de tarjetas amarillas recibidas por los equipos de La Liga cuando juegan como visitantes. 
      Se observa que siete equipos (encabezados por el Villarreal) registran el promedio más alto, con exactamente 3.0 tarjetas amarillas por partido fuera de casa.
      En contraste, el resto de los equipos de la lista (como el Athletic Bilbao, Barcelona o Real Madrid) presentan un promedio menor, situado en 2.0 tarjetas. 
      Es importante destacar que el Getafe se encuentra en el grupo de mayor
      amonestación (3.0). Esta comparación permite identificar que, en esta muestra, la disciplina fuera de casa se divide claramente en dos bloques bien diferenciados.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("grafico_de_barras_gabi.png", width=800)
    elif grafico_seleccionado == 'barras.png':
        st.subheader("📊 Grafico de Barras Matias: Tarjetas amarillas")
        texto_8 = """
      Se observa que la mayoría de los equipos mantiene un promedio entre 2 y 3 trajetas amarillas por partido fuera de casa. Celta se ubica en un rango intermedio, 
      esto muestra un nivel de faltas moderado en comparación con el resto de equipos, existe una disciplina estandar por parte del equipo Celta dentro de la liga 
      
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("barras.png", width=800)
   
    elif grafico_seleccionado == 'grafico_pastel_gabi.png':
        st.subheader("📊 Grafico Pastel Gabi: Resultados Getafe")
        texto_8 = """
      Gráfico pastel de gabi: El gráfico muestra la distribución de los resultados obtenidos por el Getafe cuando juega como local.
      Se observa un empate técnico en la mayor proporción: tanto las victorias como las derrotas representan un 42.1% del total de los partidos. 
      Por otro lado, los empates constituyen la menor proporción, con apenas un 15.8%, lo que indica que es el resultado menos
      frecuente para el equipo en casa. En síntesis, la distribución revela un desempeño local muy polarizado, donde el equipo o gana o pierde, 
      pero rara vez reparte puntos.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("grafico_pastel_gabi.png", width=800)
    elif grafico_seleccionado == 'histograma_abi.png':
        st.subheader("📊 Histograma Gabi: Goles Getafe")
        texto_8 = """
       En el histograma se muestra la distribución de los goles anotados por el Getafe cuando juega como local.
       Se observa que la cantidad más frecuente es de 0 goles, con 8 partidos, lo que indica que el equipo tuvo dificultades para marcar en una parte importante de sus encuentros en casa. Asimismo,
       se registra una frecuencia de 5 partidos en los que anotó 1 gol y otros 5 en los que anotó 2 goles. Finalmente, solo en 1 partido logró anotar 3 goles. En general, los resultados muestran 
       que el Getafe presenta una tendencia a marcar pocos goles cuando juega como local, ya que la mayor concentración de partidos se encuentra entre los 0 y 2 goles.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma_abi.png", width=800)
           
    elif grafico_seleccionado == 'nube_de_gabi.png':
        st.subheader("Wordcloud Gabi: Crimen y castigo")
        texto_8 = """
      Esta nube de palabras resalta las palabras mas frecuentes del libro "Crimen y castigo", escrito por Fiodor Dostovyeski 
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("nube_de_gabi.png", width=800)
           
    elif grafico_seleccionado == 'histograma_1.png':
        st.subheader("📊 Histograma Matias: Goles recibidos Celta")
        texto_8 = """
      En cuanto a los goles recibidos como local, la distribución muestra que la mayor 
      frecuencia se concentra en 1 gol recibido, seguido por los encuentros en los que el equipo logró mantener
      su portería en cero y aquellos donde recibió 2 goles.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("histograma_1.png", width=800)
    elif grafico_seleccionado == 'pastel.png':
        st.subheader("📊 Grafico pastel Matias: Resultados Celta")
        texto_8 = """
      Observamos que la mayor proporción corresponde a victorias, seguida de empates y, en menor proporción, derrotas fuera de casa. La diferencia entre
      victorias y derrotas es notable y favorable para el equipo. Esto demuestra que Celta tiene una buena capacidad para conseguir victorias cuando
      juega fuera de casa.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("pastel.png", width=800)
    elif grafico_seleccionado == 'wordcloud.png':
        st.subheader(" Wordcloud Matias: El principito")
        texto_8 = """
      Esta nube de palabras resalta las palabras mas frecuentes del libro "El pincipito", escrito por Antoine de Saint-Exuperi
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        col1, col2, col3 = st.columns([1, 7, 1])
        with col2:
            st.image("wordcloud.png", width=800) 
           
    elif grafico_seleccionado == 'mapa_pucp.html':
        st.subheader(" 🗺️ Mapa Gabi: Puerta Principal")
        texto_8 = """
        Para la elaboración del mapa interactivo se utilizó la biblioteca Folium, debido a que permite representar información geográfica mediante marcadores y
        ventanas emergentes. Se eligió OpenStreetMap como mapa base 
        porque facilita la ubicación de las ciudades de nacimiento de los pilotos y permite visualizar sus posiciones geográficas.
        Respecto a los marcadores, se utilizaron colores diferentes para distinguir a Nico Rosberg y Felipe Massa, lo que facilita identificar a cada piloto en el mapa. Asimismo, se incorporó un ícono
        relacionado con las carreras de automovilismo para mantener una relación visual con el tema de la Fórmula 1.
        En las ventanas emergentes se emplearon etiquetas HTML como h2 para destacar el nombre de cada piloto, img para incorporar su fotografía y p  para organizar la información de su 
        escudería, lugar de nacimiento y puntaje total. 
        También se utilizó b para resaltar los datos más importantes. Finalmente, se optó por una distribución centrada y ordenada para facilitar
        la lectura y permitir que el usuario identifique rápidamente la información de cada piloto. De esta manera, el mapa no solo presenta la ubicación geográfica, sino que también integra información 
        deportiva y personal de los participantes de la temporada 2016.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        with open("mapa_pucp.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
        components.html(html_content,height=600)
    elif grafico_seleccionado == 'mapa_vettel_raikkonen.html':
        st.subheader(" 🗺️ Mapa Matias: Pilotos F1")
        texto_8 = """
      Para este diseño, elegí una distribución vertical y centrada porque permite identificar al piloto y leer sus datos de manera
      ordenada: nombre, imagen, escudería y puntaje. Asismiso elegí dos pilotos que pertenecen a la misma escudería, Ferrari, esto
      facilita una comparación entre ambos.
      Los elementos html, como el h2, lo use para el nombre del piloto y funciona como título princiapl, tiene un color azul para que resalte.
      img: muestra la fotografía del piloto en un tamaño cuadrado de 150x150 px y border radius de 10 px para darle un borde redondo y que se vea más suave
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_8}</div>", unsafe_allow_html=True)
    
        with open("mapa_vettel_raikkonen.html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    else:
        st.subheader("🗺️ Mapa Mayte: Nacionalidad pilotos")
        texto_9 = """
        Elegí esta forma de organizar la información porque permite mostrar los datos de cada piloto de manera clara y ordenada dentro de una ventana 
        emergente. Primero utilicé elementos HTML como h2 para destacar el nombre del piloto, p para separar sus datos y b para resaltar información
        importante como la nacionalidad, la escudería y el puntaje total. También agregué una imagen para facilitar su identificación y utilicé estilos
        como el texto centrado y los margenes para lograr una presentación más agradable y fácil de leer. De esta manera, el usuario puede consultar la 
        información de cada piloto simplemente haciendo clic en su marcador del mapa. Ademas agrege un color e icono llamativo al marcador del mapa para 
        que este sea facil de encontrar.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_9}</div>", unsafe_allow_html=True)
            
        with open("maymapa (1).html", "r", encoding="utf-8") as mapa:
                html_content = mapa.read()
    
        components.html(html_content,height=600)
    

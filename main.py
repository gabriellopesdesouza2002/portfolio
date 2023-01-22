import os
import streamlit as st
from tools.tools import *
from src.widgets.widgets import *
from streamlit_extras.buy_me_a_coffee import button as buy_me_a_coffe
from markdownlit import mdlit
from streamlit_extras.badges import badge

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="👨🏽‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
sidebar = st.sidebar
sidebar.title('Bem vindo à MultiTools, aqui você terá diversas ferramentas para o seu dia a dia.')
choice = sidebar.selectbox('Escolha para onde você quer ir', ['Home / Ferramentas', 'Sobre...'])
sidebar.warning('Ainda estou desenvolvendo, espere mais algumas semanas que você verá várias ferramentas aqui. 😉')



if choice == 'Home / Ferramentas':
    st.title('MultiTools')
    st.subheader('Aqui você encontrará diversas ferramentas para ajudar no seu desenvolvimento...')
    ferramenta = st.selectbox('Ferramentas', ['Converter de Bytes para...'])

    if ferramenta == 'Converter de Bytes para...':
        converter_os_bytes()

elif choice == 'Sobre...':
    c1, c2 = st.columns(2)
    c1.image('gabriel.jpeg', width=150)
    c2.markdown('## Gabriel Lopes')
    c2.markdown('##### Desenvolvedor Python júnior que está sempre em busca de novas funcionalidades. Não apenas para mim, mas também para ouros Devs e quem sabe, para o mundo, utilizando  sempre como linguagem principal, o Python.')
    c2.markdown('###### [Isso é amar ao próximo como a ti mesmo!](https://www.bibliaon.com/versiculo/mateus_22_37-39/)')
    st.markdown('---')
    st.markdown('##### Algumas das minhas competências:')
    with st.expander('Python e Suas Bibliotecas'):
        st.markdown('#### Criação de sistemas utilizando:')
        st.markdown('* Selenium (um dos que mais uso para Web Scraping);')
        st.markdown('* BS4 - Beautifulsoup 4 (para Web Scraping também);')
        st.markdown('* Requests (para consumo de APIs Rest e um pouco para Web Scraping);')
        st.markdown('* Streamlit (onde está executando esse "CV");')
        st.markdown('* POO;')
        st.markdown('* Pandas (para manipular desde arquivos Excel, até criar alguns gráficos);')
        st.markdown('* Openpyxl;')
        st.markdown('* Regex - re;')
        st.markdown('* Rest API')
        st.markdown('* .env (Para chaves de API e credenciais que não devem ser expostas no código);')
        st.markdown('* PySimpleGUI (para fazer interfaces gráficas);')
        st.markdown('* PyInstaller (para fazer arquivos .exe);')
        st.markdown('* GitHub Actions (para deixar alguns scripts sendo executados automaticamente);')
        st.markdown('* PythonAnywhere (para APIs Rest, Automação de Tarefas e entre outras atividades);')
        st.markdown('* Google Sheets API for Python;')
        st.markdown('* Google BigQuery API for Python;')
        st.markdown('* Um pouquinho de Odoo ERP;')
        st.markdown('* Entre outras bibliotecas (são muitas). 😱')
        st.markdown('> Ufa! Ainda crio desde automações utilizando Selenium, analises de dados, criação e consumo de APIs Rest, e por ai vai. Estou sempre tentando melhorar...')
    with st.expander('Banco de Dados e SGBDs'):
        st.markdown('#### Sei manipular esses bancos e ferramentas para bancos de dados:')
        st.markdown('* [SQL](https://pt.wikipedia.org/wiki/SQL) (que é primordial);')
        st.markdown('* [PostgreSQL](https://www.postgresql.org/) (para muitos dos projetos que já criei empresarialmente);')
        st.markdown('* [MySQL](https://www.mysql.com/) (Para bancos de dados no PythonAnywhere);')
        st.markdown('* [SQLite](https://www.sqlite.org/index.html) (Um dos que mais utilizo para .exe);')
        st.markdown('* [TinyDB](https://tinydb.readthedocs.io/en/latest/) (esse utilizo muito pouco...);')
        st.markdown('> Para o SQLite, sei tanto utilizar com o Python, quanto com o [DB Browser](https://sqlitebrowser.org/);')
    with st.expander('CSS & HTML'):
        st.markdown('#### Fiz alguns sites utilizando:')
        st.markdown('* CSS;')
        st.markdown('* HTML;')
        st.markdown('* JavaScript;')
        st.markdown('* Bootstrap;')
        st.markdown('* Outras ferramentas que auxiliaram no desenvolvimento.')
    with st.expander('Sistemas Operacionais - OS'):
        st.markdown('* Windows')
        st.markdown('> No Windows, desde o pacote Office, até configurações de variáveis de ambiente para o desenvolvimento...')
        st.markdown('* Linux ')
        st.markdown('> Pelo Linux, trabalho desde o Terminal, até ferramentas como o SSH para conexões com bancos de dados...')
    
    
    col1, col2, col3 = st.columns(3)
    from streamlit_extras.mention import mention

    st.markdown('Entre em contato comigo, será ótimo trocar experiências (independente da sua área)...')
    with col1:
        mention(
            label="LinkedIn",
            icon="https://cdn-icons-png.flaticon.com/512/174/174857.png",
            url="https://linkedin.com/in/gabriel-lopes2002",
        )
    with col2:
        mention(
            label="GitHub",
            icon="Github",
            url="https://linkedin.com/in/gabriel-lopes2002",
        )
    with col3:
        mention(
            label="WhatsApp",
            icon="https://cdn-icons-png.flaticon.com/512/3536/3536445.png",
            url="https://linkedin.com/in/gabriel-lopes2002",
        )
        
    with st.expander('Algumas "frases" do meu livro preferido...'):
        st.markdown('## **A Bíblia!**')
        st.markdown('##### ***O temor do Senhor é o princípio da ciência; Os loucos desprezam a sabedoria e a instrução. - Provérbios: 1:7***')
        st.markdown('##### ***O que trabalha com mão displicente empobrece, mas a mão dos diligentes enriquece. - Provérbios 10:4***')
        st.markdown('##### ***Porque o Filho do homem veio buscar e salvar o que se havia perdido. - Lucas 19:10***')

    
    buy_me_a_coffe('gabriellopes', text='Me dê um café...', floating=False, bg_color='#00A867')
import streamlit as st       
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           


# Cores:
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #32CD32, #E3F2FD);
    }
    </style>
    """,
    unsafe_allow_html=True
)

#login:
st.title('Seja bem vindo á VendaGest')
st.write('## Faça o login')

nome_usuario = st.text_input('Digite seu nome: ')
senha_s = st.text_input('Digite sua senha: ', type='password')

if senha_s in ['1234', '4321', 'pedro']:
    st.button('Entrar')
    st.page_link('pages/principal.py',
                 label='Entrar',
                 icon='✔')
    st.success('Ok, click no botão acima para avançar.')

else:
     st.error('Tente novamente.')  

st.write('## Sobre a VendaGest')     
st.write('-> A VendaGest é um site para você ter controle da sua empresa ou seu negocio.')
st.write('Na VendaGest você tem acesso a graficos e tabelas de finaças da sua empresa.')
st.write('Para ter mais informações acesse nosso instagram ou entre em contato com nossos desenvolvedores.')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# Banco de dados:
engine = create_engine('sqlite:///dados_usuarios.db')
Session = sessionmaker(bind=engine)
session = Session()

base = declarative_base()
# Tabelas:

class Usuario(base):
    __tablename__ = 'usuarios' 
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    senha = Column('senha', String)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, senha, ativo, ):
        self.nome = nome
        self.senha = senha
        self.ativo = ativo


base.metadata.create_all(bind=engine)


# Adicionar no banco (CRUD):
if nome_usuario and senha_s:
    usuario1 = Usuario(nome=nome_usuario, 
                          senha = senha_s, 
                          ativo=True)
session.add(usuario1)
session.commit()
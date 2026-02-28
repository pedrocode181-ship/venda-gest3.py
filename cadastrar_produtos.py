from sqlalchemy import create_engine,Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import streamlit as st 
import pandas as pd
# cores
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

st.title('Cadastro de produtos')
st.write('Adicione as informações desejadas.')

produto1 = st.text_input('Digite o nome do produto:')
valor1 = st.number_input('Digite o valor do produto:')
validade1 = st.text_input('Digite a validade do produto')

# banco de dados
engine = create_engine('sqlite:///dados_produtos.db')
session = sessionmaker(bind=engine)
session = session()
base = declarative_base()
# Tabela
class Produtos(base):
    __tablename__ = 'produto'
    id = Column('id', Integer, primary_key=True)
    produto = Column('produto', String)
    valor = Column('valor', Integer)
    validade = Column('validade', String)

    def __init__(self, produto, valor, validade):
        self.produto = produto
        self.valor = valor
        self.validade = validade 

base.metadata.create_all(bind=engine)    

# Cadastrar o produto
if st.button('Cadastrar', type='primary'):
    produto_cadastrado = Produtos(produto=produto1, valor=valor1, validade=validade1)
    session.add(produto_cadastrado)
    session.commit()

# Tabela de produtos cadastrados
st.title("📦 Tabela de Produtos cadastrados")
df = pd.read_sql("SELECT * FROM produto", engine)
st.dataframe(df) 
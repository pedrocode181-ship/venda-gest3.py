import streamlit as st
# Cores 
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
# Página principal

st.title('Página principal')

st.write('-> Aqui é a página principal do seu site onde você vai encontrar os contatos dos desenvolvedores e botões de acesso' \
'para as páginas seguintes.')
# Contatos
st.write('## Contatos dos desenvolvedores')

st.write('Pedro -> 81994317883')
numero_pedro = 81994317883 
mensagem = 'Olá vimpelo WhatsApp'
link = f'https://wa.me/{numero_pedro}?text={mensagem}'

st.link_button('💬 Conversar com Pedro', link, type='primary')

# Acesso das proximas páginas

st.write('## Botões de acesso ')

if st.button('Grafico de vendas', type='primary'):
    st.page_link('pages/grafico1.py',
                 label='Grafico de vendas',
                 icon='📊')
    
if st.button('Dachboard Geral', type='primary'):
    st.page_link('pages/dachboard.py',
                 label='Ir',
                 icon='📊')
    
if st.button('Cadastro de produtos', type='primary'):
    st.page_link('pages/cadastrar_produtos.py',
                 label='Ir',
                 icon='✔'
                 )
import streamlit as st


st.title('**st.latex**')
st.write('*Displays mathematical expressions formatted as LaTeX*')

option = st.selectbox('Pick any math formula!',
('Formula 1', 'Formula 2'))

if option == 'Formula 1':
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

if option == 'Formula 2':
    st.latex(r'''(a + b)^2 = a^2 + 2ab + b^2''')
import datetime

import streamlit as st
import pandas as pd
import numpy as np

# Import and header
st.header('My Dashboard')

# Display text and sidebar in the browser
st.text('BrunoPyDev')
st.sidebar.markdown('# Filter menu')
st.sidebar.text(' Filter menu')

# Displays text with (markdown) formatting
st.markdown('### streamlit')

# Create a caption
st.caption('Zeze balloon creates images with modeling balloons ...')

# Renders different elements
people = [{'Name': 'Bruno', 'Age': '43'},
          {'Name': 'Inês', 'Age': '36'}]
st.write("# hello", ['Bruno', 'Gonçalves'])
st.write('Person', people)

# Display a title
st.title('My title')


#  Data display

# Create and display a table
df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['Price', 'Vacancy rate', 'Default rate']
)
st.table(df)

# Create and display a DataFrame
df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Price', 'Vacancy rate', 'Default rate'])

st.dataframe(df)



# Create charts

# Line chart
df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Price', 'Vacancy rate', 'Default rate'])

st.line_chart(df)


# Bar chart
df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Price', 'Vacancy rate', 'Default rate'])

st.bar_chart(df)

# Data input

# Button
if st.button('MEU BOTÃO'):
     st.write('Click')



# Checkbox
check = st.checkbox('Aceito')

if check:
     st.write('Marcado')


# Radio
opcao = st.radio(
 "Selecione uma opção",
 ('Opção 1', 'Opção 2'))

if opcao == 'Opção 1':
    st.write('1')
else:
    st.write("2")


# Selectbox
option = st.selectbox(
    'Selecione',
    ('Op 1', 'Op 2', 'Op 3'))

st.write('Você selecionou:', option)

# Multselect
options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Vermelho', 'Verde'])



# Slider
values = st.slider(
'Intervalo',
0.0, 100.0, (25.0, 75.0))

# Text
title = st.text_input('Nome', 'Caio')

# Number
number = st.number_input('Número')

# Date
d = st.date_input(
 "Digite uma data",
 datetime.date(2022, 2, 2))

#
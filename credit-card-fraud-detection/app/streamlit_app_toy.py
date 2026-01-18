import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import time

st.write("""
         
# My first App
Hello *world!*

         I am new here!

""")

"""
first attempt
"""

df = pd.DataFrame(
    {'first col': [1,2,3,4],
    'second col' : [1,4,6,8]}
)

df

add_selectbox = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first col']
)

'You selected: ', add_selectbox



x = 10

'x', x # draw 

arr = np.random.normal(1,1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)


df2 = pd.DataFrame(
   np.random.randn(10,20),
   columns = ('col %d' % i for i in range(20))
)

st.dataframe(df2.style.highlight_max(axis=0))

st.line_chart(df2)


map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, - 122.4],
    columns=['lat','lon']
)

viz = st.container()

add_slider = st.sidebar.slider('x', label_visibility='hidden')
st.write(x, 'squared is', x*x)

with viz:
    map_data[map_data['lat'] > add_slider]


st.map(map_data)

st.text_input('Your name', key='name')
st.session_state.name

#

left_column, right_column = st.columns(2)
# I can use columns just like st.sidebar:
left_column.button('Press me!')

# Or even better, call st functions inside a with block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
    )
    st.write(f'You are in {chosen} house!')


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    #update progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'... and now we\'re done!'



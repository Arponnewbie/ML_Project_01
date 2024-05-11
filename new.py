import streamlit as st
st.title('MPG ML-Project')

displacement=st.number_input('displacement',value=300,placeholder="enter any number for the displacement")

horsepower=st.number_input('horsepower',value=130,placeholder="enter any number for the horsepower")

weight=st.number_input('weight',value=3000,placeholder="enter any number for the weight")

acceleration=st.number_input('acceleration',value=14,placeholder="enter any number for the Accleration")

import streamlit as st

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

st.title('Factorial Calculator')

number = st.number_input('Enter a number:', min_value=0, step=1)
if st.button('Calculate Factorial'):
    if number < 0:
        st.error('Factorial is not defined for negative numbers.')
    else:
        fact = factorial(int(number))
        st.success(f'The factorial of {number} is: {fact}')


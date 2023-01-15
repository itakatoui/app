import streamlit as st
from scipy.optimize import linprog

st.title("Linear Programming with Streamlit")

# Define the objective function
c = [4, 5]
obj_fun = linprog(c, bounds=(0, None))

st.write("Objective function: ", obj_fun)

# Define the constraints
A = [[3, 2], [1, 2]]
b = [6, 4]

# Solve the linear program
x0_bounds = (0, None)
x1_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')

st.write("Solution: ", res)


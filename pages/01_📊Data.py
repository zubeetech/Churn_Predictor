import streamlit as st
import pyodbc

st.set_page_config(
    page_title='Data Page',
    page_icon='📊',
    layout='wide'
)

st.title("Vodafone Churn Database")

# Create a connection to database
# Qery the database

@st.cache_resource(show_spinner='connecting to database...')


# Define the function to initialize the connection
def init_connect():
    return pyodbc.connect(
        "DRIVER={SQL Server}; SERVER="
        + st.secrets['server']
        + "; DATABASE="
        + st.secrets['database']
        + "; UID="
        + st.secrets['username']
        + "; PWD="
        + st.secrets['password']
    )

# Cache the data fetching function
@st.cache_data(show_spinner='running query...')

def running_query(query):
    conn = init_connect()  # Initialize connection inside the function
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        return rows
    except pyodbc.Error as e:
        st.error(f"Database error: {e}")
        return None
    finally:
        conn.close()

# Define the SQL query
squery = "SELECT * FROM LP2_Telco_churn_first_3000"

# Execute the query
rows = running_query(squery)

# Display the results
if rows:
    st.write(rows)
else:
    st.write("No data available or query failed.")


st.dataframe(rows)

# conn = init_connect()

# @st.cache_data(show_spinner='running query...')

# def running_query(query):
#     with conn.cursor() as cursor:
#         cursor.execute(query)
#         rows = cursor.fetchall()

#     return rows

# squery = " SELECT * FROM LP2_Telco_churn_first_3000 "

# rows = running_query(squery)

# st.write(rows)
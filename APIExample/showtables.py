import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL database
cnx = mysql.connector.connect(user="root", password="Porca0ntasRemota",
                              host="108.143.251.143",
                              database="LBGAPP")
# Read data from MySQL table into a Pandas DataFrame
df = pd.read_sql('SELECT * FROM pessoas', con=cnx)

# Create a bar chart of the data
df.plot(kind='bar', x='column1', y='column2')
plt.show()
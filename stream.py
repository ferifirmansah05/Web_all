import streamlit as st
import pandas as pd
import plotly.express as px

# Contoh data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales_A': [100, 120, 130, 150, 160, 170, 180, 200, 220, 240, 260, 300],
    'Sales_B': [80, 100, 90, 110, 130, 120, 140, 160, 180, 190, 210, 230],
    'Sales_C': [70, 90, 85, 105, 125, 115, 135, 155, 175, 185, 205, 225],
    'Sales_D': [90, 110, 100, 120, 140, 130, 150, 170, 190, 200, 220, 240]
}

df = pd.DataFrame(data)

# Judul aplikasi
st.title("Explorative Line Plot with Multiple Y Axes in Streamlit")

# Filter untuk memilih data
selected_months = st.multiselect("Select Months", options=df['Month'], default=df['Month'])
selected_sales_y1 = st.multiselect("Select Y1 Sales Data", options=['Sales_A', 'Sales_B'], default=['Sales_A'])
selected_sales_y2 = st.multiselect("Select Y2 Sales Data", options=['Sales_C', 'Sales_D'], default=['Sales_C'])

# Filter data berdasarkan pilihan
filtered_df = df[df['Month'].isin(selected_months)]

# Pengaturan plot
st.sidebar.header("Plot Settings")
line_style = st.sidebar.selectbox("Select Line Style", options=['solid', 'dash', 'dot'])
line_width = st.sidebar.slider("Line Width", 1, 10, 3)
plot_height = st.sidebar.slider("Plot Height", 400, 800, 600)

# Membuat plot menggunakan Plotly
fig = px.line(
    filtered_df,
    x='Month',
    y=selected_sales_y1 + selected_sales_y2,
    title='Monthly Sales Comparison',
    labels={'value': 'Sales', 'variable': 'Sales Category'}
)

# Menambahkan garis kedua untuk y2
for y2_col in selected_sales_y2:
    fig.add_scatter(x=filtered_df['Month'], y=filtered_df[y2_col], mode='lines', name=y2_col, yaxis='y2')

# Mengubah gaya garis
for line in fig.data:
    line.update(line=dict(dash=line_style, width=line_width))

# Mengatur sumbu y kedua
fig.update_layout(
    yaxis=dict(title="Y1 Sales"),
    yaxis2=dict(title="Y2 Sales", overlaying='y', side='right'),
    height=plot_height
)

# Menampilkan plot
st.plotly_chart(fig, use_container_width=True)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Read the CSV Data
inventory_df = pd.read_csv('inventory.csv')

# Convert OrderDate to datetime for plotting
inventory_df['OrderDate'] = pd.to_datetime(inventory_df['OrderDate'])

# Tkinter window
root = tk.Tk()
root.title('Inventory Dashboard')

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP)

# Function to create donut chart for product category distribution
def plot_donut_chart():
    category_group = inventory_df.groupby('CategoryName').agg({'OrderItemQuantity': 'sum'})
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(category_group['OrderItemQuantity'], labels=category_group.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    ax.set_title('Product Category Distribution')

    # Embedding Figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, padx=10)

# Function to create bar chart for total quantity ordered by product
def plot_bar_chart():
    product_group = inventory_df.groupby('ProductName').agg({'TotalItemQuantity': 'sum'}).sort_values(by='TotalItemQuantity', ascending=False)
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.bar(product_group.index, product_group['TotalItemQuantity'])
    ax.set_xlabel('Product Name')
    ax.set_ylabel('Total Item Quantity Ordered')
    ax.set_title('Total Quantity Ordered by Product')
    ax.tick_params(axis='x', rotation=90)

    # Embedding Figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, padx=10)

# Function to create line chart for profit over time
def plot_line_chart():
    profit_group = inventory_df.groupby('OrderDate').agg({'Profit': 'sum'})
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot_date(profit_group.index, profit_group['Profit'], linestyle='solid')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Profit')
    ax.set_title('Profit Over Time')
    ax.tick_params(axis='x', rotation=90)

    # Embedding Figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, padx=10)

# Button to show donut chart
btn_donut_chart = ttk.Button(button_frame, text="Show Category Distribution", command=plot_donut_chart)
btn_donut_chart.pack(side=tk.LEFT, padx=10, pady=10)

# Button to show bar chart
btn_bar_chart = ttk.Button(button_frame, text="Show Quantity by Product", command=plot_bar_chart)
btn_bar_chart.pack(side=tk.LEFT, padx=10, pady=10)

# Button to show line chart
btn_line_chart = ttk.Button(button_frame, text="Show Profit Over Time", command=plot_line_chart)
btn_line_chart.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:





# In[ ]:





# In[ ]:





# In[ ]:






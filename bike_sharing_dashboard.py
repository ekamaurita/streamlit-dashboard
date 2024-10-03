import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca data
all_df = pd.read_csv("all_data.csv")

# Fungsi untuk plot rata-rata pengguna sepeda berdasarkan hari kerja dan akhir pekan
def plot_workingday_usage():
    workingday_usage = all_df.groupby('workingday')['cnt_day'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x='workingday', y='cnt_day', data=workingday_usage)
    plt.title('Rata-rata Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan')
    plt.xlabel('Akhir Pekan (0) vs Hari Kerja (1)')
    plt.ylabel('Rata-rata Jumlah Pengguna')
    st.pyplot(plt)

# Fungsi untuk plot rata-rata pengguna sepeda berdasarkan kondisi cuaca
def plot_weather_usage():
    weather_usage = all_df.groupby('weathersit')['cnt_hour'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x='weathersit', y='cnt_hour', data=weather_usage)
    plt.title('Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca (1 = Cerah, 4 = Hujan Lebat)')
    plt.ylabel('Rata-rata Jumlah Pengguna')
    st.pyplot(plt)

# Fungsi untuk plot pengelompokan penggunaan sepeda
def plot_usage_category():
    bins = [0, 2000, 4000, 7000]
    labels = ['Low Usage', 'Medium Usage', 'High Usage']
    all_df['Usage_Category'] = pd.cut(all_df['cnt_day'], bins=bins, labels=labels)

    usage_workingday = all_df.groupby(['workingday', 'Usage_Category'])['cnt_day'].count().unstack()

    plt.figure(figsize=(10, 6))
    usage_workingday.plot(kind='bar', stacked=True, colormap='Set2')
    plt.title('Pengelompokan Penggunaan Sepeda pada Hari Kerja vs Akhir Pekan')
    plt.xlabel('Hari Kerja (1) vs Akhir Pekan (0)')
    plt.ylabel('Jumlah Pengguna')
    plt.xticks(rotation=0)
    plt.legend(title='Kategori Penggunaan')
    st.pyplot(plt)

# Fungsi untuk plot rata-rata pengguna sepeda berdasarkan jam dan kondisi cuaca
def plot_hour_weather_usage():
    hour_weather_usage = all_df.groupby(['hr', 'weathersit'])['cnt_hour'].mean().unstack()
    plt.figure(figsize=(12, 8))
    sns.heatmap(hour_weather_usage, cmap='Blues', annot=True, fmt='.1f')
    plt.title('Rata-rata Penggunaan Sepeda Berdasarkan Jam dan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jam')
    st.pyplot(plt)

# Membuat Layout Dashboard
st.title("Dashboard Penggunaan Sepeda")
st.header("Analisis Penggunaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan")
plot_workingday_usage()
st.header("Analisis Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
plot_weather_usage()
st.header("Pengelompokan Penggunaan Sepeda")
plot_usage_category()
st.header("Rata-rata Penggunaan Sepeda Berdasarkan Jam dan Kondisi Cuaca")
plot_hour_weather_usage()

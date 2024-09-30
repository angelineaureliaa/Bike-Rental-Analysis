import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

hour_df = pd.read_csv('data/hour.csv')
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
min_date = hour_df['dteday'].min()
max_date = hour_df['dteday'].max()
hour_df.reset_index(inplace=True)

with st.sidebar:
    st.title("Bike Rental (01 Jan 2011 - 31 Dec 2012)")

    criteria = st.selectbox(
        label ="Choose Analysis Category",
        options = ("Temperature", "Humidity", "Windspeed", "Holiday", "Season", "Time Frame", "Hour", "Day", "Month", "Year", "User Type", "RFM"))

    if criteria == 'Time Frame':
        start_date, end_date = st.date_input(
            label = "Time Frame", 
            min_value = min_date,
            max_value = max_date, 
            value = [min_date, max_date]
        )
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

#Temperature
#hitung rata2 rental per kategori suhu
def avg_rental_per_temp_all():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Temp_Category'] = pd.cut(hour_df['temp'], bins=bins, labels=labels)

    avg_rentals_per_temp_all = hour_df.groupby('Temp_Category')['cnt'].mean().reset_index()

    return avg_rentals_per_temp_all


#Humidity
def avg_rental_per_hum_all():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Hum_Category'] = pd.cut(hour_df['hum'], bins=bins, labels=labels)

    avg_rentals_per_hum_all = hour_df.groupby('Hum_Category')['cnt'].mean().reset_index()

    return avg_rentals_per_hum_all

#Windspeed
def avg_rental_per_wind_all():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Wind_Category'] = pd.cut(hour_df['windspeed'], bins=bins, labels=labels)

    avg_rentals_per_wind_all = hour_df.groupby('Wind_Category')['cnt'].mean().reset_index()

    return avg_rentals_per_wind_all

#Holiday
def avg_rental_per_holiday_all():
    avg_rentals_per_holiday_all = hour_df.groupby('holiday')['cnt'].mean().reset_index()

    return avg_rentals_per_holiday_all
    
#Season
def avg_rental_per_season_all():
    avg_rentals_per_season_all = hour_df.groupby('season')['cnt'].mean().reset_index()

    return avg_rentals_per_season_all


def total_rental_per_season_year():
    total_rentals_per_season_year = hour_df.groupby(['season', 'yr'])['cnt'].sum().reset_index()

    return total_rentals_per_season_year

#Time Frame
def total_rental_per_time_frame():
    total_rentals_per_time_frame = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)].groupby('dteday')['cnt'].sum().reset_index()

    return total_rentals_per_time_frame

def avg_rental_per_time_frame_user_type():
    avg_rentals_per_time_frame_user_type = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)].groupby('dteday')[['casual', 'registered']].mean().reset_index()  

    return avg_rentals_per_time_frame_user_type

#Hour
def total_rental_per_hour():
    total_rentals_per_hour = hour_df.groupby('hr')['cnt'].mean().reset_index()

    return total_rentals_per_hour

def total_rental_busy_hour():
    hour_df['busy'] = hour_df['hr'].apply(lambda x: 'Busy' if (7 <= x <= 9) or (17 <= x <= 19) else 'No')
    busy = hour_df.groupby('busy')['cnt'].sum().reset_index()

    return busy

def hourly_rental_per_day():
    hourly_rental_per_day = hour_df.groupby(['hr', 'weekday'])['cnt'].sum().reset_index()

    return hourly_rental_per_day

#Day
def total_rental_per_day():
    total_rentals_per_day = hour_df.groupby('weekday')['cnt'].mean().reset_index()

    return total_rentals_per_day

def avg_rental_weekday_weekend():
    hour_df['weekend'] = hour_df['weekday'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
    weekend = hour_df.groupby('weekend')['cnt'].sum().reset_index()

    return weekend

#Month
def total_rental_per_month():
    total_rentals_per_month = hour_df.groupby('mnth')['cnt'].sum().reset_index()

    return total_rentals_per_month

def total_rental_per_month_year():
    total_rentals_per_month_year = hour_df.groupby(['mnth', 'yr'])['cnt'].sum().reset_index()

    return total_rentals_per_month_year

#Year
def total_rental_per_year():
    total_rentals_per_year = hour_df.groupby('yr')['cnt'].sum().reset_index()

    return total_rentals_per_year

def total_rentar_per_year_month():
    total_rentals_per_year_month = hour_df.groupby(['yr', 'mnth'])['cnt'].sum().reset_index()

    return total_rentals_per_year_month

def total_rental_per_year_season():
    total_rentals_per_year_season = hour_df.groupby(['yr', 'season'])['cnt'].sum().reset_index()

    return total_rentals_per_year_season

#User Type
def avg_rental_per_temp_user_type():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Temp_Category'] = pd.cut(hour_df['temp'], bins=bins, labels=labels)

    avg_rentals_per_temp_user_type = hour_df.groupby('Temp_Category')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_temp_user_type


def avg_rental_per_hum_user_type():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Hum_Category'] = pd.cut(hour_df['hum'], bins=bins, labels=labels)

    avg_rentals_per_hum_user_type = hour_df.groupby('Hum_Category')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_hum_user_type

def avg_rental_per_wind_user_type():
    bins = [0, 0.33, 0.67, 1]
    labels = ['Low', 'Medium', 'High']
    hour_df['Wind_Category'] = pd.cut(hour_df['windspeed'], bins=bins, labels=labels)

    avg_rentals_per_wind_user_type = hour_df.groupby('Wind_Category')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_wind_user_type

def avg_rental_per_holiday_user_type():
    avg_rentals_per_holiday_user_type = hour_df.groupby('holiday')[['casual', 'registered']].mean().reset_index()
    avg_rentals_long = avg_rentals_per_holiday_user_type.melt(id_vars='holiday', 
                                                          var_name='user_type', 
                                                          value_name='average_rentals')
    

    return avg_rentals_long

def avg_rental_per_season_user_type():
    avg_rentals_per_season_user_type = hour_df.groupby('season')[['casual', 'registered']].mean().reset_index()
    avg_rentals_long = avg_rentals_per_season_user_type.melt(id_vars='season', 
                                                          var_name='user_type', 
                                                          value_name='average_rentals')

    return avg_rentals_long

def avg_rental_per_hour_user_type():
    avg_rentals_per_hour_user_type = hour_df.groupby('hr')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_hour_user_type

def avg_rental_per_day_user_type():
    avg_rentals_per_day_user_type = hour_df.groupby('weekday')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_day_user_type

def avg_rental_per_month_user_type():
    avg_rentals_per_month_user_type = hour_df.groupby('mnth')[['casual', 'registered']].mean().reset_index()

    return avg_rentals_per_month_user_type

def avg_rental_per_year_user_type():
    avg_rentals_per_year_user_type = hour_df.groupby('yr')[['casual', 'registered']].mean().reset_index()
    avg_rentals_long = avg_rentals_per_year_user_type.melt(id_vars='yr', 
                                                          var_name='user_type', 
                                                          value_name='average_rentals')

    return avg_rentals_long

#RFM
def rfm():
    today = hour_df['dteday'].max() + pd.Timedelta(days=1)
    rfm_df = hour_df.groupby('dteday').agg({
        'cnt': 'sum', 
    }).reset_index()

    rfm_df['Recency'] = (today - rfm_df['dteday']).dt.days
    rfm_df['Frequency'] = rfm_df['cnt']

    return rfm_df

st.header("Bike Rental Dashboard :sparkles::bike:")

if criteria == "Temperature":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("Average Rental per Temperature Category")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_temp_all = avg_rental_per_temp_all()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#003366', '#3366CC', '#66B3FF']
    sns.barplot(data=avg_rentals_per_temp_all, x='Temp_Category', y='cnt', palette=colors)

    plt.xlabel('Temperature Category', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)
    
    plt.figtext(0.5, -0.1, 
                "Low: 0 - 13.53 °C\n"
                "Medium: 13.54 - 27.47 °C\n"
                "High: 27.48 - 41 °C", 
                ha='center', fontsize=12, wrap=True)
    
    st.pyplot(fig)

if criteria == "Humidity":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("Average Rental per Humidity Category")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_hum_all = avg_rental_per_hum_all()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#003366', '#3366CC', '#66B3FF']
    sns.barplot(data=avg_rentals_per_hum_all, x='Hum_Category', y='cnt', palette=colors)

    plt.xlabel('Humidity Category', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)

    plt.figtext(0.5, -0.1, 
                "Low: 0 - 33 %\n"
                "Medium: 34 - 67 %\n"
                "High: 68 - 100 %", 
                ha='center', fontsize=12, wrap=True)
    
    st.pyplot(fig)

if criteria == "Windspeed":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("Average Rental per Windspeed Category")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    
    avg_rentals_per_wind_all = avg_rental_per_wind_all()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#003366', '#3366CC', '#66B3FF']
    sns.barplot(data=avg_rentals_per_wind_all, x='Wind_Category', y='cnt', palette=colors)

    plt.xlabel('Windspeed Category', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)
    
    plt.figtext(0.5, -0.1,
                "Low: 0 - 22.11 km/h\n"
                "Medium: 22.12 - 44.89 km/h\n"
                "High: 44.9 - 67 km/h", 
                ha='center', fontsize=12, wrap=True)
    
    st.pyplot(fig)

if criteria == "Holiday":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("Average Rental per Holiday")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_holiday_all = avg_rental_per_holiday_all()
    colors = ['#003366', '#3366CC', '#66B3FF']
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=avg_rentals_per_holiday_all, x='holiday', y='cnt', palette=colors)

    plt.xlabel('Holiday', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)

    plt.xticks([0, 1], ['No', 'Yes'])

    st.pyplot(fig)

if criteria == "Season":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    

    st.subheader("Average Rental per Season")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_season_all = avg_rental_per_season_all()
    colors = ['#003366', '#3366CC', '#66B3FF', '#99CCFF']
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=avg_rentals_per_season_all, x='season', y='cnt', palette=colors)

    plt.xlabel('Season', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)

    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Season per Year")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_season_year = total_rental_per_season_year()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#FF4500', '#FFA07A', '#FFA500', '#FFB347', '#FFCC99', '#FF3300', '#FF6666', '#FF9966', '#FF6600']
    sns.barplot(data=total_rentals_per_season_year, x='season', y='cnt', hue='yr', palette=colors)

    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)

    plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])
    plt.legend(title='Year')

    st.pyplot(fig)

if criteria == "Time Frame":
    col1, col2 = st.columns(2)

    with col1:
        filtered_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]
        total_rentals = filtered_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("Total Rental per Time Frame")
    st.write(f"Date Range: {start_date.strftime('%d %b %Y')} - {end_date.strftime('%d %b %Y')}")
    total_rentals_per_time_frame = total_rental_per_time_frame()
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=total_rentals_per_time_frame, x='dteday', y='cnt', marker = 'o')

    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Time Frame per User Type")
    st.write(f"Date Range: {start_date.strftime('%d %b %Y')} - {end_date.strftime('%d %b %Y')}")
    avg_rentals_per_time_frame_user_type = avg_rental_per_time_frame_user_type()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_time_frame_user_type['dteday'], y=avg_rentals_per_time_frame_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_time_frame_user_type['dteday'], y=avg_rentals_per_time_frame_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Date')

    st.pyplot(fig)


if criteria == "Hour":
    col1, col2 = st.columns(2)
    
    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    
    st.subheader("Total Rental per Hour")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_hour = total_rental_per_hour()
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=total_rentals_per_hour, x='hr', y='cnt', marker = 'o')
    plt.xticks(range(0, 24))

    plt.xlabel('Hour of Day (0-23)', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Busy Hour")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    busy = total_rental_busy_hour()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#FF4500', '#FFA07A', '#FFA500', '#FFB347', '#FFCC99', '#FF3300', '#FF6666', '#FF9966', '#FF6600']
    sns.barplot(data=busy, x='busy', y='cnt',  palette=colors)

    plt.xlabel('Hour', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.figtext(0.5, -0.1,
                "Busy: 7 - 9 AM & 5 - 7 PM\n"
                "No: Other Hours",
                ha='center', fontsize=12, wrap=True)

    st.pyplot(fig)

    st.write("")

    st.subheader("Hourly Rental per Day")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    hourly_rental_per_day = hourly_rental_per_day()
    fig = plt.figure(figsize=(12, 6))

    data = hour_df.groupby(['hr', 'weekday'])['cnt'].sum().reset_index()
    for day in range(7):
        day_data = data[data['weekday'] == day]
        plt.plot(day_data['hr'], day_data['cnt'])

    plt.title('Hourly Rental Count by Day')
    plt.xlabel('Hour of Day (0-23)')
    plt.ylabel('Total Rentals')
    plt.xticks(range(0, 24))
    plt.legend(title='Weekday', loc='upper right', labels=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
    
    st.pyplot(fig)

if criteria == "Day":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    
    st.subheader("Average Rental per Day")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_day = total_rental_per_day()
    colors = ['#001f3f','#003366','#00509E','#3366CC','#66B3FF','#99CCFF','#CCE5FF']

    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=total_rentals_per_day, x='weekday', y='cnt', palette=colors)

    plt.xlabel('Day of Week', fontsize=14)
    plt.ylabel('Average Rentals', fontsize=14)
    plt.xticks(range(0, 7), ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Weekday & Weekend")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    weekend = avg_rental_weekday_weekend()
    colors = ['#FF4500','#FFA07A', '#FFA500', '#FFB347', '#FFCC99', '#FF3300', '#FF6666', '#FF9966', '#FF6600']
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=weekend, x='weekend', y='cnt', palette=colors)

    plt.xlabel('Day Type', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.figtext(0.5, -0.1,
                "Weekday: Mon - Fri\n"
                "Weekend: Sat - Sun", 
                ha='center', fontsize=12, wrap=True)
    plt.xticks([0, 1], ['Weekday', 'Weekend'])

    st.pyplot(fig)

if criteria == "Month":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    
    st.subheader("Total Rental per Month")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_month = total_rental_per_month()
    colors = ['#001f3f', '#003366', '#00509E', '#3366CC', '#66B3FF', '#99CCFF', '#CCE5FF', '#00264D', '#004080', '#6699CC', '#99B3E6', '#CCD6FF']
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=total_rentals_per_month, x='mnth', y='cnt', palette=colors)
    
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.xticks(range(1, 13))

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Month per Year")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_month_year = total_rental_per_month_year()
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=total_rentals_per_month_year, x='mnth', y='cnt', hue='yr', palette=colors, marker = 'o')

    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.xticks(range(1, 13))
    plt.figtext(0.5, -0.1,
                "Year :\n"
                "0: 2011\n"
                "1: 2012",
                ha='center', fontsize=12, wrap=True)


    st.pyplot(fig)

if criteria == "Year":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    
    st.subheader("Total Rental per Year")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_year = total_rental_per_year()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#003366', '#3366CC', '#66B3FF']
    sns.barplot(data=total_rentals_per_year, x='yr', y='cnt', palette=colors)

    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.xticks([0, 1], ['2011', '2012'])

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Year per Month")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_year_month = total_rentar_per_year_month()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#003300', '#006600', '#009900', '#00CC00', '#33CC33', '#66CC66', '#99CC99', '#CCCC00', '#D9D900', '#E5E500', '#FFFF00', '#FFFFCC']
    sns.barplot(data=total_rentals_per_year_month, x='yr', y='cnt', hue='mnth', palette=colors)

    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.xticks([0, 1], ['2011', '2012'])
    plt.legend(title='Month')

    st.pyplot(fig)

    st.write("")

    st.subheader("Total Rental per Year per Season")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    total_rentals_per_year_season = total_rental_per_year_season()
    fig = plt.figure(figsize=(12, 6))
    colors = ['#FF4500', '#FF6347', '#FF7F50', '#FF8C00', '#FFA07A', '#FFA500', '#FFB347', '#FFCC99', '#FF3300', '#FF6666', '#FF9966', '#FF6600']
    sns.barplot(data=total_rentals_per_year_season, x='yr', y='cnt', hue='season', palette=colors)

    plt.xlabel('Season', fontsize=14)
    plt.ylabel('Total Rentals', fontsize=14)
    plt.xticks([0, 1], ['2011', '2012'])
    plt.figtext(0.5, -0.2,
                "Season :\n"
                "1: Spring\n"
                "2: Summer\n"
                "3: Fall\n"
                "4: Winter",
                ha='center', fontsize=12, wrap=True)
    plt.legend(title='Season')


    st.pyplot(fig)

if criteria == "User Type":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)
    
    st.subheader("Average Rental per Temperature Category per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_temp_user_type = avg_rental_per_temp_user_type()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_temp_user_type['Temp_Category'], y=avg_rentals_per_temp_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_temp_user_type['Temp_Category'], y=avg_rentals_per_temp_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Temperature Category')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Humidity Category per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_hum_user_type = avg_rental_per_hum_user_type()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_hum_user_type['Hum_Category'], y=avg_rentals_per_hum_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_hum_user_type['Hum_Category'], y=avg_rentals_per_hum_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Humidity Category')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Windspeed Category per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_wind_user_type = avg_rental_per_wind_user_type()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_wind_user_type['Wind_Category'], y=avg_rentals_per_wind_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_wind_user_type['Wind_Category'], y=avg_rentals_per_wind_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Windspeed Category')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Holiday per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_holiday_user_type = avg_rental_per_holiday_user_type()
    colors = ['#003366', '#3366CC', '#66B3FF']
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='holiday', y='average_rentals', hue='user_type', data=avg_rentals_per_holiday_user_type, palette=colors, ax=ax)
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Holiday (0 = No, 1 = Yes)')
    ax.legend(title='User Type')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Season per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_season_user_type = avg_rental_per_season_user_type()
    colors = ['#FF4500', '#FFA07A', '#FFA500', '#FFB347', '#FFCC99', '#FF3300', '#FF6666', '#FF9966', '#FF6600']
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='season', y='average_rentals', hue='user_type', data=avg_rentals_per_season_user_type, palette=colors, ax=ax)
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Season (1: Spring, 2: Summer, 3: Fall, 4: Winter)')
    ax.legend(title='User Type')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Hour per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_hour_user_type = avg_rental_per_hour_user_type()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_hour_user_type['hr'], y=avg_rentals_per_hour_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_hour_user_type['hr'], y=avg_rentals_per_hour_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Hour')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Day per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_day_user_type = avg_rental_per_day_user_type()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_day_user_type['weekday'], y=avg_rentals_per_day_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_day_user_type['weekday'], y=avg_rentals_per_day_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Day')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Month per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_month_user_type = avg_rental_per_month_user_type()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=avg_rentals_per_month_user_type['mnth'], y=avg_rentals_per_month_user_type['casual'], label='Casual', ax=ax, marker = 'o')
    sns.lineplot(x=avg_rentals_per_month_user_type['mnth'], y=avg_rentals_per_month_user_type['registered'], label='Registered', ax=ax, marker = 'o')
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Month')

    st.pyplot(fig)

    st.write("")

    st.subheader("Average Rental per Year per User Type")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    avg_rentals_per_year_user_type = avg_rental_per_year_user_type()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='yr', y='average_rentals', hue='user_type', data=avg_rentals_per_year_user_type, palette=colors, ax=ax)
    ax.set_ylabel('Average Rentals')
    ax.set_xlabel('Year (0: 2011, 1: 2012)')
    ax.legend(title='User Type')

    st.pyplot(fig)

if criteria == "RFM":
    col1, col2 = st.columns(2)

    with col1:
        total_rentals = hour_df['cnt'].sum()
        st.metric(label="Total Rentals", value=total_rentals)

    st.subheader("RFM Analysis")
    st.write("Date Range: 01 Jan 2011 - 31 Dec 2012")
    rfm_df = rfm()
    fig = plt.figure(figsize=(12, 6))
    sns.scatterplot(data=rfm_df, x='Recency', y='Frequency', size='cnt', sizes=(20, 200), hue='cnt', palette='viridis')

    plt.xlabel('Recency (days)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend(title='Total Rentals')

    st.pyplot(fig)

    
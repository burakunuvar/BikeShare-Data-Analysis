# START
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# FUNCTION 1:
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=(input('>>> Would you like to see data for Chicago, New York City, or Washington?: ')).lower()
        if city in CITY_DATA :
            print(f">>> Great! We will analyze bikeshare data of {city} \n ")
            break
        else:
            print(">>> Hmm, please retry- available cities are: Chicago, New York City, or Washington\n")

    while True:
        filter_by=(input(""">>> How would you like to filter data ? Please choose one of options below:
    Type "month" to filter based on month only
    Type "day" to filter based on day of the week only
    Type "both"to filter
    Type "none" for nofilters
    :"""))
        month = 'all'
        day = 'all'
        # TO DO: get user input for month (all, january, february, ... , june)
        if filter_by.lower() == 'month':
            month = input('>>> filter by which month? (january, february, march ... ): ').capitalize()
            print(f">>> Great! We will analyze bikeshare data in {month} \n ")
            break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter_by.lower() == 'day':
            day = input('>>> filter by which day of the week? (monday, tuesday, wednesday ... ): ').capitalize()
            print(f">>> Great! We will analyze bikeshare data in {day} \n ")
            break
        elif filter_by.lower() == 'both':
            month = input('>>> filter by which month? (january, february, march ...): ').capitalize()
            day = input('>>> filter by which day of the week? (monday, tuesday, wednesday ... ): ').capitalize()
            print(f">>> Great! We will analyze bikeshare data in {month} for {day} \n ")
            break
        elif filter_by.lower() == 'none':
            print(f">>> no filters ; ) So all months and all days of the week will be included in analysis ")
            break
        print(">>> Hmm, please retry, you can only filter by 'month' or 'day of the week' ! ")

    print('-'*40)
    return city, month, day,filter_by

# FUNCTION 2:
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour, month and day of week from Start Time to create new columns
    df["Hour"]=df['Start Time'].dt.hour
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] =  df['Start Time'].dt.weekday_name

    #filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march','april',
                  'may', 'june','july','august',
                  'september','october','november','december']
        month = months.index(month.lower())+1
        # filter by month to create the new dataframe
        df = df[df['Month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.capitalize()]

    return df


# FUNCTION 3:

def time_stats(df,filter_by):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month :
    #df["month"].mode()[0]


    # TO DO: display the most common day of week :
    #df["day_of_week"].mode()[0]


    # TO DO: display the most common start hour :
    #df["hour"].mode()[0]

    months = ['january', 'february', 'march','april',
                  'may', 'june','july','august',
                  'september','october','november','december']
    selected_month = months[df["Month"].values[0]-1]
    selected_day = df["Day of Week"].values[0]

    if filter_by=='none':
        popular_month = df["Month"].mode()[0]
        count_popular_month = (df['Month'] == popular_month).sum()
        popular_day = df["Day of Week"].mode()[0]
        count_popular_day = (df['Day of Week'] == popular_day).sum()
        popular_hour = df["Hour"].mode()[0]
        count_popular_hour = (df['Hour'] == popular_hour).sum()
        print(f""">> >when there are no filters:
    the most popular month: {popular_month} Count: {count_popular_month}
    the most popular day of week: {popular_day} Count: {count_popular_day}
    the most common start hour: {popular_hour} Count: {count_popular_hour}
    """)

    elif filter_by=='month':
        popular_day = df["Day of Week"].mode()[0]
        count_popular_day = (df['Day of Week'] == popular_day).sum()
        popular_hour = df["Hour"].mode()[0]
        count_popular_hour = (df['Hour'] == popular_hour).sum()
        print(f""">>> Data is filtered by {selected_month}:
    the most popular day of week: {popular_day} Count: {count_popular_day}
    the most common start hour: {popular_hour} Count: {count_popular_hour}
    """)

    elif filter_by=='day':
        popular_month = df["Month"].mode()[0]
        count_popular_month = (df['Month'] == popular_month).sum()
        popular_hour = df["Hour"].mode()[0]
        count_popular_hour = (df['Hour'] == popular_hour).sum()
        print(f""">>> Data is filtered by {selected_day} :
    the most popular month: {popular_month} Count: {count_popular_month}
    the most common start hour: {popular_hour} Count: {count_popular_hour}
    """)

    elif filter_by=='both':
        popular_hour = df["Hour"].mode()[0]
        count_popular_hour = (df['Hour'] == popular_hour).sum()
        print(f""">>> Data is filtered by both {selected_day} and {selected_month}:
    the most common start hour: {popular_hour} Count: {count_popular_hour}
    """)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# FUNCTION 4:
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start= df["Start Station"].mode()[0]
    count_start= (df['Start Station'] == most_used_start).sum()

    # TO DO: display most commonly used end station
    most_used_stop= df["End Station"].mode()[0]
    count_stop= (df['End Station'] == most_used_stop).sum()

    # TO DO: display most frequent combination of start station and end station trip
    station_routes = df.groupby(['Start Station','End Station']).size()
    most_frequent_route = station_routes.idxmax()

    #TO DO : display how many times this combination was used
    station_route_counts=df.groupby(['Start Station','End Station']).size().reset_index(name='route_counts')
    count_most_frequent = station_route_counts['route_counts'].max()

    print(f""">>> Station Stats:
the most commonly used start station: {most_used_start}; used {count_start} times
the most commonly used end station: {most_used_stop}; used {count_stop} times
the most common route is from "{most_frequent_route[0] }" to "{ most_frequent_route[1] }"; used {count_most_frequent} times
    """)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# FUNCTION 5:
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time:
    #df["Trip Duration"].sum()

    # TO DO: display mean travel time
    #df["Trip Duration"].mean()

    print(f""">>> Trip Duration Stats
the total travel time is: {df["Trip Duration"].sum()} seconds
the total number of trips: {len(df["Trip Duration"])} seconds
the average travel time: {df["Trip Duration"].mean()} seconds
    """)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# FUNCTION 6:
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    counts_user_types = "No user_type data stored"
    counts_gender = "No gender data stored"
    birth_years = None
    # TO DO: Display counts of user types

    try:
        counts_user_types=df['User Type'].value_counts()
        print(f">>> The breakdown of User Types:\n{counts_user_types}\n")
    except KeyError as e:
        print(f"{e} data not stored")

    try:
        counts_gender=df['Gender'].value_counts()
        print(f">>> The breakdown of Gender:\n{counts_gender}\n")
    except KeyError as e:
        print(f"{e} data not stored")

    try:
        birth_years={
            "min":df['Birth Year'].min(),
            "max":df['Birth Year'].max(),
            "most_common": df['Birth Year'].mode()[0]
        }
        print(f""">>> The breakdown of Birth Year:
earliest year of birth: {int(df['Birth Year'].min())}
most recent year of birth: {int(df['Birth Year'].max())}
most common year of birth: {int(df['Birth Year'].mode()[0])}
""")
    except KeyError as e:
        print(f"{e} data not stored")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day,filter_by = get_filters()
        df = load_data(city, month, day)
        time_stats(df,filter_by)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        sample_data = input('\nWould you like view sample data ? Enter yes or no.\n')
        if sample_data.lower() == 'yes':
            print(df.head(10))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_names=['chicago','new york city','washington']
        city=input('1. would you like to view statistics of chicago or new york city or washington?: ').lower()
        if city in city_names:
            break
        else:
            print('\nPlease enter name of city from named cities above: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months_=['all','january','february','march','april','may','june']
        month=input('2. Which month? all, January, February, March, April, May or June :').lower()
        if month in months_:
            break
        else:
            print('\nPlease enter the input chosen from above options :')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days_=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        day=input('3. Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all :').lower()
        if day in days_:
            break
        else:
            print('\nEnter input chosen from above options :')

    print('-'*40)
    return city, month, day


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
    #load data into pandas dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    #change start time column to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    #extract month and day of a week from Start Time to add month and day columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    #filter data by month
    if month!='all':
        months=['january','february','march','april','may','june']
        #create new dataframe fitltered with a month
        df=df[df['month']==(months.index(month)+1)]
        
    #filter data by day
    if day!='all':
        df=df[df['day_of_week']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day of a week is ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    #create a new column hour from Start Time
    df['hour']=df['Start Time'].dt.hour
    print('the most common start hour is ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most used start station is :',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most used end station is :',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start and end station :',(df['Start Station']+df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def convert_time_to_preferred_format(seconds):
    hours_,seconds=divmod(seconds,3600)
    minutes_,seconds=divmod(seconds,60)
    return hours_,minutes_,seconds

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #calculate total trip duration
    total_duration=df['Trip Duration'].sum()
    #convert to preferred time format
    hours,minutes,seconds=convert_time_to_preferred_format(total_duration)  
    # TO DO: display total travel time
    print('/ntotal travel time is {} hours {} minutes {} seconds'.format (hours,minutes,seconds))
    
    #calculate mean travel time
    mean_duration=df['Trip Duration'].mean()
    #convert time to preffered formart
    hours,minutes,seconds=convert_time_to_preferred_format(mean_duration)
    # TO DO: display mean travel time
    print('\naverage travel time is {} hours {} minutes {} seconds'.format(hours,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of each user type :\n',user_types)
    # TO DO: Display counts of gender
    if city== 'chicago' or city== 'new york city':
        gen=df['Gender'].value_counts()
        print('\ncount of each gender :\n',gen)
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob=df['Birth Year'].min()
        print('\nearliest year of birth is :',earliest_yob)
        most_recent_yob=df['Birth Year'].max()
        print('\nmost recent year of birth is :',most_recent_yob)
        most_common_yob=df['Birth Year'].mode()
        print('\nmost common year of birth is :',most_common_yob)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_trips(df):
    user_options=['yes','no']
    start=0
    end=5
    print('\n------ VIEW INDIVIDUAL\'S TRIP INFORMATION-------')
    while True:
        
        option_=input("\nwould you like to view individual trip data? type 'yes' or 'no' :").lower()
        if option_ in user_options:
            if option_=='yes':
                
                # check if we have not reached end of data
                if end<=df.shape[0]:
                    data=df.iloc[start:end,:]
                    print(data)
                else:
                    end=df.shape[0]
                    data=df.iloc[start:end,:]
                    print(data)
                    print('\n---you have reached the end of data-----')
                    break
                start=start+5
                end=end+5
               
                    
            else:
                break
        else:
            print("\nInput is not valid (please enter yes or no)\n")
        
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_trips(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Load data
    print("Loading data...")
    data = pd.read_csv(r"uber.csv")
    print("Data loaded successfully!")

    # Add derived columns
    data["Date/Time"] = pd.to_datetime(data["Date/Time"])
    data["Day"] = data["Date/Time"].apply(lambda x: x.day)
    print("Data processing complete!")

    # Which day the Uber trips were highest
    sns.set(rc={'figure.figsize': (12, 10)})
    #You Can Replace "Day" with "Weekday" or "Hour"
    sns.histplot(data["Day"], bins=31)
    plt.title("Distribution of Rides by Day")
    plt.show()

    # The density of Uber trips according to the regions of the New Your city
    data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
    figsize=(12, 8), cmap=plt.get_cmap('jet'))
    plt.title("Uber Trips Analysis")
    plt.legend()
    plt.show()

    # Correlation of Weekday and Hour
    df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
    df = df.unstack()
    sns.heatmap(df, annot=False)

except Exception as e:
    print(f"An error occurred: {e}")




    

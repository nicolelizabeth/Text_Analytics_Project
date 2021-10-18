import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
scored = pd.read_csv('C:/Users/jackm/Documents/analytics/fall2/text/scored_reviews.csv')

scored["posted_date"] = pd.to_datetime(scored["posted_date"])
mask = (scored['posted_date'] > '2018-1-1')
scored = scored.loc[mask]
scored["posted_date"] = scored["posted_date"].dt.date
positive_avg = scored.groupby("posted_date").mean()
positive_avg

plt.figure( figsize = ( 12, 5))
  
sns.lineplot(x = 'posted_date',
             y = 'Positive',
             data = scored,
             label = 'Positive review score')

sns.lineplot(x = 'posted_date',
             y = 'Negative',
             data = scored,
             label = 'Negative review score')

scored["posted_date"] = pd.to_datetime(scored["posted_date"])
scored['WeekDate'] = scored.apply(lambda row: row['posted_date'] - dt.timedelta(days=row['posted_date'].weekday()), axis=1)
perweek = scored.groupby('WeekDate').mean()

sns.lineplot(x = 'WeekDate',
             y = 'Positive',
             data = perweek,
             label = 'Positive review score')

sns.lineplot(x = 'WeekDate',
             y = 'Negative',
             data = perweek,
             label = 'Negative review score')

perweek.to_csv('C:/Users/jackm/Documents/analytics/fall2/text/perweek.csv')

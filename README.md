# Ford GoBike System Data Analysis

## by Oluwaseyi Daniel

## Dataset

> This data set includes information about individual rides made in a bike-sharing system covering the greater San Francisco Bay area. The data was collected from e-bikes used over a period of time. There are 16 columns provided, below are some that were of interest:  
>
>* `duration_sec` - This the amount of time that the bike is used, measured in seconds.
>* ``start_time`` - This is the timestamp that shows when the session began.
>* ``end_time`` - This is the timestamp that shows when the session ended.
>* ``start_station_latitude`` - As the name implies.
>* ``start_station_longitude`` - As the name implies.
>* ``end_station_latitude`` - As the name implies.
>* ``end_station_longitude``  - As the name implies.
>* ``bike_id`` - This is the unique identification given to each bike.
>* ``user_type`` - states whether the user is a customer or subscriber.
>* ``member_birth_year`` - The year the user was born.
>* ``member_gender`` - The gender of the user.
>
> I had to make some transformations based on the given data. First I had to derive the ages of users based on the `member_birth_year` column. Then I used a geolocation package `geopy` to calculate the average distance travelled based on the coordinates given in the dataset.

## Summary of Findings
  > From my analysis on this dataset, I have made the following findings:  
  >
  > * Majority of the users of this service are the male gender, with aproximately 75% of the population serviced. They tend to use the bikes to travel longer distances and also use them for longer, however this can't be seen by using the mean due to the sheer magnitude of their population.  
  > * The difference in the population of customers vs subscribers is glaring. Subscribers have a larger range of ages and distance travelled with the bikes.
  > * Users are mostly between ages 20 and 50. and they tend to use the bikes for not more than 3 km at a go. Younger people seem to travel longer distances and older people travel shorter distances.  
  > * Bikes with id above 4000 have seen more usage and have travelled more distance than the others. This maybe due to where they are located or maybe the bikes with this id are more durable or have more battery life.  

## Key Insights for Presentation
 > These are the Insights I would focus on in the presentation:  
 >
 > * Majority of the users of this service are the male gender, with aproximately 75% of the population serviced. They tend to use the bikes to travel longer distances and also use them for longer, however this can't be seen by using the mean due to the sheer magnitude of their population. 
 > * Users are mostly between ages 20 and 50. and they tend to use the bikes for not more than 3 km at a go. Younger people seem to travel longer distances and older people travel shorter distances.
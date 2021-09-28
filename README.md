### Overview 
For this project, Python and SQLAlchemy were used to gather statistics on weather data for the months of June and December in Hawaii from the given dataset in a sqlite file. The end goal is to determine wheter or not a surf shop would be a sucessful business idea throughtout the year depending on the history of weather. The jupyter notebook file SurfsUp_Challenge is where this code resides.

### Results 
After filtering the dataset to only include the months of June and December, the describe() function was used to produce the following dataframes for each month's recorded temperatures:

<img width="150" alt="june_temps" src="https://user-images.githubusercontent.com/85901073/135123081-3caaa3d2-2057-4aa1-ae17-25f0d10de5a2.png">

<img width="190" alt="dec_temps" src="https://user-images.githubusercontent.com/85901073/135123107-67a74410-0869-433e-8bb7-00f3987d559a.png">

From the two dataframes, it can be seen that 
- The mean temperature in both months is in the low seventies with a standard deviation of about three degrees. So the temperature appears to be consistent enough at the halfways points in the year so that a surf shop can stay in business all year instead of only seasonal.  
- However, the minimum temperature in June is higher than the minumum in December, approximating nearly eight degrees colder in Decemeber than in June. The difference is not necessarily too drastic that the surf shop would not survive around this time, but just points to the fact that perhaps there would be fewer days of operation for the shop around the Decemeber months, or that there would just be fewer customers on those days who are willing to bear the colder temperatures out on the water.
- Fifty percent of the recorded temperatures fall between 73º and 77º in June, and 69º and 74º in Decemeber, a range that seems managable for a surf shop 

### Summary 
Given the three points above, the temperatures in June and Decemeber generally have a small enough difference that a surf shop would be able to handle when it comes to generating enough business regardless of the time of year. More analysis should be done on, however, to be sure. Another possible query would be to determine the amount of rainfall during these two months and how that generally relates to temperature. For example, a month filled with heavy amounts of precipitation with the addition of colder temperatures is not ideal for a surf shop, but the loss of expenses could be offset by the revenue generated during the better months of the year which have both warmer temperatures and less rainfall. A query could also be made to find out how the temperature changes throughout the year. 


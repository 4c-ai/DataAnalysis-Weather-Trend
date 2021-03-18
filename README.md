# DataAnalysis-Weather-Trend
DataAnalysis-Weather Trend
Overview
As part of this project assignment submission, I have analyzed the data set on average temperature, year on year basis for the global as well as UAE capital, Abu Dhabi. To generate the data sets SQL query is used, whereas for analysis and observation Python is used. I have mentioned step by step guide to reach at the observation.
SQL work
Step1
As a start point, I have looked at the data set by selecting * from all the tables
Dataset city_list
SELECT *
FROM city_list
This table city_list contains Country and City names 
Dataset global_data
SELECT *
FROM global_data
This table contains year and average temperature
Dataset city_data
SELECT *
FROM city_data
This table contains year, city and average temperature
Step2
Checking my city , whether it exist in the data set or not . My project city is my city of residence i.e. Abu Dhabi
SELECT *
 		FROM city_list WHERE Country='United Arab Emirates'
    		AND city = 'Abu Dhabi';
Step3
Check the average temperature of Abu Dhabi from the city data list
SELECT avg_temp,year,city,country
 		FROM city_data
 		WHERE city='Abu Dhabi';
Step4
As average temperature exists in global_data and city_data, the field names in each data set need to be uniquely identified in a common data set and for that table join is required. So renaming the field name avg_temp in both the tables.
ALTER TABLE city_data
	RENAME COLUMN avg_temp to CAVG;
ALTER TABLE global_data
	RENAME COLUMN avg_temp to GAVG;
Step5
Now update join the tables. This data set now created gives yearly average of Abu Dhabi and corresponding yearly Global average. Single CSV is generated.
SELECT global_data.year,global_data.gavg,city_data.cavg
FROM global_data JOIN city_data
ON global_data.year = city_data.year
WHERE city LIKE ‘Abu Dhabi’;
CSV is downloaded now for analysis and plot in python.
Python work
Step1
Import libraries in Jupyter notebook
Pandas to work on the data set, Numpy to work on moving average and Matplotlib and Seaborn for ploting
Step2
Create the dataframe.
Df = pd.read_csv(‘abudhabi_avg_temp.csv’)
Step3
Checking moving average for Global average and Abudhabi average by plotting
 
Fig 1
 
Fig 2
 
Fig 3
Observations
•	Fig 1 shows up to 1950, the average temperature used to be in the range of 8.8 degree Celsius and since 1980 onwards there has been a sudden spike in the temperature
Rapid industrialization can be attributed to this change in world climatic condition
•	Fig 2 shows the similar data for Abu Dhabi. The average temp during 1950 used to be in the range of 26.7, but since 1990 the trend shows a cause of concern.
•	Fig 3 shows a grim picture of Abu Dhabi temp, compared to the world, even though global temperature across cities is growing at an alarming rate.
•	The need of the hour is to have a serious Climate change policy to be introduced by world Governments including UAE Govt (Even though this is not a direct inference from the data analysis)



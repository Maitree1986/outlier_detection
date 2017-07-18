# outlier_detection
This is a reusable module for outlier detection
If you have number of categorical variables with you and you want to find the most uncommon pattern of the categorical variables. 
You just need to give all the categorical variables and the threshold limit of the uncommon pattern.
For example if you want to find all the patterns which occurs less than or equal to 1 times in the data, you can give the threshold as 1. 
The module will give an array of 1 and -1. The array will have -1 for the records where the count of the record pattern is less than or 
equal to 1. The array will have 1 for the records where the count of the record pattern is more than 1 .  

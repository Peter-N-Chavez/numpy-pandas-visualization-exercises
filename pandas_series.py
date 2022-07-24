import pandas as pd
import numpy as np
from pydataset import data

a = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato",
               "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

#    Determine the number of elements in fruits.

print(len(a))

#    Output only the index from fruits.

print(a.index)

#    Output only the values from fruits.

print(a.values)

#    Confirm the data type of the values in fruits.

print(a.dtypes)

#    Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

print(a.head())

#    Run the .describe() on fruits to see what information it returns when called on a Series with string values.

print(a.describe())

#    Run the code necessary to produce only the unique string values from fruits.

print(a.unique())

#    Determine how many times each unique string value occurs in fruits.

print(a.value_counts())

#    Determine the string value that occurs most frequently in fruits.

b = a.value_counts().head(1)
print(b)

#    Determine the string value that occurs least frequently in fruits.

b= a.value_counts().tail(1)
print(b)

#    Capitalize all the string values in fruits.

b = a.str.capitalize()
print(b)

#    Count the letter "a" in all the string values (use string vectorization).

b = a.str.count("a")
print(b)

#    Output the number of vowels in each and every string value.

b = a.str.count("[aeiou]")

#    Write the code to get the longest string value from fruits.

b = a[a.str.len().idxmax()]
print(b)

#    Write the code to get the string values with 5 or more letters in the name.

b = a[a.str.len() >= 5]
print(b)

#    Find the fruit(s) containing the letter "o" two or more times.

b = a[a.str.count("o") >= 2]
print(b)

#    Write the code to get only the string values containing the substring "berry".

b = a[a.str.contains("berry")]
print(b)

#    Write the code to get only the string values containing the substring "apple".

b = a[a.str.contains("apple")]
print(b)

#    Which string value contains the most vowels?

b = a[a.str.count("[aeiou]").idxmax()]
print(b)

a = list("hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejil" 
        "zjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy")
b = pd.Series(a)

#    Which letter occurs the most frequently in the letters Series?

c = b.value_counts().idxmax()
print(c)

#    Which letter occurs the least frequently?

c = b.value_counts(sort = True).idxmin()
print(c)

#    How many vowels are in the Series?

c = b.apply(lambda v: v.lower() in "aeiou").value_counts()
print(c)

#   34 vowels

#    How many consonants are in the Series?

#   166 consonants

#    Create a Series that has all of the same letters but uppercased.

c = b.str.upper()
print(c)

#    Create a bar plot of the frequencies of the 6 most commonly occuring letters.

c = b.value_counts().head(6).plot.bar()
print(c)

a = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
    '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', 
    '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']
b = pd.Series(a)

#    What is the data type of the numbers Series?

print(b.dtype)

#    How many elements are in the number Series?

print(len(b))

#    Perform the necessary manipulations by accessing Series attributes and methods to 
#    convert the numbers Series to a numeric data type.

c = b.str.strip('$').str.replace(',','_').astype(float)
print(c)

#    Run the code to discover the maximum value from the Series.

print(c.max())

#    Run the code to discover the minimum value from the Series.

print(c.min())

#    What is the range of the values in the Series?

print(c.max() - c.min())

#    Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

print(c.value_counts(bins = 4))

#    Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

print(c.value_counts(bins = 4).sort_index().plot.bar(title="Ranges of Invoices").set(xlabel="Ranges", ylabel="Count"))


a = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
b = pd.Series(a)

#    How many elements are in the exam_scores Series?

print(len(b))

#    Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

print(b.describe())
print(b.median())

#    Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

print(b.plot.hist(title = "Distribution of Exam Scores").set(xlabel = "Exam Scores", ylabel = "Frequency"))

#    Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
#    Add the necessary points to the highest grade to make it 100, and add the same number of points to 
#    every other score in the Series as well.

c = (100 - b.max()) + b
print(c)

#    Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of 
#    letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. 
#    Save this as a Series named letter_grades.

final_g = pd.cut(c, bins=[0,60,70,80,90,100], labels=['F','D','C','B','A'])
print(final_g)

#    Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

print(final_g.value_counts().sort_index(ascending=False).plot.bar(title = "Letter Grades").set(xlabel = "Exam Letter Grades (after curve)", ylabel = "Frequency"))

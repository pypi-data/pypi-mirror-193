
Python Package: ‘distributions_jks’ Documentation

Introduction

This python package is an encapsulation of related classes and methods based on distributions in statistics. Distribution in statistics is a mathematical concept that represents how numbers are occurring, their possible values with probabilities.
In this package there are three classes, each defined in separated modules. They are:
1.	Distribution
2.	Gaussian
3.	Binomial
These classes consist of attributes and methods useful for calculating simple statistical measures. Such as mean, standard deviation and probability density. There are also methods to visualize the distributions in an XY plane.

DEPENDENCIES
This package makes use of two more packages/modules. They are:
-	Matplotlib
-	Math


Distribution

Distribution class represents a general distribution of numbers. Any distribution consists of two attributes, mean and standard deviation. The Distribution class also provides a method for reading data from a text file.

ATTRIBUTES
data_list: list of ints - represents a list of numbers read from a data file.
mean: float – represents the mean of a distribution (list of numbers) – default: 0.
stdev: float – represents the standard deviation of a distribution (list of numbers) – default: 1

METHODS
__init__()
This instance initializing method executes at the time of instance creation. This function defines the instance variables mean and stdev. If arguments are provided mean and stdev are initialized with the values. Or else default values are given.
Arguments
self: An instance of Distribution class
mean_v: represents the mean of a distribution
stdev_v: represents the standard deviation of a distribution

read_data_file()
This method reads a text file consisting of numbers into the data_list attribute as a list of ints. The file should be a text file and formatted in such a way that each line only consists of a single number.
Note: Even if we provide float values in the file, this method truncates the fractional part as it typecasts the values to int values.
Arguments
self: An instance of Distribution class
file_path: The relative or absolute path of the text file where the data is stored.


Gaussian

This class, Gaussian, is a specialized distribution of numbers inheriting the Distribution class. It consists of the same attributes as of Distribution class and extra methods for dealing with new problems.

ATTRIBUTES
data_list: list of ints - represents a list of numbers read from a data file.
mean: float – represents the mean of a distribution (list of numbers) – default: 0.
stdev: float – represents the standard deviation of a distribution (list of numbers) – default: 1

METHODS
__init__() – Same as of Distribution class

read_data_file_() – Same as of Distribution class

calculate_mean()
This method calculates the mean value of the data_list and returns the same.
Arguments
self: An instance of Gaussian class
Returns
float – represents the mean value of the data_list

calculate_stdev()
This method calculates the standard deviation value of the data_list and returns the same.
Arguments
self: An instance of Gaussian class
sample: boolean – represents whether the data_list is a sample (True) or population (False)
Returns
float – represents the standard deviation value of the data_list.

probability_density()
This method calculates the probability density function on the data_list based on point and returns the same.
Arguments
self: An instance of Gaussian class
point: int – represents the point at which the function calculates the probability density.
Returns
float – represents the probability density value on the data_list at the point.

plot_histogram()
This function outputs a histogram of the instance variable data using matplotlib pyplot library. It takes nothing as an argument except the self and draws the plot based on the data_list itself.

plot_histogram_probability_density()
This function plots the normalized histogram of the data and a plot the probability density function along the same range. It take n_spaces as an argument and returns the X and Y axes values for the probability density function plot
Arguments
self: An instance of Gaussian class
n_spaces: int – represents number of data points
Returns
list – X axes values for probability density function plot
list – Y axes values for probability density function plot

__add__()	
This function adds two Gaussian distribution instances together to create a new Gaussian distribution with different mean and standard deviation (stdev) values based on the given mean and stdev values of the provided two Gaussian instances. It overloads the + operator so that it can work with Gaussian class as a binary operator. It returns the new Gaussian instance.
Arguments
self: An instance of Gaussian class
other: Gaussian – represents the other Gaussian instance we are adding the self 
Returns
Guassian – A new Gaussian instance obtained from adding the self and other

__repr__()
This function represents the Gaussian instances as a string consisting of mean and standard deviation. It can used to directly print the contents of Gaussian instance without directly accessing the attributes.


Binomial

This class, Binomial, is a specialized distribution of numbers inheriting the Distribution class as well. It consists of the same attributes as of Distribution class and extra methods for dealing with new problems.

ATTRIBUTES
data_list: list of ints - represents a list of numbers read from a data file.
size: int – represents the number of values present in the Binomial distribution.
prob: float – represents the probability of the Binomial distribution.
mean: float – represents the mean of a distribution (list of numbers) – default: 0.
stdev: float – represents the standard deviation of a distribution (list of numbers) – default: 1

METHODS
__init__()
This initialization method adds on to the initialization method of Distribution class. It defines two extra instance attributes size and prob.

read_data_file_() – Same as of Distribution class

calculate_mean()
This method calculates the mean value of the distribution based on size and probability (prob) and returns the same.
Arguments
self: An instance of Binomial class
Returns
float – represents the mean value of the distribution.

calculate_stdev()
This method calculates the standard deviation value of the distribution based on size and probability (prob) and returns the same.
Arguments
self: An instance of Binomial class
Returns
float – represents the standard deviation value of the distribution

replace_stats_with_data()
This method calculates the size and probability (prob) of the distribution provided by the text file read  into data_list. 
Arguments
self: An instance of Binomial class
Returns
int – represents the size of the distribution.
float – represents the probability (prob) of the distribution.

probability_density()
This method calculates the probability density function on distribution based on point and returns the same.
Arguments
self: An instance of Binomial class
point: int – represents the point at which the function calculates the probability density.
Returns
float – represents the probability density value on the distribution at the point.

plot_bar()
This function outputs a bar graph of the instance variable data using matplotlib pyplot library. It takes nothing as an argument except the self and draws the plot based on the data_list itself.

plot_bar_probability_density()
This function plots the normalized bar graph of the data and a plot the probability density function along the same range. It returns the X and Y axes values for the probability density function plot
Arguments
self: An instance of Binomial class
Returns
list – X axes values for probability density function plot
list – Y axes values for probability density function plot

__add__()	
This function adds two Binomial distribution instances together to create a new Binomial distribution with different size and probability (prov) values based on the given size and prob values of the provided two Binomial instances. It overloads the + operator so that it can work with Binomial class as a binary operator. It returns the new Binomial instance.
Arguments
self: An instance of Binomial class
other: Binomial – represents the other Binomial instance we are adding the self. 
Returns
Binomial – A new Binomial instance obtained from adding the self and other.

__repr__()
This function represents the Binomial instances as a string consisting of size, probability, mean and standard deviation.

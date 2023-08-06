import math
import matplotlib.pyplot as plt
from .GeneralDistribution import Distribution

class Binomial(Distribution):

    """Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials"""
    
    
    def __init__(self, prob_v = 0.5, size_v = 20):
                
        self.size = size_v
        self.prob = prob_v
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
                        
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set"""
        
        self.mean = self.prob * self.size
                
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set"""
             
        self.stdev = math.sqrt(self.size * self.prob * (1 - self.prob))
        
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value"""
    
        self.size = len(self.data)
        self.prob = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()     

 
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None"""
                
        plt.bar(x = ['0', '1'], height = [(1 - self.prob) * self.size, self.prob * self.size])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        
        
        
    def probability_density(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        a = math.factorial(self.size) / (math.factorial(k) * (math.factorial(self.size - k)))
        b = (self.prob ** k) * (1 - self.prob) ** (self.size - k)
        
        return a * b
        

    def plot_bar_probability_density(self):

        """Function to plot the probabilty density of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the probability density plot
            list: y values for the probability density plot"""
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.size + 1):
            x.append(i)
            y.append(self.probability_density(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
        
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution"""
        
        try:
            assert self.prob == other.prob, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.size = self.size + other.size
        result.prob = self.prob
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian"""
        
        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.prob, self.size)
import numpy as np

"""
Computes the mean, sum, and maximum distance between two functions,
evaluated at a set of x values.
"""
class Evaluate:
    def __init__(self, x, f, g):
        self._x = x
        self._y1 = np.vectorize(f)(x)
        self._y2 = np.vectorize(g)(x)
        error = [abs(self._y2[i] - self._y1[i]) for i in range(len(x))]
        self._mean = np.mean(error)
        self._sum = np.sum(error)
        self._max = np.max(error)

    @property
    def x(self):
        return self._x

    @property
    def y1(self):
        return self._y1
    
    @property
    def y2(self):
        return self._y2
    
    @property
    def mean(self):
        return self._mean
    
    @property
    def sum(self):
        return self._sum
    
    @property
    def max(self):
        return self._max

"""
A class to generate unique random floats within a range.
We will use this class to generate training, validation, and evaluation data.
"""
class UniqueRandomFloatGenerator:
    def __init__(self, low, high, precision=5):
        """
        Initialize the generator with a range and precision.
        
        :param low: The lower bound of the range.
        :param high: The upper bound of the range.
        :param precision: The precision (decimal places) for uniqueness.
        """
        self.low = low
        self.high = high
        self.precision = precision
        self.generated = set()
    
    def next(self, n):
        samples = []
        for _ in range(n):          
            sample = self.next_sample()
            samples.append(sample)
        return samples

    def next_sample(self):
        """
        Generate a unique random sample from the range.
        
        :return: A unique float within the specified range.
        """
        while True:
            # Generate a random float in the range
            sample = round(np.random.uniform(self.low, self.high), self.precision)
            # Check if it's unique
            if sample not in self.generated:
                self.generated.add(sample)
                return sample

# Generates n samples of f(x) for values of x between x0 and x1
# Sample has gaussian noise with standard deviation std_dev
def sample(f, x, std_dev = 0):
    y = np.vectorize(f)(x)
    noise = np.random.normal(0, std_dev, len(x)) if std_dev > 0 else 0
    return x, y + noise

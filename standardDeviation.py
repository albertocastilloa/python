# Given: 
# std_dev = standard deviation of the dataset
# mean = mean of the dataset

# 68% of the data falls between +/- 1 standard deviation
one_std_range = [mean - std_dev, mean + std_dev]

# 95% of the data falls between +/- 2 standard deviations
two_std_range = [mean - (2*std_dev), mean + (2*std_dev)]

# 99.7% of the data falls between +/- 3 standard deviations
three_std_range = [mean - (3*std_dev), mean + (3*std_dev)]
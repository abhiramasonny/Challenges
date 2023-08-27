"""Given a set of numbers n (padded with zeros as needed), 
compute the 1D averaging convolution with stride=1 and kernel size of k. 
(ask Krishna for help).
"""

import matplotlib.pyplot as plt

def average_convolution(data, k):
    kernel = [1/k for _ in range(k)]
    padding_size = (k - 1) // 2
    padded_data = [0] * padding_size + data + [0] * padding_size
    
    res = []
    for i in range(len(data)):
        segment = padded_data[i:i+k]
        averaged_value = sum([a*b for a, b in zip(segment, kernel)])
        res.append(averaged_value)
    
    return res

data = [2, 3, 4, 5, 6]
ksize = 3
convoluted_data = average_convolution(data, ksize)
print(convoluted_data)
plt.figure(figsize=(10, 6))
plt.title('og data vs. conv data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.plot(data, 'o-', label='og data', color='darkblue')
plt.plot(convoluted_data, 's-', label='conv data', color='darkred')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()

#W website: https://e2eml.school/convolution_one_d.html
import numpy as np
import matplotlib.pyplot as plt

#program simulira met šivanke, d = l = 1 
#vir: https://statmodeling.stat.columbia.edu/2024/05/23/gpt-today-jokes-and-buffons-needle-in-python-with-plotting/

num_samples = 20 #število poskusov
field_width = 16 #x koordinata
field_height = 20 #y koordinata


def generate_needles(num_samples, field_width, field_height):
    # naključne sredinske točke šivanke
    x = np.random.uniform(0, field_width, num_samples)
    y = np.random.uniform(0, field_height, num_samples)
    # naključni kot
    theta = np.random.uniform(0, 2*np.pi, num_samples)
    
    return x, y, theta



x, y, theta = generate_needles(num_samples, field_width, field_height)

def check_overlaps(x, y, theta, field_width):
    num_cracks = field_width + 1
    crack_positions = np.linspace(0, field_width, num_cracks)
    overlaps = np.zeros(len(x), dtype=bool)
    arr = [0 for i in range(len(x))]
    for i in range(len(x)):
        # legi obeh krajišč šivanke
        x1 = x[i] + 0.5 * np.cos(theta[i])
        y1 = y[i] + 0.5 * np.sin(theta[i])
        x2 = x[i] - 0.5 * np.cos(theta[i])
        y2 = y[i] - 0.5 * np.sin(theta[i])
        
        # ali šivanka seka kakšno od črt x = 0, x = 1, ... ,x = field_width  
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        overlaps[i] = np.any((crack_positions > min_x) & (crack_positions < max_x))
        arr[i] = (((i+1))*2)/sum(overlaps)
    x = [i for i in range(len(x))]
    plt.plot(x,arr,"ro")
    plt.xlabel('št. poskusov')
    plt.ylabel('približek')
    plt.show()
    return ((len(x))*2)/sum(overlaps) #končni približek


import math
import copy
import matplotlib.pyplot as plt

original_path = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [5, 5]]
smooth_path = []


def Distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)


def Smooth(path=original_path, weight_path=0.5, weight_smooth=0.1, tolerance=0.000001):

    smooth = copy.deepcopy(path)
    while True:
        for x in range(1, len(path)-1):
            for y in range(1, len(path[0])):
                line = weight_path*(path[x][y] - smooth[x][y])
                alpha = weight_smooth*(smooth[x-1][y] - smooth[x][y])
                beta = weight_smooth*(smooth[x+1][y] - smooth[x][y])
            
                smooth[x][y] = smooth[x][y] + line + alpha + beta

        if abs(Distance(path[1], smooth[1])) < tolerance:
            print("[MSG] Tolerance is Greater...")
            break

    #Plotting the lines against eachother
    plt.plot(smooth, label = "Smoothed Line")
    plt.plot(path, label = "Original Path")
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()

    print("Smooth Line: " + str(smooth))
    return smooth

Smooth(original_path, 0.5, 0.1, 0.0000001)
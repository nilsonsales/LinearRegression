import matplotlib.pyplot as plt



def sum_vector(vector):
    result = 0
    for i in range(len(vector)):
        result += vector[i]
    return result


def vector_squared(vector):
    new_v = []
    for i in range(len(vector)):
        new_v.append(vector[i]**2)
    return new_v


def mult_vect_elem(v1, v2):
    new_v = []
    for i in range(len(v1)):
        new_v.append(v1[i]*v2[i])
    return new_v


def line_function(x, a, b):
    return (a * x + b)


def main():

    x = [1, 2, 3, 4, 5]
    y = [1, 1, 2, 2, 4]

    n = len(x)

    x_squared = vector_squared(x)

    xi_times_yi = mult_vect_elem(x, y)

    x_average = sum(x)/n
    y_average = sum(y)/n

    # slope/gradient of the line
    a = (n*sum(xi_times_yi) - sum(x)*sum(y)) / (n*sum(x_squared) - sum(x)**2)

    # y-intercept of the line
    b = y_average - a*x_average

    # calculate two points to draw the line
    x_line = [0, x[-1]+1]
    y_line = (b, line_function(x[-1] + 1, a, b))

    # draw the points
    plt.plot(x, y, 'o')
    # draw the line
    plt.plot(x_line, y_line, 'r--')

    # define the limits of the graph
    plt.axis([0, max(x)+1, 0, max(y)+1])

    #plt.ylabel('Y')
    #plt.xlabel('X')
    plt.title("Linear Regression")
    plt.figure(figsize=(8, 6))

    plt.show()


if __name__ == '__main__':
    main()

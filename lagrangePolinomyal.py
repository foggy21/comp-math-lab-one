def Multiplication(node, values_x, x_star, i):
    result = 1
    for j in range(node):
        if i != j:
            result = result * ((x_star - values_x[j])/(values_x[i] - values_x[j]))
    return result

# Patrick Bateman sigma...
def SigmaSum(node, values_y, values_x, x_star):
    result = 0
    for i in range(node):
        result += values_y[i] * Multiplication(node, values_x, x_star, i)
    return result
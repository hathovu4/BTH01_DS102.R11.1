#x^4 + y^2 + 2xy+ 1
#4x^3+2y -> d/dx: 12x^2 d/dy: 2
#2y+2x -> d/dx: 2 d/dy: 2
import copy
import numpy as np
def grad(u):
    x, y = u
    return np.array([
        4*x**3 + 2*y,
        2*y + 2*x
        ])

def hessian(u):
    x,y = u
    return np.array([
        [12*x**2, 2],
        [2, 2]
    ])

def newton_optimizer(grad, hessian, u_0, tol = 1e-8, max_iter = 100):
    history = [u_0]
    u = copy.deepcopy(u_0)
    for i in range(max_iter):
        g = grad(u)
        if np.linalg.norm(g) < tol:
            break
        h = hessian(u)
        #hessian_inv = np.linalg.inv(h)
        #u = u - g @ hessian_inv
        a = np.linalg.solve(h, g)
        u = u - a
        history.append(copy.deepcopy(u))
    return history, u
if __name__ == "__main__":
    u_0 = (10,10)
    history, u = newton_optimizer(grad, hessian, u_0)
    print(history, u)
    
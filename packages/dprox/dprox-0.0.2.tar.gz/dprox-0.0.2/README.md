# OpenProx

An Open-Source Toolbox for Proximal Algorithms.

<img src="example.png" width="350" />

:sparkles: Advantages over [ProxImaL](https://github.com/comp-imaging/ProxImaL)

- Fast: Implemented in PyTorch, Cache Intermediate variable.
- Intelligence: Automatic Parameter Selection with Reinforcement Learning
- Diversity: More algorithms, Proxiaml operators, Plug-and-Play

## Install

```s
pip install openprox
```

## Usages

- Image denoising with total variation priors.

```python
I = scipy.misc.ascent() / 255
b = I + np.random.normal(0, 10/255, I.shape)

# Define and Solve the Problem 

x = Variable()
data_term = sum_squares(x, b)
reg = norm1(Grad(0)+Grad(1))

problem = Problem(data_term + reg)
x_pred = problem.solve(solver='admm', 
                       x0=b, 
                       eps=1e-6,
                       rhos=0.025, 
                       weights={reg: 20},
                       max_iter=5)
```

## Citations

```bibtex
@software{lai_openprox_2022,
  author = {Zeqiang Lai},
  title = {OpenProx: Differentiable Proximal Programming for Efficient Image Optimization},
  url = {https://github.com/Zeqiang-Lai/OpenProx},
  year = {2022}
}
```
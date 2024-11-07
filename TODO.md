# TODO

* Dev container
* Explanatory test
  * Explanation of hat basis construction
  * Explain matrix math and impact of removing ReLU.
* x Delete old code
* x Python model missing first and last segment
  * x PyTorch model doesn't seem to miss these segments.
    * x PyTorch model does build_layers on x and y - not segments
* Difference between Python and PyTorch models seems too high in the middle
  * x Difference in ends is because of missing segments
  * Maybe need to check for 32-bit math or 64-bit vectors
* Better names than f(), g(), h()
* Better names than model1, model2
* Decide about NumPy vs Pytorch size polarity mismatch
* Render segments in PyTorch model. Is this even possible?
* Repeatability with random numbers of training data and PyTorch
* PyTorch CPU vs GPU
* Find good random number seed to keep text in sync with data
* Consistant use of float32
* Hyperparameter exploration
* Save best model encountered during epochs
* Train pytorch model on f with noise.
  * Show how model evolves over time.
  * Find out when PyTorch gets over fit
  * Show overfitting.
* 2D hat basis

* x Convert from step function basis to hat function basis
  * x This will increase numerical stability
* x Write introduction.
  * x Goals.
  * x Overview.
* x Write prerequisites.
* x Function to calculate error - used for evaluation.
* x Display error for python model and pytorch model.
* x Train pytorch model on f.
  * x Show how model evolves over time.
* x Extend to 2d, using hat function basis.

### MathJAX

$\hat{Y} = \hat{\beta}_{0} + \sum \limits _{j=1} ^{p} X_{j}\hat{\beta}_{j} $

### Notes

* [Piecewise linear approximation applied to nonlinear function](https://d1wqtxts1xzle7.cloudfront.net/68655773/ip-cds_3A1997158720210808-11197-24q1x5-libre.pdf?1628434530=&response-content-disposition=inline%3B+filename%3DPiecewise_linear_approximation_applied_t.pdf&Expires=1730594824&Signature=LU334S8WYZopJQlLx47LS8J~QLqoUArS6l87jd3qAXOBEXSDZnMFshBjOWnZmByPDDHzSOZRraDWcAhY1lrnTL9G1X6Rn2XpyT2EVk~CicVWgOfEQ9naLe98umLE7FPD6SxaaT7762y7wlg090tagIV3IEGs4SbkVfHSpm3tV608ULmu-XwAD7MAM~Drz9LG-MAhzrWoJP-6vRySjBnpSSM6DDtdaV2pgaUny4TSYLH6tiXcEdQuYebyzm327Q13dnM7HNV-nIz1sQolQ0g9J2srlfjNi4gJ51xIOVdVgl1wUIF~OetkKDd5L6GzN7Wj9qzi~6-K1kKjUUWkEJ-o5A__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
* [Laplace Transform of Functions](https://lpsa.swarthmore.edu/LaplaceXform/FwdLaplace/LaplaceFuncs.html)

### Sample Code

# %matplotlib widget
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Generate some data for the height field
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)
# X, Y = np.meshgrid(x, y)
# Z = np.sin(np.sqrt(X**2 + Y**2))

# # Create a figure and 3D axes
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the surface
# surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# # Add labels and title
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Height')
# plt.title('3D Height Field')

# # Show the plot
# plt.show()
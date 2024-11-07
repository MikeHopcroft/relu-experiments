# TODO


ERROR: Ignored the following versions that require a different python version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
ERROR: Could not find a version that satisfies the requirement pywin32==308 (from versions: none)
ERROR: No matching distribution found for pywin32==308

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
numba 0.59.1 requires numpy<1.27,>=1.22, but you have numpy 2.1.2 which is incompatible.
s3fs 2024.3.1 requires fsspec==2024.3.1, but you have fsspec 2024.10.0 which is incompatible.
datasets 2.19.1 requires fsspec[http]<=2024.3.1,>=2023.1.0, but you have fsspec 2024.10.0 which is incompatible.
streamlit 1.38.0 requires pillow<11,>=7.1.0, but you have pillow 11.0.0 which is incompatible.
pywavelets 1.5.0 requires numpy<2.0,>=1.22.4, but you have numpy 2.1.2 which is incompatible.
Successfully installed MarkupSafe-3.0.2 Pygments-2.18.0 asttokens-2.4.1 comm-0.2.2 contourpy-1.3.0 cycler-0.12.1 debugpy-1.8.7 executing-2.1.0 filelock-3.16.1 fonttools-4.54.1 fsspec-2024.10.0 ipython-8.29.0 jedi-0.19.1 jupyter_client-8.6.3 kiwisolver-1.4.7 matplotlib-inline-0.1.7 networkx-3.4.2 numpy-2.1.2 nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.4.127 packaging-24.1 parso-0.8.4 pillow-11.0.0 platformdirs-4.3.6 prompt_toolkit-3.0.48 psutil-6.1.0 pure_eval-0.2.3 pyparsing-3.2.0 pyzmq-26.2.0 setuptools-75.3.0 stack-data-0.6.3 sympy-1.13.1 torch-2.5.1 torchsummary-1.5.1 triton-3.1.0 typing_extensions-4.12.2 wcwidth-0.2.13


* Dev container
  * install/enable jupyter, python extensions
  * create and activate venv
  * linux commands for create/activate
  * pip3 instad of pip?
  * remove pywin32==308 from requirements.txt
* x Convert segments array to xs, yx in piecewise section
* Can Layer3 and Layer4 be combined?
* Explanatory test
  * x Explanation of hat basis construction
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
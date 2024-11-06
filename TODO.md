# TODO

* Explanation of hat basis construction
* Delete old code
* x Python model missing first and last segment
  * x PyTorch model doesn't seem to miss these segments.
    * x PyTorch model does build_layers on x and y - not segments
* Difference between Python and PyTorch models seems too high in the middle
  * Difference in ends is because of missing segments
  * Maybe need to check for 32-bit math or 64-bit vectors
* Better names than f(), g(), h()
* Better names than model1, model2
* Decide about NumPy vs Pytorch size polarity mismatch
* Render segments in PyTorch model. Is this even possible?
* Find out when PyTorch gets over fit
## Version 1.0

In this version, I was primarily focused on training T5 on a custom data set. T5 (Text-To-Text Transfer Transformer) is a transformer-based model introduced by Google that can perform a wide variety of NLP tasks. Training T5 on a custom data set involves fine-tuning the pre-trained model on specific data to improve its performance on a particular task or domain.

To train T5 on a custom data set, you can follow these general steps:

- Data Preparation: Collect and preprocess your data set according to the task you want T5 to perform. Ensure that the data is in a format suitable for fine-tuning T5. i.e. (Question – Answer – Context).
- Model Selection: Choose the pre-trained T5 model that best fits your task and domain. You can use the base T5 model or one of its variants (e.g., T5-small, T5-base, T5-large, T5-3B, T5-11B).
- Fine-Tuning: Fine-tune the selected T5 model on your custom data set. This involves loading the pre-trained weights of the model and updating them using your data set through gradient descent.

For detailed instructions and explanation of the code refer to Venelin Valkov videos on T5

- <https://youtu.be/_l2wJb3QPdk?si=DhqNJKLyWto2QoPM>
- <https://youtu.be/r6XY80Z9eSA?si=nIlX1phGq42yJ1vW>

## Version 1.1

In this version, I added comments to the code to make it easier for anyone to understand.

## Version 1.2

In version 1.2 of the project, I attempted to enhance the model's performance by adjusting the validation set from 5% to 20%. Increasing the validation set size can provide a more reliable estimation of the model's generalization capabilities and potentially improve its performance on unseen data. Studies such as [Smith et al.](#references) have indicated that a larger validation set can lead to better model selection and tuning, thus contributing to overall model robustness.

However, during testing on hardware configurations including NVIDIA Tesla P100 GPUs and Intel Xeon 2GHz (2 core) CPUs, I observed significant resource consumption, with both the GPU and CPU maxing out. As a result, I reverted the validation set back to 5% to maintain reasonable resource usage and ensure efficient training and testing processes.

### References

- Smith, J., et al. "Optimizing Machine Learning Models for Robustness: A Review." Journal of Artificial Intelligence Research, vol. 56, 2016, pp. 205-235.

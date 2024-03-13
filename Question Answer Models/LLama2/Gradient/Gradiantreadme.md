# Finetuning the 13B Parameter LLAMA 2 Model:
This repository contains instructions for finetuning a 13B parameter LLAMA 2 model. The finetuning process was conducted on the Gradient platform, using two distinct approaches: Version 1, which utilized three sample inputs provided in the code, and Version 2, which employed a custom CSV dataset provided by the user.

# Version_1: Training with samples:

Version 1 training with samples given in the code involves fine-tuning a pre-trained 13B parameter Llama 2 model using a small set of samples that are directly provided within the code itself. This method is particularly useful when labeled data is scarce or when there's a need to quickly prototype and test the model on a specific task without relying on external datasets

# Version_2: Training with custom dataset:

Version 2 training involves fine-tuning the pre-trained 13B parameter Llama 2 model using a custom dataset, typically provided in the form of a CSV file. This method allows for more customization and adaptation of the model to specific tasks or domains where labeled data is available.


## Notes:
-Base Model: The base model used in this test is the 13B Parameter LLAMA 2 Model, also known as nous-hermes2. It serves as the starting point for fine-tuning with custom data. Although, there are other models on the site if needed.

-Custom Dataset: Ensure your custom dataset is properly formatted with text inputs and corresponding labels. This is essential for effective training.

-Epochs: Adjust the number of epochs according to your GPU memory and training requirements. Experiment with different configurations to achieve optimal results.

## Additional Resources:
-Gradient: https://gradient.ai/

-Custom Dataset: characters

-YouTube Video Tutorial: https://youtu.be/74NSDMvYZ9Y

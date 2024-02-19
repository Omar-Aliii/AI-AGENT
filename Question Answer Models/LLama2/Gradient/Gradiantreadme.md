# Version 1: Training with Gradient's Base Model (Llama 2 pretrained model):

## Instructions:
1.**Install the required packages: Ensure you have installed the necessary Python packages using the command provided above.

2.Set your environment variables: Use your API access token and workspace ID provided by Gradient to set environment variables. This step is crucial for accessing Gradient's resources.

3.Run the provided code: Execute the provided code to start training with Gradient's base model. This version uses the Llama 2 pretrained model, also known as nous-hermes2, and fine-tunes it with custom text samples.

# Version 2: Training with Custom Dataset:

## Instructions:
1.Install the required packages: Similar to Version 1, ensure you have installed the necessary Python packages using the provided command.

2.Set your environment variables: Use your API access token and workspace ID provided by Gradient to set environment variables, enabling access to Gradient's resources.

3.Prepare your custom dataset: Organize your data in a CSV format with 'inputs' and 'label' columns. This dataset will be used for training the model on specific tasks.

4.Run the provided code: Execute the provided code, replacing 'characters.csv' with the filename of your custom dataset. This version trains the model on your dataset and fine-tunes it accordingly.

## Notes:
-Base Model: The base model used in Version 1 is the Llama 2 pretrained model, also known as nous-hermes2. It serves as the starting point for fine-tuning with custom data.
-Custom Dataset: Ensure your custom dataset is properly formatted with text inputs and corresponding labels. This is essential for effective training.
-Batch Size and Epochs: Adjust the batch size and number of epochs according to your GPU memory and training requirements. Experiment with different configurations to achieve optimal results.

# Llama 2 chat training and finetuining:

## Llama 2 v1_1:
-Dataset and Pretrained Model: The choice of dataset (mlabonne/guanaco-llama2-1k) and pretrained model (NousResearch/Llama-2-7b-chat-hf) is crucial for the performance of the Llama 2 model. These decisions depend on factors such as the nature of the task, available computational resources, and the quality of the dataset.

-Fine-tuning: Fine-tuning involves adjusting the parameters of the pretrained Llama 2 model to better fit the specific requirements of the task at hand. This process typically involves feeding the dataset through the model, computing gradients, and updating the model's parameters using techniques like backpropagation.

-Quantized Low Rank Adaptation (QLORA): QLORA is a technique used to adapt the pretrained Llama 2 model efficiently. It combines quantization, : a process that involves reducing the precision of the model's weights and activations to lower bit-width representations, thereby reducing memory footprint and computational overhead (Jacob, 2018). with low-rank adaptaion, 
with Low-Rank Adaptation (LoRA): is a technique used to compress and adapt large neural network models, such as Llama 2, to make them more suitable for deployment in resource-constrained environments like AI call centers. By injecting trainable rank decomposition matrices into each layer of the Transformer architecture and freezing the pretrained model weights, Low-Rank Adaptation, or LoRA, significantly reduces the number of trainable parameters for jobs that come after (Hu, 2021) . In addition, reducing the model's rank, LoRA reduces computational complexity and memory requirements without significantly sacrificing performance.

References: 

•Hu, E. J.-Z. (2021). Lora: Low-rank adaptation of large language models.

•Jacob, B. K. (2018). Quantization and training of neural networks for efficient integer-arithmetic-only inference. In Proceedings of the IEEE conference on computer vision and pattern recognition .


-Pipeline for Question Generation: A pipeline is a sequence of steps used to process input data and generate output. In this case, the pipeline takes a question as input and generates an answer using the fine-tuned Llama 2 model.

-Upload to Hugging Face: Hugging Face is a platform that hosts a large collection of pretrained models and datasets for natural language processing. Uploading the finetuned model to Hugging Face makes it accessible to other researchers and developers, facilitating collaboration and knowledge sharing.

## Llama 2 v1_2:
-Datasets: The choice of datasets ("Salesforce/dialogstudio" and "TweetSumm") the datasets likely contain conversational data, which can be used to train and evaluate the Llama 2 model.

-Data Cleaning: Data cleaning is an essential preprocessing step to ensure the quality and consistency of the dataset. This process may involve removing noise, correcting errors, and standardizing the format of the data.

-Loss Visualization: Visualizing the training and validation loss helps monitor the training process and identify potential issues such as overfitting or underfitting. It provides insights into how well the model is learning from the data and whether adjustments to the training procedure are necessary.

-Conversation Simulation: Simulating a conversation between a client and an agent demonstrates the practical application of the trained Llama 2 model. 

## Llama 2 v1_3:
-Dataset: : using a medical dataset from google drive called BioASQ.

-Evaluation Metrics: BERT Score is a metric used to evaluate the quality of generated text by comparing it to reference text using contextual embeddings from BERT (Bidirectional Encoder Representations from Transformers). BERT Score measures the similarity between the generated text and the ground truth summaries based on contextual embeddings, providing a more nuanced evaluation of summarization quality compared to traditional metrics like ROUGE. (Zhang, 2019)

Refrence: Zhang, T. K. (2019). Bertscore: Evaluating text generation with bert.

-Human Evaluation: Conducting a human evaluation adds an important qualitative dimension to the evaluation process. While automated metrics like BERTScore provide useful insights, human judgments can capture aspects of text quality that may not be captured by automated metrics alone. This helps assess the practical usability of the trained model in real-world scenarios. I compared the generated answer from the model I trained and the orginal model.


## Llama 2 v1_4(final code):
-Dataset: SQuAD v1 is a popular dataset for training and evaluating question answering systems. It consists of questions posed by crowdworkers on a set of Wikipedia articles, along with the corresponding passages containing the answers.

-Sampling: Offering different sample sizes allows for experimentation with the amount of data used for training. Training with smaller samples may be faster and require less computational resources but may result in lower performance compared to training with larger samples. This is why I choose the 3 samples as you will see in the code the 100, 1000, and 5000 samples.

-Evaluation Metrics: For each generated question-answer pair, Recall, Precision, and F1 score are calculated. The average of these scores is then evaluated.Recall, Precision, and F1 score are standard metrics used to evaluate the performance of question answering systems. Recall measures the proportion of relevant items that were retrieved, Precision measures the proportion of retrieved items that are relevant, and F1 score is the harmonic mean of Recall and Precision, providing a balanced measure of performance.

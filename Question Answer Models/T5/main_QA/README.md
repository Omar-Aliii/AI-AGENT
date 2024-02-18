## Version 1.0

In this version, I was primarily focused on training T5 on a custom data set. T5 (Text-To-Text Transfer Transformer) is a transformer-based model introduced by Google that can perform a wide variety of NLP tasks. Training T5 on a custom data set involves fine-tuning the pre-trained model on specific data to improve its performance on a particular task or domain.

To train T5 on a custom data set, you can follow these general steps:

- Data Preparation: Collect and preprocess your data set according to the task you want T5 to perform. Ensure that the data is in a format suitable for fine-tuning T5. i.e. (Question – Answer – Context).
- Model Selection: Choose the pre-trained T5 model that best fits your task and domain. You can use the base T5 model or one of its variants (e.g., T5-small, T5-base, T5-large, T5-3B, T5-11B).
- Fine-Tuning: Fine-tune the selected T5 model on your custom data set. This involves loading the pre-trained weights of the model and updating them using your data set through gradient descent.

For detailed instructions and explanation of the code refer to Venelin Valkov videos on T5:
- <https://youtu.be/_l2wJb3QPdk?si=DhqNJKLyWto2QoPM>
- <https://youtu.be/r6XY80Z9eSA?si=nIlX1phGq42yJ1vW>

## Version 1.1

In this version, I added comments to the code to make it easier for anyone to understand.

## Version 1.2

In version 1.2 of the project, I attempted to enhance the model's performance by adjusting the validation set from 5% to 20%. Increasing the validation set size can provide a more reliable estimation of the model's generalization capabilities and potentially improve its performance on unseen data. Studies such as [Smith et al.](#references) have indicated that a larger validation set can lead to better model selection and tuning, thus contributing to overall model robustness.

However, during testing on hardware configurations including NVIDIA Tesla P100 GPUs and Intel Xeon 2GHz (2 core) CPUs, I observed significant resource consumption, with both the GPU and CPU maxing out. As a result, I reverted the validation set back to 5% to maintain reasonable resource usage and ensure efficient training and testing processes.

References:
- Smith, J., et al. "Optimizing Machine Learning Models for Robustness: A Review." Journal of Artificial Intelligence Research, vol. 56, 2016, pp. 205-235.

## Version 1.3


### Evaluation of Results

One of the key objectives in this version was to measure the accuracy of the generated answers compared to the actual answers. This involved rigorous evaluation methods to assess the quality of the output. Various metrics and techniques were employed to gauge the effectiveness of the model in generating accurate responses. The results of this evaluation process provide valuable insights into the performance of the system and guide further improvements.

In this version, I removed duplicates from datasets to expedite training and enable more epochs.
### Evaluation Metrics

### BLEU Score

In natural language processing, the BLEU (Bilingual Evaluation Understudy) score is a metric used to evaluate the quality of machine-generated text against one or more reference texts. It measures the n-gram overlap between the generated text and the reference texts, rewarding higher precision in matching n-grams while penalizing longer generated sequences. BLEU score is widely used in machine translation tasks and has been adopted in various other natural language generation tasks due to its simplicity and effectiveness. However, BLEU score's effectiveness is more pronounced for evaluating longer sequences or sentences rather than short phrases or single words. This is because longer sequences provide more context and allow for a more meaningful evaluation of the generated text. It is crucial to note that while BLEU score provides a quantitative measure of similarity between the generated and reference texts, it does not fully capture the semantic equivalence or fluency of the generated text. 

Reference:
- Papineni, K., Roukos, S., Ward, T., & Zhu, W. J. (2002). BLEU: A Method for Automatic Evaluation of Machine Translation. In Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL).

### Jaccard Similarity

On the other hand, Jaccard similarity, also known as the Jaccard index or Jaccard coefficient, is a statistic used for comparing the similarity and diversity of sample sets. It calculates the similarity between two sets by dividing the size of the intersection of the sets by the size of the union of the sets. While Jaccard similarity is straightforward and easy to compute, it has limitations, particularly in natural language processing tasks. One significant drawback is its insensitivity to the order of elements in the sets, meaning it treats "apple" and "papple" as equally dissimilar, which is not ideal for tasks where the sequence of characters matters. Moreover, Jaccard similarity doesn't account for variations such as case sensitivity or misspellings, making it less suitable for text comparison tasks where these factors are important considerations. 

Reference:
- Jaccard similarity coefficient. (n.d.). In Wikipedia. Retrieved January 29, 2024, from https://en.wikipedia.org/wiki/Jaccard_index

# Version 1.0

## Fine-tuning Language Model BERT on SQuAD v1 for Question Answering

In Version 1.0, the primary objective was to fine-tune the Language Model BERT (Bidirectional Encoder Representations from Transformers) on the SQuAD v1 dataset for the task of question answering. BERT, a cutting-edge transformer-based model developed by Google, is renowned for its exceptional ability to understand bidirectional context in natural language.

The SQuAD v1 (Stanford Question Answering Dataset) serves as a widely adopted benchmark dataset in the field, containing over 100,000 question-answer pairs sourced from various Wikipedia articles. Each pair presents a challenge to models, requiring them to accurately pinpoint answer spans within the provided text passages.

To ensure a thorough understanding of the task and the tools involved, comprehensive research was conducted. This included in-depth study of academic papers detailing the BERT architecture, alongside educational materials such as instructional videos, aimed at elucidating effective fine-tuning strategies. Furthermore, extensive exploration of resources pertaining to the SQuAD dataset was undertaken to grasp its underlying structure and intricacies.

The preprocessing phase involved the division of the SQuAD v1 dataset into distinct training and validation sets, with a distribution of 90% for training and 10% for validation. Subsequently, the Language Model BERT underwent fine-tuning on the designated training subset, capitalizing on its advanced bidirectional context understanding capabilities.

Following fine-tuning, rigorous evaluation was conducted on the validation subset, employing metrics such as Exact Match and F1 Score to assess the model's performance.

**References:**
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805), Jacob Devlin et al., Google AI Language.
- Rajpurkar, P., Zhang, J., Lopyrev, K., & Liang, P. (2016). [SQuAD: 100,000+ Questions for Machine Comprehension of Text](https://www.aclweb.org/anthology/D16-1264/). In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (EMNLP).



# Version 1.2

## Evaluating Model Performance on SQuAD Dataset

Version 2.0 focused on testing the model's performance using the SQuAD dataset in various scenarios to assess its question-answering capabilities. Three distinct approaches were employed:

1. **Contextual Question Answering:** Initially, the model was tested by providing it with the same question and context from the SQuAD dataset. The model's objective was to generate the answer based on the given context.

2. **Context-Agnostic Question Answering:** In this scenario, the model was given the same question from the SQuAD dataset without the accompanying context. The model's task was to locate the question in the dataset along with its corresponding context and then generate the answer.

3. **Question Rephrasing and Similarity Matching:** Another testing methodology involved presenting the model with a rephrased question without any context. A separate model, DistilRoBERTa, was employed to identify the most similar question in the SQuAD dataset. Subsequently, the model BERT was given the most similar question along with its corresponding context from the dataset. The goal for BERT in this case was to generate the answer based on the provided context.

Each of these approaches provided insights into the model's ability to understand and generate answers to questions, both in contexts it was directly provided and in scenarios where it needed to infer context or handle rephrased queries.


# Version 1.3

## Incorporating Early Stopping and Semantic Answer Similarity Metrics

In Version 3.0, the focus was on enhancing model training and evaluation methodologies through the incorporation of early stopping and semantic answer similarity metrics.

**Early Stopping**, a widely adopted technique in deep learning, was implemented to halt the training process when the model's performance on a validation set ceased to improve ([Prechelt, 1998](https://link.springer.com/chapter/10.1007/BFb0028978)). This strategy prevents overfitting by curbing the tendency to memorize noise in the training data. It requires the specification of a validation set, an evaluation metric, and a patience parameter to determine the optimal stopping point. Although effective in improving generalization, early stopping necessitates careful parameter selection and may reduce training data availability.

Additionally, extensive research was conducted to identify and implement **evaluation metrics** that calculate the semantic similarity between the generated model answer and the ground truth answer. Unlike traditional metrics such as BLEU, which focus on lexical differences, semantic similarity metrics provide a more nuanced assessment of the model's performance. This approach required thorough exploration of academic papers discussing relevant metrics, as well as studying methodologies outlined in the [BERTScore paper (Tianyi et al., 2020)](https://arxiv.org/abs/2004.09602). Educational articles and instructional videos were also consulted to gain insights into the practical implementation of these techniques.

**References:**
- Prechelt, L. (1998). [Early stopping-but when?](https://link.springer.com/chapter/10.1007/BFb0028978) In Neural Networks: Tricks of the Trade (pp. 55-69). Springer.
- Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. (2020). [BERTScore: Evaluating Text Generation with BERT.](https://arxiv.org/abs/2004.09602) arXiv preprint arXiv:2004.09602.


# Version 2

## Fine-tuning on Different Dataset Subsets and Utilizing TensorBoard for Loss Visualization

Version 4.0 aimed to enhance the training process and evaluation methods through several key strategies.

Firstly, different subsets from the SQuAD dataset were utilized, ensuring each context had only one associated question, thus eliminating duplicates. Fine-tuning was performed on subsets of varying sizes, including 100, 1000, and 5000 examples. This approach allowed for a comprehensive analysis of model performance across different dataset sizes.

Additionally, **TensorBoard**, a visualization tool provided by TensorFlow, was employed to monitor the training process effectively. Train loss and validation loss were visualized in each epoch, providing insights into the model's convergence and performance over time.

Furthermore, the model's performance was rigorously evaluated using **BERTScore**, a metric that calculates the precision, recall, and F1 score of generated answers compared to ground truth answers ([Tianyi et al., 2020](https://arxiv.org/abs/2004.09602)). To assess performance comprehensively, the model generated answers for 10 random questions, and BERTScore was computed for each generated answer. The average BERTScore (precision, recall, F1) was then calculated and displayed using graphical representations, offering a holistic view of the model's overall performance.

**References:**
- Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q. Weinberger, and Yoav Artzi. (2020). [BERTScore: Evaluating Text Generation with BERT.](https://arxiv.org/abs/2004.09602) arXiv preprint arXiv:2004.09602.


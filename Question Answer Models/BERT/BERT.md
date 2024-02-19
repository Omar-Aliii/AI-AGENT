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

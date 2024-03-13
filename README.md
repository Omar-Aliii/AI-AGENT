# C.A.S.S.I.E
## Download the project files
Refer to this [link](https://github.com/Omar-Aliii/AI-AGENT/releases) and download the latest version.
## Environment Setup

[![N|Solid](https://fgnt.github.io/python_crashkurs_doc/_images/logo-dark.png)](https://nodesource.com/products/nsolid)

Anaconda3 simplifies package management for data analysis and machine learning. Its purpose is to streamline package management, allowing users to easily install, update, and manage dependencies for data analysis and machine learning projects. It provides a comprehensive toolkit for researchers and data scientists to work efficiently within Python and R ecosystems.

To install Anaconda, click on the install button [here](https://www.anaconda.com/download).
Replace name_enviroment with your desired environment name.
```sh
conda create --name name_enviroment python=3.10
```
This command activates the created environment.
```sh
conda activate name_enviroment
```
This command installs the CUDA Toolkit.
```sh
conda install cudatoolkit -c anaconda -y
```
This command installs PyTorch with CUDA support.
```sh
conda install pytorch-cuda=12.1 -c pytorch -c nvidia -y
```
This command installs additional dependencies for PyTorch.
```sh
conda install pytorch torchvision torchaudio -c pytorch -c nvidia -y
```



## _Ollama_
<img src="https://bookface-images.s3.amazonaws.com/logos/ee60f430e8cb6ae769306860a9c03b2672e0eaf2.png" alt="alt text" width="250">
Ollama is an open-source application designed to run, create, and share large language models (LLMs) locally on MacOS, Linux and Windows systems. It simplifies the process of setting up and running LLMs by providing a command-line interface and supporting various models like Llama2, Mistral, and Phi-2. Ollama aims to offer a straightforward setup, cost-effectiveness, privacy, and versatility, making it accessible for developers, data scientists, and tech enthusiasts to leverage the power of LLMs without relying on cloud services 
[Install](https://ollama.com/download) - Ollama

To download a model from ollama simlpy prompt ollama pull
```sh
ollama pull llama2
```

## _Speech-to-text(faster-whisper)_
Faster-Whisper is a library designed to significantly speed up the transcription process by leveraging the CTranslate2 engine, which is optimized for Transformer models. It achieves up to four times faster transcription speeds compared to the original Whisper model while maintaining similar accuracy levels and using less memory. This efficiency is further enhanced with 8-bit quantization, making it a practical choice for applications requiring quick and accurate speech-to-text conversion. Faster-Whisper is particularly useful for processing large volumes of audio data, enabling users to transcribe speech more efficiently without compromising on accuracy 45.
```sh
Pip install faster_whisper
```
## R.A.G

Retrieval-Augmented Generation (RAG) is a technique that enhances the capabilities of Large Language Models (LLMs) by integrating external data sources to provide more accurate and contextually relevant responses. It works by embedding user queries into vectors, retrieving relevant data from a database, and then feeding this data back into the LLM to generate responses. This process allows RAG to offer detailed answers to specific questions, fill knowledge gaps, and provide citations for its responses, thereby increasing trust and reliability in AI-generated content.

This command installs the LangChain library.
```sh
pip install langchain
```
This command installs the PyPDF library.
```sh
pip install pypdf
```
This command pulls the nomic-embed-tex module.
```sh
ollama pull nomic-embed-tex
```
## Text-To-Speech(Coqui TTS)

Coqui TTS is a deep learning toolkit designed for Text-to-Speech applications, offering a wide range of features and models for synthesizing speech. It supports multiple languages, including 16 languages in its latest version, and provides high performance across various tasks. Coqui TTS includes capabilities for fine-tuning models, streaming with low latency, and voice cloning with unconstrained voice generation. It also integrates with Coqui Studio for easy voice generation and cloning, making it a versatile solution for developers and researchers in the field of speech synthesis.
This command updates setuptools and wheel packages.
```sh
pip install setuptools wheel -U
```
This command installs the Coqui TTS library.
```sh
pip install tts
```
This command installs the Pygame library.
```sh
pip install pygame
```


## _Other libraries_
```sh
pip install chromadb
```
```sh
pip install tiktoken
```

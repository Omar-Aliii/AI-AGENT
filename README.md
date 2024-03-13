# C.A.S.S.I.E 
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
[![N|Solid](https://kids.kiddle.co/images/thumb/8/8e/Guanaco_09.24.jpg/250px-Guanaco_09.24.jpg)](https://nodesource.com/products/nsolid)

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
## _R.A.G_
Retrieval-Augmented Generation (RAG) is a technique that enhances the capabilities of Large Language Models (LLMs) by integrating external data sources to provide more accurate and contextually relevant responses. It works by embedding user queries into vectors, retrieving relevant data from a database, and then feeding this data back into the LLM to generate responses. This process allows RAG to offer detailed answers to specific questions, fill knowledge gaps, and provide citations for its responses, thereby increasing trust and reliability in AI-generated content.

```sh
pip install langchain
```
```sh
pip install pypdf
```
```sh
ollama pull nomic-embed-tex
```
## _Text-To-Speech(Coqui TTS)_
Coqui TTS is a deep learning toolkit designed for Text-to-Speech applications, offering a wide range of features and models for synthesizing speech. It supports multiple languages, including 16 languages in its latest version, and provides high performance across various tasks. Coqui TTS includes capabilities for fine-tuning models, streaming with low latency, and voice cloning with unconstrained voice generation. It also integrates with Coqui Studio for easy voice generation and cloning, making it a versatile solution for developers and researchers in the field of speech synthesis
```sh
pip install setuptools wheel -U
```
```sh
pip install tts
```
```sh
pip install pygame
```
```sh
pip==23.3.1
pygame==2.5.2
setuptools==68.2.2
TTS==0.22.0
wheel==0.41.2
```

## _Other libraries_
```sh
pip install chromadb
```
```sh
pip install tiktoken
```

## _All version dependencies_
```sh
absl-py                                  2.1.0
aiohttp                                  3.9.3
aiosignal                                1.3.1
annotated-types                          0.6.0
anyascii                                 0.3.2
anyio                                    4.3.0
asgiref                                  3.7.2
async-timeout                            4.0.3
attrs                                    23.2.0
audioread                                3.0.1
av                                       11.0.0
Babel                                    2.14.0
backoff                                  2.2.1
bangla                                   0.0.2
bcrypt                                   4.1.2
blinker                                  1.7.0
blis                                     0.7.11
bnnumerizer                              0.0.2
bnunicodenormalizer                      0.1.6
Brotli                                   1.0.9
build                                    1.1.1
cachetools                               5.3.3
catalogue                                2.0.10
certifi                                  2024.2.2
cffi                                     1.16.0
charset-normalizer                       2.0.4
chroma-hnswlib                           0.7.3
chromadb                                 0.4.24
click                                    8.1.7
cloudpathlib                             0.16.0
colorama                                 0.4.6
coloredlogs                              15.0.1
confection                               0.1.4
contourpy                                1.2.0
coqpit                                   0.0.17
ctranslate2                              4.0.0
cycler                                   0.12.1
cymem                                    2.0.8
Cython                                   3.0.9
dataclasses-json                         0.6.4
dateparser                               1.1.8
decorator                                5.1.1
Deprecated                               1.2.14
docopt                                   0.6.2
einops                                   0.7.0
encodec                                  0.1.1
exceptiongroup                           1.2.0
fastapi                                  0.110.0
faster-whisper                           1.0.1
filelock                                 3.13.1
Flask                                    3.0.2
flatbuffers                              24.3.7
fonttools                                4.49.0
frozenlist                               1.4.1
fsspec                                   2024.2.0
g2pkk                                    0.1.2
gmpy2                                    2.1.2
google-auth                              2.28.2
googleapis-common-protos                 1.63.0
greenlet                                 3.0.3
grpcio                                   1.62.1
gruut                                    2.2.3
gruut-ipa                                0.13.0
gruut-lang-de                            2.0.0
gruut-lang-en                            2.0.0
gruut-lang-es                            2.0.0
gruut-lang-fr                            2.0.2
h11                                      0.14.0
hangul-romanize                          0.1.0
httptools                                0.6.1
huggingface-hub                          0.21.4
humanfriendly                            10.0
idna                                     3.4
importlib-metadata                       6.11.0
importlib_resources                      6.1.3
inflect                                  7.0.0
itsdangerous                             2.1.2
jamo                                     0.4.1
jieba                                    0.42.1
Jinja2                                   3.1.3
joblib                                   1.3.2
jsonlines                                1.2.0
jsonpatch                                1.33
jsonpointer                              2.4
kiwisolver                               1.4.5
kubernetes                               29.0.0
langchain                                0.1.11
langchain-community                      0.0.27
langchain-core                           0.1.30
langchain-text-splitters                 0.0.1
langcodes                                3.3.0
langsmith                                0.1.23
lazy_loader                              0.3
librosa                                  0.10.0
llvmlite                                 0.42.0
Markdown                                 3.5.2
MarkupSafe                               2.1.3
marshmallow                              3.21.1
matplotlib                               3.8.3
mkl-fft                                  1.3.8
mkl-random                               1.2.4
mkl-service                              2.4.0
mmh3                                     4.1.0
monotonic                                1.6
mpmath                                   1.3.0
msgpack                                  1.0.8
multidict                                6.0.5
murmurhash                               1.0.10
mypy-extensions                          1.0.0
networkx                                 2.8.8
nltk                                     3.8.1
num2words                                0.5.13
numba                                    0.59.0
numpy                                    1.26.4
oauthlib                                 3.2.2
onnxruntime                              1.17.1
opentelemetry-api                        1.23.0
opentelemetry-exporter-otlp-proto-common 1.23.0
opentelemetry-exporter-otlp-proto-grpc   1.23.0
opentelemetry-instrumentation            0.44b0
opentelemetry-instrumentation-asgi       0.44b0
opentelemetry-instrumentation-fastapi    0.44b0
opentelemetry-proto                      1.23.0
opentelemetry-sdk                        1.23.0
opentelemetry-semantic-conventions       0.44b0
opentelemetry-util-http                  0.44b0
orjson                                   3.9.15
overrides                                7.7.0
packaging                                23.2
pandas                                   1.5.3
pillow                                   10.2.0
pip                                      23.3.1
platformdirs                             4.2.0
pooch                                    1.8.1
posthog                                  3.5.0
preshed                                  3.0.9
protobuf                                 4.25.3
psutil                                   5.9.8
pulsar-client                            3.4.0
pyasn1                                   0.5.1
pyasn1-modules                           0.3.0
PyAudio                                  0.2.14
pycparser                                2.21
pydantic                                 2.6.3
pydantic_core                            2.16.3
pygame                                   2.5.2
pynndescent                              0.5.11
pyparsing                                3.1.2
pypdf                                    4.1.0
PyPika                                   0.48.9
pypinyin                                 0.51.0
pyproject_hooks                          1.0.0
pyreadline3                              3.4.1
pysbd                                    0.3.4
PySide6                                  6.5.2
PySide6-Addons                           6.5.2
PySide6-Essentials                       6.5.2
PySocks                                  1.7.1
python-crfsuite                          0.9.10
python-dateutil                          2.9.0.post0
python-dotenv                            1.0.1
pytz                                     2024.1
PyYAML                                   6.0.1
regex                                    2023.12.25
requests                                 2.31.0
requests-oauthlib                        1.4.0
rsa                                      4.9
safetensors                              0.4.2
scikit-learn                             1.4.1.post1
scipy                                    1.11.4
setuptools                               68.2.2
shiboken6                                6.5.2
six                                      1.16.0
smart-open                               6.4.0
sniffio                                  1.3.1
soundfile                                0.12.1
soxr                                     0.3.7
spacy                                    3.7.4
spacy-legacy                             3.0.12
spacy-loggers                            1.0.5
SQLAlchemy                               2.0.28
srsly                                    2.4.8
starlette                                0.36.3
SudachiDict-core                         20240109
SudachiPy                                0.6.8
sympy                                    1.12
tenacity                                 8.2.3
tensorboard                              2.16.2
tensorboard-data-server                  0.7.2
thinc                                    8.2.3
threadpoolctl                            3.3.0
tiktoken                                 0.6.0
tokenizers                               0.15.2
tomli                                    2.0.1
torch                                    2.2.1
torchaudio                               2.2.1
torchvision                              0.17.1
tqdm                                     4.66.2
trainer                                  0.0.36
transformers                             4.38.2
TTS                                      0.22.0
typer                                    0.9.0
typing_extensions                        4.9.0
typing-inspect                           0.9.0
tzdata                                   2024.1
tzlocal                                  5.2
umap-learn                               0.5.5
Unidecode                                1.3.8
urllib3                                  2.1.0
uvicorn                                  0.28.0
wasabi                                   1.1.2
watchfiles                               0.21.0
weasel                                   0.3.4
websocket-client                         1.7.0
websockets                               12.0
Werkzeug                                 3.0.1
wheel                                    0.41.2
win-inet-pton                            1.1.0
wrapt                                    1.16.0
yarl                                     1.9.4
zipp                                     3.17.0
```


## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |




```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.




**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

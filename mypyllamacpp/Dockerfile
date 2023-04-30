FROM python:3.10
RUN curl -LJO https://the-eye.eu/public/AI/models/nomic-ai/gpt4all/gpt4all-lora-quantized-ggml.bin
RUN git clone --recursive https://github.com/nomic-ai/pygpt4all.git
RUN pip install -U pip setuptools wheel
RUN cd ./pygpt4all/pyllamacpp && sh ./install.sh
RUN python pygpt4all/pyllamacpp/llama.cpp/migrate-ggml-2023-03-30-pr613.py gpt4all-lora-quantized-ggml.bin gpt4all-lora-quantized-ggjt.bin

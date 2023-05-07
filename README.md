# 🏆 llm-leaderboard

A joint community effort to create one central leaderboard for LLMs. Contributions and corrections welcome!

## Interactive Dashboard

https://llm-leaderboard.streamlit.app/

## How to Contribute

We are always happy for contributions! You can contribute by the following:

- table work (don't forget the links):
    - filling missing entries
    - adding a new model as a new row to the leaderboard and add the source of the evaluation to the sources table. Please keep alphabetic order.
    - adding a new benchmark as a new column in the leaderboard and add the benchmark to the benchmarks table. Please keep alphabetic order.
- code work:
    - improving the existing code
    - requesting and implementing new features

## Leaderboard

| Model Name                                                                             | [Chatbot Arena Elo](https://lmsys.org/blog/2023-05-03-arena/) | [LAMBADA (zero-shot)](https://arxiv.org/abs/1606.06031) | [TriviaQA (zero-shot)](https://arxiv.org/abs/1705.03551v2 ) |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- |
| [alpaca-13b](https://crfm.stanford.edu/2023/03/13/alpaca.html)                         | [1008](https://lmsys.org/blog/2023-05-03-arena/)              |                                                         |                                                             |
| [cerebras-gpt-7b](https://huggingface.co/cerebras/Cerebras-GPT-6.7B)                   |                                                               | [0.636](https://www.mosaicml.com/blog/mpt-7b)           | [0.141](https://www.mosaicml.com/blog/mpt-7b)               |
| [cerebras-gpt-13b](https://huggingface.co/cerebras/Cerebras-GPT-13B)                   |                                                               | [0.635](https://www.mosaicml.com/blog/mpt-7b)           | [0.146](https://www.mosaicml.com/blog/mpt-7b)               |
| [chatglm-6b](https://chatglm.cn/blog)                                                  | [985](https://lmsys.org/blog/2023-05-03-arena/)               |                                                         |                                                             |
| [dolly-v2-12b](https://huggingface.co/databricks/dolly-v2-12b)                         | [944](https://lmsys.org/blog/2023-05-03-arena/)               |                                                         |                                                             |
| [eleuther-pythia-7b](https://huggingface.co/EleutherAI/pythia-6.9b)                    |                                                               | [0.667](https://www.mosaicml.com/blog/mpt-7b)           | [0.198](https://www.mosaicml.com/blog/mpt-7b)               |
| [eleuther-pythia-12b](https://huggingface.co/EleutherAI/pythia-12b)                    |                                                               | [0.704](https://www.mosaicml.com/blog/mpt-7b)           | [0.233](https://www.mosaicml.com/blog/mpt-7b)               |
| [fastchat-t5-3b](https://huggingface.co/lmsys/fastchat-t5-3b-v1.0)                     | [951](https://lmsys.org/blog/2023-05-03-arena/)               |                                                         |                                                             |
| [gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b)                         |                                                               | [0.719](https://www.mosaicml.com/blog/mpt-7b)           | [0.347](https://www.mosaicml.com/blog/mpt-7b)               |
| [gptj-6b](https://huggingface.co/EleutherAI/gpt-j-6b)                                  |                                                               | [0.683](https://www.mosaicml.com/blog/mpt-7b)           | [0.234](https://www.mosaicml.com/blog/mpt-7b)               |
| [koala-13b](https://bair.berkeley.edu/blog/2023/04/03/koala/)                          | [1082](https://lmsys.org/blog/2023-05-03-arena/)              |                                                         |                                                             |
| [llama-7b](https://arxiv.org/abs/2302.13971)                                           |                                                               | [0.738](https://www.mosaicml.com/blog/mpt-7b)           | [0.443](https://www.mosaicml.com/blog/mpt-7b)               |
| [llama-13b](https://arxiv.org/abs/2302.13971)                                          | [932](https://lmsys.org/blog/2023-05-03-arena/)               |                                                         |                                                             |
| [mpt-7b](https://huggingface.co/mosaicml/mpt-7b)                                       |                                                               | [0.702](https://www.mosaicml.com/blog/mpt-7b)           | [0.343](https://www.mosaicml.com/blog/mpt-7b)               |
| [oasst-pythia-12b](https://huggingface.co/OpenAssistant/pythia-12b-pre-v8-12.5k-steps) | [1065](https://lmsys.org/blog/2023-05-03-arena/)              |                                                         |                                                             |
| [opt-7b](https://huggingface.co/facebook/opt-6.7b)                                     |                                                               | [0.677](https://www.mosaicml.com/blog/mpt-7b)           | [0.227](https://www.mosaicml.com/blog/mpt-7b)               |
| [opt-13b](https://huggingface.co/facebook/opt-13b)                                     |                                                               | [0.692](https://www.mosaicml.com/blog/mpt-7b)           | [0.282](https://www.mosaicml.com/blog/mpt-7b)               |
| [stablelm-base-alpha-7b](https://huggingface.co/stabilityai/stablelm-base-alpha-7b)    |                                                               | [0.533](https://www.mosaicml.com/blog/mpt-7b)           | [0.049](https://www.mosaicml.com/blog/mpt-7b)               |
| [stablelm-tuned-alpha-7b](https://huggingface.co/stabilityai/stablelm-tuned-alpha-7b)  | [858](https://lmsys.org/blog/2023-05-03-arena/)               |                                                         |                                                             |
| [vicuna-13b](https://huggingface.co/lmsys/vicuna-13b-delta-v0)                         | [1169](https://lmsys.org/blog/2023-05-03-arena/)              |                                                         |                                                             |

## Benchmarks

| Benchmark Name    | Author         | Link                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chatbot Arena Elo | LMSYS          | https://lmsys.org/blog/2023-05-03-arena/ | "In this blog post, we introduce Chatbot Arena, an LLM benchmark platform featuring anonymous randomized battles in a crowdsourced manner. Chatbot Arena adopts the Elo rating system, which is a widely-used rating system in chess and other competitive games." (Source: https://lmsys.org/blog/2023-05-03-arena/)                                                                                                                                                                                                                                                                 |
| LAMBADA           | Paperno et al. | https://arxiv.org/abs/1606.06031         | "The LAMBADA evaluates the capabilities of computational models for text understanding by means of a word prediction task. LAMBADA is a collection of narrative passages sharing the characteristic that human subjects are able to guess their last word if they are exposed to the whole passage, but not if they only see the last sentence preceding the target word. To succeed on LAMBADA, computational models cannot simply rely on local context, but must be able to keep track of information in the broader discourse." (Source: https://huggingface.co/datasets/lambada) |
| TriviaQA          | Joshi et al.   | https://arxiv.org/abs/1705.03551v2       | "We present TriviaQA, a challenging reading comprehension dataset containing over 650K question-answer-evidence triples. TriviaQA includes 95K question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents, six per question on average, that provide high quality distant supervision for answering the questions." (Source: https://arxiv.org/abs/1705.03551v2)                                                                                                                                                                              |

## Sources

| Author   | Link                                     |
| -------- | ---------------------------------------- |
| LMSYS    | https://lmsys.org/blog/2023-05-03-arena/ |
| MOSAICML | https://www.mosaicml.com/blog/mpt-7b     |

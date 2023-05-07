# 🏆 llm-leaderboard

A joint community effort to create one central leaderboard for LLMs. Contributions and corrections welcome!
Visit the interactive leaderboard at https://llm-leaderboard.streamlit.app/.

## How to Contribute

We are always happy for contributions! You can contribute by the following:

- table work:
    - filling missing entries
    - adding a new model as a new row to the leaderboard and add the source of the evaluation to the sources table
    - adding a new benchmark as a new column in the leaderboard and add the benchmark to the benchmarks table
- code work:
    - improving the existing code
    - requesting and implementing new features

## Leaderboard

| Model Name              | Chatbot Arena Elo | LAMBADA (zero-shot) | TriviaQA (zero-shot) |
| ----------------------- | ----------------- | ------------------- | -------------------- |
| alpaca-13b              | 1008              |                     |                      |
| cerebras-7b             |                   | 0.636               | 0.141                |
| cerebras-13b            |                   | 0.635               | 0.146                |
| chatglm-6b              | 985               |                     |                      |
| dolly-v2-12b            | 944               |                     |                      |
| fastchat-t5-3b          | 951               |                     |                      |
| gpt-neox-20b            |                   | 0.719               | 0.347                |
| gptj-6b                 |                   | 0.683               | 0.234                |
| koala-13b               | 1082              |                     |                      |
| llama-7b                |                   | 0.738               | 0.443                |
| llama-13b               | 932               |                     |                      |
| mpt-7b                  |                   | 0.702               | 0.343                |
| opt-7b                  |                   | 0.677               | 0.227                |
| opt-13b                 |                   | 0.692               | 0.282                |
| stablelm-base-alpha-7b  |                   | 0.533               | 0.049                |
| stablelm-tuned-alpha-7b | 858               |                     |                      |
| vicuna-13b              | 1169              |                     |                      |
| oasst-pythia-7b         |                   | 0.667               | 0.198                |
| oasst-pythia-12b        | 1065              | 0.704               | 0.233                |

## Benchmarks

| Benchmark Name    | Author         | Link                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | -------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chatbot Arena Elo | LMSYS          | https://lmsys.org/blog/2023-05-03-arena/ | "In this blog post, we introduce Chatbot Arena, an LLM benchmark platform featuring anonymous randomized battles in a crowdsourced manner. Chatbot Arena adopts the Elo rating system, which is a widely-used rating system in chess and other competitive games." (Source: https://lmsys.org/blog/2023-05-03-arena/)                                                                                                                                                                                                                                                                 |
| LAMBADA           | Paperno et al. | https://arxiv.org/abs/1606.06031"        | "The LAMBADA evaluates the capabilities of computational models for text understanding by means of a word prediction task. LAMBADA is a collection of narrative passages sharing the characteristic that human subjects are able to guess their last word if they are exposed to the whole passage, but not if they only see the last sentence preceding the target word. To succeed on LAMBADA, computational models cannot simply rely on local context, but must be able to keep track of information in the broader discourse." (Source: https://huggingface.co/datasets/lambada) |
| TriviaQA          | Joshi et al.   | https://arxiv.org/abs/1705.03551v2"      | "We present TriviaQA, a challenging reading comprehension dataset containing over 650K question-answer-evidence triples. TriviaQA includes 95K question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents, six per question on average, that provide high quality distant supervision for answering the questions." (Source: https://arxiv.org/abs/1705.03551v2)                                                                                                                                                                              |

## Sources

| Author   | Link                                     |
| -------- | ---------------------------------------- |
| LMSYS    | https://lmsys.org/blog/2023-05-03-arena/ |
| MOSAICML | https://www.mosaicml.com/blog/mpt-7b     |

<div align="center">

# kamalbhue547

**Machine learning · data · open source**

Building small, well-tested ML projects and writing down what I learn along the way.

<a href="#top-10-repositories">Projects</a> ·
<a href="#topics-i-work-on">Topics</a> ·
<a href="#research-interests">Research</a> ·
<a href="#toolbox">Toolbox</a> ·
<a href="#connect">Connect</a>

</div>

---

## About

I work on machine learning end to end — framing a question, cleaning the data,
training something small enough to understand, then measuring it honestly
instead of trusting a single accuracy number.

Current focus: **evaluating language models** and **retrieval-augmented systems**
— what breaks, how to measure it, and how to make the results reproducible.

<details>
<summary><b>What I care about in code</b></summary>

<br>

- Reproducible by default: pinned seeds, pinned versions, one command to rerun.
- Baselines before models — a mean predictor beats an unmeasured neural net.
- Small and readable beats large and clever.
- Every notebook ends with a number, a chart, and a limitation.

</details>

---

## Top 10 repositories

<!-- TOP-REPOS:START -->

**5** public repositories · **0** stars · **0** forks  
<sub>Ranked by stars, then forks, then most recent push · refreshed 29 Oct 2026</sub>

| # | Repository | Description | Stack | ★ | Last push |
|:--:|---|---|---|:--:|:--:|
| 1 | [**Mskamal4**](https://github.com/kamalbhue547/Mskamal4) | — | JavaScript | 0 | 2026-10-29 |
| 2 | [**Mskamal-**](https://github.com/kamalbhue547/Mskamal-) | Software Developer \| Building cool things for the web \| Open Source E… | — | 0 | 2026-10-29 |
| 3 | [**Mskamal3**](https://github.com/kamalbhue547/Mskamal3) | Software Developer \| Building cool things for the web \| Open Source E… | — | 0 | 2026-10-27 |
| 4 | [**Mskamal2**](https://github.com/kamalbhue547/Mskamal2) | Software Developer \| Building cool things for the web \| Open Source E… | HTML | 0 | 2026-10-27 |
| 5 | [**Mskamal1**](https://github.com/kamalbhue547/Mskamal1) | Software Developer \| Building cool things for the web \| Open Source E… | Go | 0 | 2026-10-26 |

<!-- TOP-REPOS:END -->

---

## Topics I work on

| Area | What it means in practice | Explore |
|---|---|---|
| **LLM evaluation** | Benchmarks that survive scrutiny — contamination checks, error taxonomies, human baselines. | [topic](https://github.com/topics/llm-evaluation) |
| **Retrieval-augmented generation** | Chunking, embeddings, reranking, and honest retrieval metrics. | [topic](https://github.com/topics/retrieval-augmented-generation) |
| **NLP** | Text classification, information extraction, transformers. | [topic](https://github.com/topics/nlp) |
| **Interpretability** | Attention probes, feature attributions, behavioural test batteries. | [topic](https://github.com/topics/interpretability) |
| **Small & efficient models** | Distillation, quantisation, running on CPU or edge devices. | [topic](https://github.com/topics/edge-ai) |
| **MLOps** | Experiment tracking, reproducible training, model and data versioning. | [topic](https://github.com/topics/mlops) |
| **Datasets** | Cleaning, documenting, and licensing data so others can reuse it. | [topic](https://github.com/topics/dataset) |
| **Data analysis** | Exploratory analysis, statistics, and visual storytelling. | [topic](https://github.com/topics/data-analysis) |

---

## Research interests

Questions I keep coming back to, with the reading that shaped them.

<details>
<summary><b>1. How do you evaluate a model when the labels are wrong?</b></summary>

<br>

Human annotations disagree with each other more often than leaderboards admit.
I am interested in evaluation that reports **agreement intervals** rather than a
single score, and in methods for auditing benchmark labels at scale.

*Reading:* inter-annotator agreement, Krippendorff's α, benchmark contamination studies.

</details>

<details>
<summary><b>2. Does retrieval actually improve answers, or just add latency?</b></summary>

<br>

RAG systems are usually judged by the final answer only. I want ablations that
separate **retrieval quality** from **generation quality** — recall@k, rerank gain,
and answer-faithfulness scores reported side by side.

*Reading:* embedding evaluation, reranking, attribution and faithfulness metrics.

</details>

<details>
<summary><b>3. What is the smallest model that still solves the task?</b></summary>

<br>

Distil, quantise, and prune until quality breaks, then document the break point.
A useful artifact is a curve, not a checkpoint.

*Reading:* knowledge distillation, quantisation-aware training, CPU-inference budgets.

</details>

---

## Toolbox

**Languages**
`Python` · `SQL` · `Bash` · `JavaScript`

**ML / data**
`PyTorch` · `scikit-learn` · `pandas` · `NumPy` · `Hugging Face` · `Jupyter`

**Tooling**
`Git` · `Docker` · `Linux` · `GitHub Actions` · `pytest`

---

## How I work

1. **Question** — write the claim I want to test in one sentence.
2. **Data** — document source, licence, and every cleaning step.
3. **Baseline** — simplest possible thing that runs.
4. **Experiment** — one change at a time, logged.
5. **Report** — results, failure cases, and what I would do next.

---

## Connect

- **GitHub** — you are here; open an issue on any repo.
- **Collaboration** — happy to pair on evaluation, retrieval, or data-cleaning work.

<!--
  Add your links below and delete this comment.
  Keep the profile README honest: only list what is actually there.

  - Email:      you@example.com
  - LinkedIn:   https://www.linkedin.com/in/your-handle
  - X:          https://x.com/your-handle
  - Website:    https://your-site.dev
  - Kaggle:     https://www.kaggle.com/your-handle
-->

---

<sub>The Top 10 table above is regenerated daily by <a href=".github/workflows/update-top-repos.yml">a GitHub Action</a> that reads the public repository list and commits the result.</sub>

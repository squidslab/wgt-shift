# Exploring the Socio-Technical Motivations Behind the Adoption and Migration of Web GUI Testing Frameworks

**Authors:** [Giuseppe Di Martino](https://scholar.google.com/citations?user=m2tMSNsAAAAJ), [Sergio Di Meglio](https://scholar.google.com/citations?user=LDz9rscAAAAJ), [Valeria Pontillo](https://scholar.google.com/citations?user=rhiPYd4AAAAJ), and [Luigi Libero Lucio Starace](https://scholar.google.com/citations?user=_GsQ6z8AAAAJ)

This repository contains the replication package of the paper "Exploring the Socio-Technical Motivations Behind the Adoption and Migration of Web GUI Testing Frameworks".

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19741374.svg)](https://doi.org/10.5281/zenodo.19741374)

## 🔍 Abstract
Web Graphical User Interface (GUI) testing frameworks are widely used to automate end-to-end testing of modern web applications. While prior research has explored their performance and technical features, limited attention has been directed to the socio-technical motivations that drive their adoption and migration in practice. To address this gap, this paper explores the socio-technical motivations behind the adoption and migration of web GUI testing frameworks through a repository-based study of open-source projects that use them. Specifically, we analyzed commit messages and issue discussions associated with web GUI testing framework adoption and migration events, and manually identified explicit rationale statements. This process yielded 72 relevant messages supporting 52 justified events, from which we inductively derived a thematic categorization of eight socio-technical motivations. Our results indicate that initial adoption is primarily shaped by usability and integration considerations, whereas migration is more strongly associated with reliability, performance, and ecosystem alignment, providing empirical evidence that the criteria guiding framework decisions evolve over the lifecycle of web GUI testing infrastructure.

**Keywords**: Web GUI testing, Trustworthy software engineering, Explainability, Testing infrastructure, Tool migration

## 🗂️ Contents
* **[Data](./data)**: Contains all the data used in the study. *(See the README inside for a detailed data dictionary).*
* **[Software](./software)**: Contains the code for data retrieval, filtering, manual labeling, and database integration. *(See the README inside for setup instructions).*
* **[Appendix A: Filtering Keywords](./Appendix_A_Filtering_Keywords.md)** - This document contains the complete list of keywords used for filtering commits and issues in the study.

## 🚀 How to Reproduce the Study
To reproduce the study, please refer to the **[Software README](./software/README.md)**. It contains step-by-step instructions on how to install the required dependencies and execute the scripts.

## 🔗 Citation
If you use this dataset or code in your research, please cite our paper:
```bibtex
@InProceedings{dimartino2027exploring,
author="Di Martino, Giuseppe
and Di Meglio, Sergio
and Pontillo, Valeria
and Starace, Luigi Libero Lucio",
editor="Berger, Christian
and Kl{\"o}s, Verena",
title="Exploring the Socio-Technical Motivations Behind the Adoption and Migration of Web GUI Testing Frameworks",
booktitle="Software Engineering and Advanced Applications",
year="2027",
publisher="Springer Nature Switzerland",
address="Cham",
pages="549--565",
doi="10.1007/978-3-032-36590-3_38",
isbn="978-3-032-36590-3"
}
```
🔗 [Official Publisher Version (Springer)](https://doi.org/10.1007/978-3-032-36590-3_38) | 📄 [Author's version available here](https://valeriapontillo.github.io/documents/conference/C16.pdf)
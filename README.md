# VeRA
Short for **Ve**ctor database **R**etrieval **A**ugmentation, this is the repository for our project [Optimizing Knowledge Retrieval: A Benchmark-Driven Study of VecDB-RAG Integration](https://docs.google.com/document/d/13yx3XScTGULd6qjurmfKDtxGTUyCnVipCwJbkU5m60g/edit?usp=sharing).

<img width="727" alt="image" src="https://github.com/user-attachments/assets/39803c03-9ddf-4de8-afd0-6243626e4a25">

VeRA is aimed at addressing the limitations and challenges faced by Large Language Models (LLMs) by integrating Vector Databases (VecDBs) with Retrieval-Augmented Generation (RAG) models. LLMs often suffer from issues such as hallucinations, lack of domain expertise, and bias in their responses, which hinder their reliability and real-time knowledge updates. Moreover, the computational resources required for training and operating LLMs requires heavy computational resources.

The project proposes a solution by leveraging VecDBs to provide efficient storage and retrieval of domain-specific knowledge for RAG models. By integrating VecDBs, RAG models can access up-to-date and contextually relevant data, leading to more accurate and relevant responses. 

We also aim to develop a standardized evaluation framework to assess the performance of various VecDB-RAG combinations and conduct comparative analyses with different types of open-source vector databases. By optimizing the retrieval procedure and exploring alternative algorithms, we seek to enhance the efficiency and effectiveness of RAG models in dynamically evolving environments. Time and resources permitting, we also aim to explore the performance of various algorithms in optimally matching and retrieving relevant records from the VecDB.

The benchmark is proposed to evaluate the performance of the Vector DB - RAG model based on the following metrics:
- Retrieval Latency
- Throughput
- Computational Complexity
- Scalability

Some open-source vector databases that can be considered for this project include:
- FAISS
- Milvus
- Weaviate

## Key Features

- Integration of VecDBs with RAG models
- Efficient storage and retrieval of domain-specific knowledge
- Real-time updates and contextually relevant responses
- Development of standardized evaluation frameworks

## Report

Find the detailed report on the project [here](VeRA_Report.pdf).

## Online Proceedings
Check out our SPOTLIGHT Paper in the proceedings [here](https://disml2024.github.io/disml-workshop-2024/)

## Contributors
- Vihang Pancholi
- Shubh Mehta
- Aditi Ganapathi

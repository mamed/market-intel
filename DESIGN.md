# Project: Market Intelligence Multi-Agent RAG

## 1. Vision
Build a production-ready, multi-agent system capable of ingesting real-time market data (news, social, financial) to provide synthesized market intelligence.

## 2. System Architecture
The system follows a **Manager-Worker** agentic pattern.

### 2.1 Agentic Orchestration
- **Orchestrator (Manager):** Routes queries, manages the conversation state, and decomposes complex user requests into sub-tasks.
- **Researcher (Worker):** Handles live web searching, news feed scraping, and PDF data extraction.
- **Analyst (Worker):** Performs data cleaning, statistical calculation, and trend identification using a Python tool.
- **Synthesizer (Worker):** Finalizes the report, ensuring brand voice and formatting consistency.

### 2.2 Technical Stack
- **Language:** Python 3.11
- **Orchestration Framework:** LangGraph (to manage cyclic agent states)
- **Vector Database:** Qdrant (Hybrid search: Vector + BM25)
- **LLM Providers:** 
    - **Reasoning:** Claude 3.5 Sonnet or GPT-4o
    - **Embeddings:** nomic-embed-text-v1.5
- **Inference:** local `llama-server` (GGUF) for low-cost processing tasks.
- **Infrastructure:** Docker, Docker Compose, Nginx (optional for API).

## 3. Data Pipeline
1. **Ingestion:** Real-time scrapers & RSS feeds $\rightarrow$ Raw Data $\rightarrow$ Cleaning Pipeline.
2. **Indexing:** Semantic Chunking $\rightarrow$ Vector Embedding $\rightarrow$ Vector DB Indexing.
3. **Retrieval:** Hybrid Search $\rightarrow$ Contextual Reranking $\rightarrow$ Agent Input.

## 4. Development Roadmap
- [x] **Phase 1: System Audit & Optimization**
- [x] **Phase 2: Research & Architecture Design**
- [ ] **Phase 3: Project Scaffolding (Infrastructure)**
- [ ] **Phase 4: Agent & Tool Implementation**
- [ ] **Phase 5: QA & Deployment**

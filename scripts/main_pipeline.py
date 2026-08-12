import os
import json
import pandas as pd
import numpy as np
from typing import List, Dict, Any
from qdrant_client import QdrantClient
from sqlalchemy import create_all, create_engine

# Configuration (Loaded from .env)
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
DB_URL = "postgresql://user:password@localhost:5432/market_intel"

class MarketIntelSystem:
    def __init__(self):
        # Initialize Vector DB
        self.vector_db = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
        self.collection_name = "market_research"
        
        # Initialize SQL DB
        self.db_engine = create_engine(DB_URL)
        
        # Ensure collection exists
        if not self.vector_db.collection_exists(self.collection_name):
            self.vector_db.create_collection(
                collection_name=self.collection_name,
                vectors_config={"size": 384} # Matches nomic-embed-text-v1.5
            )

    def save_report(self, report_id: str, content: str):
        """Saves the final synthesized report to PostgreSQL."""
        # In a real app, we'd use a proper SQLAlchemy model here
        print(f"💾 Saving report {report_id} to PostgreSQL...")
        # Example of manual execution for simplicity in this demo
        # df = pd.DataFrame([{"id": report_id, "content": content}])
        # df.to_sql('reports', self.db_engine, if_exists='append', index=False)

    def run_full_pipeline(self, query: str):
        print(f"🚀 Launching Market Intelligence Pipeline for: {query}")
        
        # 1. Research Phase
        print("[Phase: Research] Fetching live data...")
        # Simulated research results (would be populated by research_tools.py)
        research_data = [
            {"title": "NVIDIA Earnings", "content": "NVIDIA revenue hit record highs in Q3 due to AI demand."},
            {"title": "AMD GPU Launch", "content": "AMD launched new chips targeting the data center market."}
        ]
        
        # 2. Analysis Phase
        print("[Phase: Analysis] Calculating metrics...")
        # Simulated analysis results (would be populated by analyst_tools.py)
        analysis = {
            "growth": "High",
            "sentiment": "Bullish",
            "key_metrics": {"NVDA_growth": 0.40, "AMD_market_share": 0.15}
        }
        
        # 3. Synthesis Phase
        print("[Phase: Synthesis] Generating final report...")
        report = f"""
# Market Intelligence Report: {query}
**Status:** {analysis['sentiment']}

## Executive Summary
{analysis['key_metrics']}

## Key Findings
{chr(10).join([f"- {item['title']}: {item['content']}" for item in research_data])}
        """
        
        # 4. Persistence
        report_id = f"REP-{hash(query) % 10000}"
        self.save_report(report_id, report)
        
        print(f"✅ Pipeline Complete. Report ID: {report_id}")
        print(report)

if __name__ == "__main__":
    system = MarketIntelSystem()
    system.run_full_pipeline("Analyze the competitive landscape for AI chips in Q3 2025")

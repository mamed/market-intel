import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from typing import List, Dict, Union

class AnalystTools:
    """Tools for the Analyst Agent to perform quantitative analysis."""
    
    def __init__(self, output_dir="/tmp/market_intel_analysis"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def calculate_growth_metrics(self, data: List[Dict]) -> Dict:
        """
        Calculates % growth and average values from a list of transaction records.
        Expects records with 'amount' and 'timestamp' keys.
        """
        if not data:
            return {"error": "No data provided"}
            
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Sort by time
        df = df.sort_values('timestamp')
        
        # Calculate daily averages
        daily_avg = df.resample('D', on='timestamp')['amount'].mean().to_dict()
        
        # Calculate % growth (change from previous period)
        df['prev_amount'] = df['amount'].shift(1)
        df['growth_pct'] = ((df['amount'] - df['prev_amount']) / df['prev_amount']) * 100
        
        summary = {
            "mean_amount": round(df['amount'].mean(), 2),
            "max_amount": round(df['amount'].max(), 2),
            "min_amount": round(df['amount'].min(), 2),
            "total_growth": round(df['growth_pct'].mean(), 2)
        }
        
        return summary

    def generate_trend_chart(self, data: List[Dict], output_filename: str) -> str:
        """
        Generates a simple trend chart and returns the path to the saved image.
        """
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        
        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['amount'], marker='o', linestyle='-')
        plt.title("Market Trend Analysis")
        plt.xlabel("Time")
        plt.ylabel("Amount")
        plt.grid(True)
        
        # Save to our output dir
        path = os.path.join(self.output_dir, output_filename)
        plt.savefig(path)
        plt.close()
        
        return path

if __name__ == "__main__":
    tools = AnalystTools()
    # Test Data
    mock_data = [
        {"timestamp": "2026-01-01 10:00:00", "amount": 100.0},
        {"timestamp": "2026-01-02 10:00:00", "amount": 150.0},
        {"timestamp": "2026-01-03 10:00:00", "amount": 130.0},
        {"timestamp": "2026-01-04 10:00:00", "amount": 200.0},
    ]
    print(f"Metrics: {tools.calculate_growth_metrics(mock_data)}")
    print(f"Chart saved to: {tools.generate_trend_chart(mock_data, 'trend_analysis.png')}")

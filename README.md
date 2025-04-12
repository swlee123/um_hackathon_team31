# um_hackathon_Team31

## Objective
Develop a Machine Learning (ML) model that analyzes on-chain data from various sources (e.g., CryptoQuant, Glassnode, Coinglass) to generate an alpha trading strategy that maximizes profit. The model should effectively extract implicit indicators from noisy data to generate profitable trading signals.

## 📚 Table of Contents


1. [🚀 Project Overview](#project-overview)
2. [⚙️ Installation](#installation)
3. [Conceptual Diagram](#)
4. [Class Diagram](#)
5. [📊 Model and Strategy Design](#)

    This includes technical architecture and details of the design and common assumptions for this backtesting framework,

6. [📁 Folder Structure](#)
7. [🔧 YAML Configuration](\docs\configurations.md)

### Project Overview 

This project is a modular quantitative trading backtesting framework designed to support multiple strategy paradigms including:

- Rule-Based (Technical Analysis)

- Hidden Markov Models (HMM)

- HMM combined with Natural Language Processing (NLP) using VADER Sentiment Analysis

### Installation 

Create a virtual environment 
```bash
python -m venv env
```
Install required library 
```bash
pip install -r requirements.txt
```

Run the **backtest_framework\main.py** to see example of backtesting under *Rule-Based* mode using MACrossover strategy
```bash
python main.py
```

### Conceptual Diagram

![Conceptual Diagram](#)

### Class Diagram 

![Class Diagram](#)


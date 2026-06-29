# AI Tender Summariser

A Python tool that uses the Anthropic Claude API to automatically analyse construction tender documents and extract key information for estimators.

## What It Does

Paste in tender text and the tool returns a structured analysis including:

- **Scope of works** — bullet point breakdown of what is required
- **Key risks** — programme, commercial, and site-specific risks
- **Commercial watch points** — LDs, insurance, contract form, preliminaries
- **Questions to raise with client** — gaps in information that need clarifying before pricing

## Why I Built This

Reviewing tenders manually is time-consuming and easy to miss critical details under time pressure. This tool acts as a first-pass analysis assistant, helping estimators work faster and more consistently.

## Technology

- Python
- Anthropic Claude API (claude-sonnet-4-6)
- python-dotenv for secure API key management

## How to Use

1. Clone the repo
2. Install dependencies:
```bash
   pip install anthropic python-dotenv
```
3. Create a `.env` file with your Anthropic API key:
ANTHROPIC_API_KEY=your-key-here

4. Usage: Add your tender text to a .txt file and run the script. You will be prompted to enter the filename.
5. Run:
```bash
   python tender_summary_v1.py
```


# 00-ai-engineering-End to End Devlopment

If you do need to run the code, this is how:

- Clone the repository.
- Run:
```bash
cp env.example .env
```

Edit `.env` and add your API keys:

```
OPENAI_API_KEY=your_google_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```
Keep the remaining configuration as per ```.env.example```.


#### To run the project, execute:

```bash
make run-docker-compose
```

Streamlit application: http://localhost:8501

FastAPI documentation: http://localhost:8000/docs



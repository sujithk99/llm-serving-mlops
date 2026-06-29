\# 🚀 LLM Serving MLOps Project



\## Project Overview



This project demonstrates an end-to-end MLOps workflow for serving a Large Language Model (LLM) locally using FastAPI, Docker, Prometheus, and GitHub Actions.



The application exposes REST APIs for inference, supports containerized deployment, includes automated testing, monitoring, and CI/CD.



\---



\## Features



\- Local LLM inference using Qwen2.5-0.5B-Instruct

\- FastAPI REST API

\- Swagger UI documentation

\- Docker containerization

\- Automated testing with Pytest

\- Prometheus monitoring

\- GitHub Actions CI pipeline



\---



\## Tech Stack



\- Python

\- FastAPI

\- Hugging Face Transformers

\- PyTorch

\- Docker

\- Pytest

\- Prometheus

\- GitHub Actions

\- Git



\---



\## API Endpoints



\### Health Check



GET



```

/ping

```



Response



```json

{

&#x20; "status":"healthy"

}

```



\---



\### Inference



POST



```

/invocations

```



Example



```json

{

&#x20; "prompt":"Explain Docker"

}

```



\---



\### Metrics



GET



```

/metrics

```



Returns Prometheus metrics.



\---



\## Project Structure



```text

app/

tests/

.github/workflows/

Dockerfile

requirements.txt

pytest.ini

README.md

```



\---



\## How to Run



Create virtual environment



```

python -m venv venv

```



Activate



```

venv\\Scripts\\activate

```



Install dependencies



```

pip install -r requirements.txt

```



Start API



```

uvicorn app.main:app --reload

```



Open



```

http://localhost:8000/docs

```



\---



\## CI/CD



GitHub Actions automatically:



\- Installs dependencies

\- Runs automated tests

\- Validates every push



\---



\## Monitoring



Prometheus metrics available at



```

/metrics

```



\---



\## Future Improvements



\- Kubernetes deployment

\- Model versioning

\- MLflow integration

\- Authentication

\- Cloud deployment



\---



\## Author



Sujith Kumar S


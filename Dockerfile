# Build from ~/Projects:
#   docker build -f raphael-workflows/Dockerfile .
FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY raphael-contracts /deps/raphael-contracts
RUN uv pip install --system /deps/raphael-contracts
COPY raphael-workflows/pyproject.toml raphael-workflows/README.md ./
COPY raphael-workflows/src ./src
RUN python3 -c "import re; from pathlib import Path; p=Path('pyproject.toml'); p.write_text(re.sub(r'\n\[tool\.uv\.sources\][^\[]*','\n',p.read_text(),flags=re.S))"
RUN uv pip install --system -e .
ENV RAPHAEL_SERVICE_PORT=8094
EXPOSE 8094
CMD ["uvicorn", "raphael_workflows.app:app", "--host", "0.0.0.0", "--port", "8094"]

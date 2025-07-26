FROM python:3.9
WORKDIR /app
COPY pipeline.py .
RUN pip install pandas
ENTRYPOINT [ "python", "pipeline.py"  ]

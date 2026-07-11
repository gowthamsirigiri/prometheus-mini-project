FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Copy the requirements file into the container
COPY requirements.txt /tmp/

# Install the dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

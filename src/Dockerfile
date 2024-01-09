FROM python:3.9

# Install Rust and Cargo
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

# Set Rust environment variables
ENV PATH="/root/.cargo/bin:${PATH}"
ENV CARGO_HOME="/root/.cargo"
ENV RUSTUP_HOME="/root/.rustup"

WORKDIR /app

COPY . /app

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 800

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]

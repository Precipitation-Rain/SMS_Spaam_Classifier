# 1. Base image
FROM python:3.13-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy project files
COPY . .

# 5. Download NLTK data
RUN python -m nltk.downloader punkt punkt_tab stopwords

# 6. Expose port for Streamlit
EXPOSE 8501

# 7. Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
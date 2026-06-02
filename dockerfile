# Step 1: Use an official lightweight Python image
FROM python:3.7-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application files
COPY app.py .

# Step 6: Expose port 5000 inside the container
EXPOSE 5000

# Step 7: Command to run the application when the container starts
CMD ["python", "app.py"]
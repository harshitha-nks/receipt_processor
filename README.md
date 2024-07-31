# Receipt Processor Service

This service processes receipts and calculates points based on the provided rules.

## Running the application

### Using Docker

1. Ensure you have Docker installed on your system. You can download it from [here](https://www.docker.com/products/docker-desktop).

2. Build the Docker image:

   ```
   docker build -t receipt-processor .
   ```
3. Run the docker container

    ```
    docker run -p 5000:5000 receipt-processor
    ```
4. To test the application, open a new command line and run:

    ```
    python3 test.py
    ```

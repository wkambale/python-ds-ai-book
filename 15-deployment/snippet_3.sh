# Build the image

docker build -t mobicash-api:1.0.0 .

docker run -d \
  --name mobicash-api \
  -p 8000:8000 \
  -e API_KEY=your-secret-key \
  mobicash-api:1.0.0

docker logs mobicash-api

docker stop mobicash-api && docker rm mobicash-api

docker-compose up --build
# Example: Deploy to Google Cloud Run
# (Requires gcloud CLI and a GCP project)
# Build and push to Google Container Registry

gcloud builds submit --tag gcr.io/PROJECT_ID/mobicash-api:1.0.0

gcloud run deploy mobicash-api \
  --image gcr.io/PROJECT_ID/mobicash-api:1.0.0 \
  --platform managed \
  --region africa-south1 \  # Use region closest to your users
  --memory 1Gi \
  --cpu 1 \
  --min-instances 0 \       # Scale to zero when idle
  --max-instances 10 \
  --set-env-vars "API_KEY=your-production-key"
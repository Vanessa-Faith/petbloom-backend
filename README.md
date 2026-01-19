# PetBloom Backend API

FastAPI backend for PetBloom e-commerce platform.

## Railway Deployment

### Prerequisites
1. Railway account (https://railway.app)
2. GitHub repository with backend code
3. Firebase Admin SDK credentials

### Deployment Steps

#### 1. Create Railway Project
- Go to https://railway.app
- Click "New Project"
- Select "Deploy from GitHub repo"
- Select your backend repository

#### 2. Add PostgreSQL Database
- Click "+ New" → "Database" → "PostgreSQL"
- Railway will automatically create `DATABASE_URL` variable

#### 3. Set Environment Variables
Go to your backend service → Variables tab and add:

```
DATABASE_URL=<automatically set by Railway>
FRONTEND_URL=https://your-app.vercel.app
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_KEY\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@your-project.iam.gserviceaccount.com
PORT=8000
```

#### 4. Deploy
- Railway will automatically deploy
- Get your backend URL (e.g., `https://petbloom-backend.railway.app`)

#### 5. Update Frontend
Update frontend `.env.production`:
```
VITE_API_URL=https://your-backend.railway.app/api/v1
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Generate Prisma client
prisma generate

# Run migrations
prisma db push

# Seed database (optional)
python seed.py

# Start server
uvicorn app.main:app --reload --port 8000
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /api/v1/users/` - Create user
- `GET /api/v1/pets/` - List pets
- `GET /api/v1/products/` - List products
- `POST /api/v1/cart/` - Add to cart
- `POST /api/v1/orders/` - Create order

Full API docs: `/docs` (Swagger UI)

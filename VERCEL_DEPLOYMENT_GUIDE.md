# 🚀 Deploy ECHO to Vercel - Complete Guide

## Step 1: Create Vercel Account
1. Go to https://vercel.com
2. Click **Sign Up**
3. Choose **Sign up with GitHub** (easier for automatic deployment)
4. Authorize Vercel to access your GitHub account

## Step 2: Import Your GitHub Repository

1. After signing in, click **Add New Project**
2. Click **Import Git Repository**
3. Paste: `https://github.com/Taran-heera/codds.git`
4. Click **Continue**

## Step 3: Configure Project Settings

**Framework**: React
**Root Directory**: `./frontend`
**Build Command**: `npm run build`
**Output Directory**: `build`

### Environment Variables:
1. Click **Environment Variables**
2. Add the following:
   - **Name**: `REACT_APP_API_URL`
   - **Value**: `https://your-backend-url.com` (We'll set this after backend deployment)
   - **Save**

## Step 4: Deploy Frontend

1. Click **Deploy**
2. Wait for build to complete (usually 2-5 minutes)
3. You'll get a URL like: `https://codds.vercel.app`

---

## Step 5: Deploy Backend (Choose One Option)

### Option A: Railway (Recommended - Easiest)

**Prerequisites:**
- GitHub account (already have it)
- Credit card (free tier available, ~$5/month for always-on)

**Steps:**
1. Go to https://railway.app
2. Click **Create New Project**
3. Select **Deploy from GitHub repo**
4. Authorize Railway to access GitHub
5. Select **Taran-heera/codds** repository
6. Railway will automatically detect it's a Python project
7. Add environment variables:
   - `FLASK_ENV=production`
   - `MONGODB_URI=your-mongodb-connection-string`
   - `JWT_SECRET=your-secret-key`
   - `SMTP_SERVER=smtp.gmail.com` (optional, for emails)
   - `SMTP_PORT=587`
   - `SENDER_EMAIL=your-email@gmail.com`
   - `SENDER_PASSWORD=your-app-password`
8. Deploy
9. Get your backend URL (e.g., `https://codds-production.up.railway.app`)

### Option B: Heroku (Free tier limited)

1. Go to https://heroku.com
2. Create new app: `codds-api`
3. Connect to GitHub repository
4. Add `Procfile` to backend:
   ```
   web: python app.py
   ```
5. Add buildpack for Python
6. Deploy
7. Get backend URL

### Option C: Render (Free + Paid)

1. Go to https://render.com
2. Click **New +** → **Web Service**
3. Connect GitHub
4. Select repository
5. Set:
   - Name: `codds-api`
   - Runtime: `Python 3`
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`
6. Deploy

---

## Step 6: Update Frontend with Backend URL

Once backend is deployed:

1. Go back to Vercel Dashboard
2. Select your `codds` project
3. Go to **Settings** → **Environment Variables**
4. Update `REACT_APP_API_URL` to your backend URL
5. Go to **Deployments** → click latest deployment → **Redeploy**

---

## Step 7: Update API Endpoints in Code

Edit your frontend files to use the environment variable:

**File**: `frontend/src/pages/Dashboard.jsx`
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000';

const response = await fetch(`${API_URL}/api/analyze/text`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({ text: analysisText })
});
```

Do this for all pages that call the API:
- `BatchAnalyzer.jsx`
- `UserProfile.jsx`
- `APIKeys.jsx`
- `AdminDashboard.jsx`

---

## Step 8: Setup MongoDB (If Not Already Done)

1. Go to https://mongodb.com/cloud/atlas
2. Create Free Cluster
3. Get connection string (looks like: `mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/dbname`)
4. Add to backend environment variables as `MONGODB_URI`

---

## Step 9: Enable CORS on Backend

Edit `backend/app/__init__.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://codds.vercel.app",
            "http://localhost:3000"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

Install flask-cors:
```bash
pip install flask-cors
```

---

## Step 10: Verify Deployment

1. **Frontend**: Visit https://codds.vercel.app
   - Check if it loads
   - Try login with admin/password
   
2. **Backend**: Test API endpoints
   ```bash
   curl https://your-backend-url.com/api/analyze/text \
     -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -d '{"text":"test content here"}'
   ```

---

## Automatic Updates

- **Frontend**: Any push to `main` branch on GitHub will automatically deploy to Vercel
- **Backend**: Same with Railway/Render - automatic on push to `main`

---

## Common Issues & Solutions

### Issue: "Cannot connect to backend"
**Solution**: 
- Check backend URL in environment variables
- Verify CORS is enabled
- Check backend is actually deployed and running

### Issue: "MongoDB connection refused"
**Solution**:
- Verify MongoDB connection string is correct
- Check whitelist IP on MongoDB Atlas (add `0.0.0.0/0` for all IPs)

### Issue: "Module not found" error on backend
**Solution**:
- Add `requirements.txt` to backend root:
  ```
  Flask==2.3.0
  Flask-CORS==4.0.0
  PyMongo==4.3.3
  PyJWT==2.8.0
  reportlab==4.0.4
  python-dotenv==1.0.0
  ```

### Issue: "REACT_APP_API_URL not updating"
**Solution**:
- Vercel caches builds - force redeploy:
  1. Go to Deployments
  2. Click latest deployment
  3. Click "..." → **Redeploy**

---

## Final URLs

After deployment:
- **Frontend**: https://codds.vercel.app
- **Backend**: https://codds-api.railway.app (or your chosen platform)
- **GitHub**: https://github.com/Taran-heera/codds

---

## Cost Summary

| Service | Cost | Notes |
|---------|------|-------|
| Vercel | FREE | Frontend hosting (unlimited) |
| Railway | ~$5-10/mo | Backend + MongoDB (very affordable) |
| MongoDB Atlas | FREE | Free tier with 512MB storage |
| **TOTAL** | **~$5-10/month** | Production-ready |

---

## Next Steps

1. Deploy to Railway (backend)
2. Get backend URL
3. Update Vercel environment variables
4. Redeploy frontend
5. Test everything works
6. Share live URL: https://codds.vercel.app

Questions? Follow the troubleshooting section above!

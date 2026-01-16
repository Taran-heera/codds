# 🚀 SIMPLEST DEPLOYMENT - Replit (Just 3 Clicks!)

## What is Replit?
- Free hosting for both frontend & backend
- Auto-deploys from GitHub
- No configuration needed
- Works right away

---

## Deploy in 3 Steps:

### **Step 1: Go to Replit**
Open: https://replit.com

### **Step 2: Connect GitHub**
1. Click **Sign Up** → **Sign up with GitHub**
2. Authorize Replit to access your GitHub

### **Step 3: Create Two Projects**

#### **For Frontend:**
1. Click **+ Create** → **Import from GitHub**
2. Paste: `https://github.com/Taran-heera/codds`
3. Name it: `codds-frontend`
4. Set directory: `frontend`
5. Click **Import**
6. Wait 2-3 minutes ✅
7. Click **Run** button (green button on top)
8. Your frontend is LIVE! Get the URL (looks like: `https://codds-frontend.replit.dev`)

#### **For Backend:**
1. Click **+ Create** → **Import from GitHub** (again)
2. Paste: `https://github.com/Taran-heera/codds`
3. Name it: `codds-backend`
4. Set directory: `backend`
5. Click **Import**
6. Create `.env` file with:
   ```
   MONGODB_URI=your-mongodb-connection
   JWT_SECRET=your-secret-key
   ```
7. Click **Run** button
8. Your backend is LIVE! Get the URL

### **Step 4: Connect Them Together**
1. Go to frontend project settings
2. Add Environment Variable:
   - Name: `REACT_APP_API_URL`
   - Value: `https://codds-backend.replit.dev`
3. Click **Run** again

**DONE! Your site is live!** 🎉

---

## Cost
- **FREE** forever (with ads)
- Or **$7/month** for no ads + always-on

---

## That's It!
No configuration, no CLI commands, just click **Import** and **Run**!

Your live URLs:
- **Frontend**: `https://codds-frontend.replit.dev`
- **Backend**: `https://codds-backend.replit.dev`

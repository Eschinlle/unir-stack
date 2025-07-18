# Unir Stack

## Features

- 🤖 AI-powered code generation
- ⚡️ Real-time development environment
- 🎨 Multiple arbitrary starter templates (see `/images`)
- 👥 Team collaboration and management
- 📝 Git version control
- 🔄 Live preview
- 🧠 Chain-of-Thought reasoning for complex asks
- 🔌 Support for OpenAI and Anthropic models
- 📱 Multi-page app generation
- 📸 Sketch and screenshot uploads
- 🚀 Deployment to GitHub (+ Netlify, Vercel, etc)
- 🌙 Dark mode support
- 🔗 Share chats and projects publicly
- 💾 Prompt caching for cheaper responses
- 🖥️ Virtual browser logs and screenshots for debugging

## Setup

### Environment Configuration

See `backend/config.py` for the environment variables that are used to configure the app.

- Requires modal account to be created and configured.
- Requires AWS account and s3 bucket to be configured.
- Requieres Netlify account

### Development

- `cd frontend && npm install --force && npm run dev`
- `cd backend && pip install -r requirements.txt && python3 main.py` pero antes crea un ambiente virtual

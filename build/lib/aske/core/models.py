class GitignoreModel:
    """Model for generating .gitignore file content"""

    @staticmethod
    def get_python_gitignore():
        """Get standard Python .gitignore content"""
        return '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# Environment variables
.env
.env.*

# IDE
.idea/
.vscode/
*.swp
*.swo
.project
.pydevproject

# macOS
.DS_Store
.DS_STORE
.AppleDouble
.LSOverride
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Logs and databases
*.log
*.sqlite
*.db

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
'''

class NodejsModel:
    """Model for generating Node.js project structure and files"""

    @staticmethod
    def get_nodejs_gitignore():
        """Get standard Node.js .gitignore content"""
        return '''# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
.yarn/
.pnp.*

# Environment variables
.env
.env.*
.env.local
.env.*.local

# IDE
.idea/
.vscode/
*.swp
*.swo
.project
*.sublime-workspace
*.sublime-project

# macOS
.DS_Store
.DS_STORE
.AppleDouble
.LSOverride
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Logs
logs
*.log

# Testing
coverage/
.nyc_output/

# Build
dist/
build/
out/
.next/
'''

    @staticmethod
    def get_package_json(name):
        """Generate package.json content"""
        return f'''{{
  "name": "{name}",
  "version": "1.0.0",
  "description": "",
  "main": "src/index.js",
  "scripts": {{
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "lint": "eslint .",
    "format": "prettier --write ."
  }},
  "keywords": [],
  "author": "",
  "license": "MIT",
  "dependencies": {{
    "dotenv": "^16.0.0",
    "express": "^4.18.0"
  }},
  "devDependencies": {{
    "eslint": "^8.0.0",
    "jest": "^29.0.0",
    "nodemon": "^3.0.0",
    "prettier": "^3.0.0"
  }}
}}'''

    @staticmethod
    def get_prettierrc():
        """Generate .prettierrc content"""
        return '''{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}'''

    @staticmethod
    def get_eslintrc():
        """Generate .eslintrc content"""
        return '''{
  "env": {
    "node": true,
    "es2021": true,
    "jest": true
  },
  "extends": ["eslint:recommended"],
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "indent": ["error", 2],
    "linebreak-style": ["error", "unix"],
    "quotes": ["error", "single"],
    "semi": ["error", "always"]
  }
}'''

    @staticmethod
    def get_index_js():
        """Generate index.js content"""
        return '''require('dotenv').config();
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'Welcome to your Node.js application!' });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
'''

    @staticmethod
    def get_env():
        """Generate .env content"""
        return '''# Server Configuration
PORT=3000
NODE_ENV=development

# Add your environment variables here
'''

class NextjsModel:
    """Model for generating Next.js project structure and files"""

    @staticmethod
    def get_nextjs_gitignore():
        """Get standard Next.js .gitignore content"""
        return '''# Next.js
.next/
out/
build/
dist/

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
.yarn/
.pnp.*

# Environment variables
.env
.env.*
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.idea/
.vscode/
*.swp
*.swo
.project
*.sublime-workspace
*.sublime-project

# macOS
.DS_Store
.DS_STORE
.AppleDouble
.LSOverride
._*

# TypeScript
*.tsbuildinfo
next-env.d.ts

# Testing
/coverage
.nyc_output

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Vercel
.vercel
'''

    @staticmethod
    def get_model_prompt_component():
        """Generate ModelPrompt component"""
        return '''"use client";

import { useState } from 'react';

interface ModelPromptProps {
  onSubmit: (input: string) => void;
}

const ModelPrompt: React.FC<ModelPromptProps> = ({ onSubmit }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    onSubmit(input.trim());
    setInput('');
  };

  return (
    <div style={{ margin: '2rem 0' }}>
      <h2>Model Prompt</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your prompt..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{ padding: '0.5rem', width: '300px', marginRight: '1rem' }}
        />
        <button type="submit" style={{ padding: '0.5rem 1rem' }}>
          Submit
        </button>
      </form>
    </div>
  );
};

export default ModelPrompt;
'''

    @staticmethod
    def get_index_page():
        """Generate index page with ModelPrompt"""
        return '''"use client";

import ModelPrompt from '../components/ModelPrompt';

export default function Home() {
  const handlePromptSubmit = (input: string) => {
    console.log('User input:', input);
    // Add logic to process the prompt input
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Welcome to My Next.js App</h1>
      <p>This project is set up with best practices in mind.</p>
      <ModelPrompt onSubmit={handlePromptSubmit} />
    </div>
  );
}
''' 
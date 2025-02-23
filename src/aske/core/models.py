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

class ExpressModel:
    """Model for generating Express.js API project structure and files"""

    @staticmethod
    def get_express_gitignore():
        """Get standard Express.js .gitignore content"""
        return '''# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# Environment variables
.env
.env.*
.env.local
.env.development
.env.test
.env.production

# IDE
.idea/
.vscode/
*.swp
*.swo

# macOS
.DS_Store
.DS_STORE

# Logs
logs/
*.log

# Test coverage
coverage/
.nyc_output/

# Build
dist/
build/
'''

    @staticmethod
    def get_package_json(name):
        """Generate package.json content"""
        return f'''{{
  "name": "{name}",
  "version": "1.0.0",
  "description": "Express API with best practices",
  "main": "src/server.js",
  "scripts": {{
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "test": "jest",
    "lint": "eslint .",
    "format": "prettier --write ."
  }},
  "dependencies": {{
    "cors": "^2.8.5",
    "dotenv": "^16.0.0",
    "express": "^4.18.0",
    "express-validator": "^7.0.0",
    "helmet": "^7.0.0",
    "morgan": "^1.10.0",
    "winston": "^3.11.0"
  }},
  "devDependencies": {{
    "eslint": "^8.0.0",
    "jest": "^29.0.0",
    "nodemon": "^3.0.0",
    "prettier": "^3.0.0",
    "supertest": "^6.0.0"
  }}
}}'''

    @staticmethod
    def get_server_js():
        """Generate server.js content"""
        return '''require('dotenv').config();
const app = require('./app');
const logger = require('./utils/logger');

const port = process.env.PORT || 3000;

app.listen(port, () => {
  logger.info(`Server is running on port ${port}`);
});
'''

    @staticmethod
    def get_app_js():
        """Generate app.js content"""
        return '''const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const routes = require('./routes');
const errorHandler = require('./middleware/errorHandler');
const logger = require('./utils/logger');

const app = express();

// Security middleware
app.use(helmet());
app.use(cors());

// Request parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging
app.use(morgan('combined', { stream: { write: message => logger.info(message.trim()) } }));

// Routes
app.use('/api', routes);

// Error handling
app.use(errorHandler);

module.exports = app;
'''

    @staticmethod
    def get_routes_index():
        """Generate routes/index.js content"""
        return '''const express = require('express');
const userRoutes = require('./user.routes');
const healthRoutes = require('./health.routes');

const router = express.Router();

router.use('/users', userRoutes);
router.use('/health', healthRoutes);

module.exports = router;
'''

    @staticmethod
    def get_health_routes():
        """Generate health routes"""
        return '''const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

module.exports = router;
'''

    @staticmethod
    def get_user_routes():
        """Generate user routes with validation"""
        return '''const express = require('express');
const { body, validationResult } = require('express-validator');
const UserController = require('../controllers/user.controller');

const router = express.Router();

router.get('/', UserController.getAllUsers);

router.post(
  '/',
  [
    body('name').trim().notEmpty().withMessage('Name is required'),
    body('email').isEmail().withMessage('Valid email is required'),
  ],
  UserController.createUser
);

router.get('/:id', UserController.getUserById);

module.exports = router;
'''

    @staticmethod
    def get_user_controller():
        """Generate user controller"""
        return '''const logger = require('../utils/logger');

class UserController {
  static async getAllUsers(req, res, next) {
    try {
      // TODO: Implement user retrieval logic
      res.json({ users: [] });
    } catch (error) {
      logger.error('Error getting users:', error);
      next(error);
    }
  }

  static async createUser(req, res, next) {
    try {
      const { name, email } = req.body;
      // TODO: Implement user creation logic
      res.status(201).json({ name, email });
    } catch (error) {
      logger.error('Error creating user:', error);
      next(error);
    }
  }

  static async getUserById(req, res, next) {
    try {
      const { id } = req.params;
      // TODO: Implement user retrieval logic
      res.json({ id, name: 'Example User' });
    } catch (error) {
      logger.error(`Error getting user ${req.params.id}:`, error);
      next(error);
    }
  }
}

module.exports = UserController;
'''

    @staticmethod
    def get_error_handler():
        """Generate error handler middleware"""
        return '''const logger = require('../utils/logger');

function errorHandler(err, req, res, next) {
  logger.error(err.stack);

  if (err.type === 'validation') {
    return res.status(400).json({
      status: 'error',
      message: 'Validation error',
      errors: err.errors
    });
  }

  res.status(500).json({
    status: 'error',
    message: 'Internal server error'
  });
}

module.exports = errorHandler;
'''

    @staticmethod
    def get_logger():
        """Generate logger utility"""
        return '''const winston = require('winston');

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' })
  ]
});

if (process.env.NODE_ENV !== 'production') {
  logger.add(new winston.transports.Console({
    format: winston.format.simple()
  }));
}

module.exports = logger;
'''

    @staticmethod
    def get_env():
        """Generate .env content"""
        return '''# Server Configuration
PORT=3000
NODE_ENV=development
LOG_LEVEL=debug

# Add your environment variables here
# DATABASE_URL=
# JWT_SECRET=
''' 
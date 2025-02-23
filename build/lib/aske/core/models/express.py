class ExpressModel:
    """Model for generating Express.js API project structure and files"""

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
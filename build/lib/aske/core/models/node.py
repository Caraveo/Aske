class NodejsModel:
    """Model for generating Node.js project structure and files"""

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
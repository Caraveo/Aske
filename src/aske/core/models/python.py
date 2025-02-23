class PythonModel:
    """Model for generating Python project files"""

    @staticmethod
    def get_requirements():
        """Get requirements.txt content"""
        return '''# Core dependencies
python-dotenv>=1.0.0
pyyaml>=6.0
click>=8.0.0
'''

    @staticmethod
    def get_env(name):
        """Get .env content"""
        return f'''# Environment variables
DEBUG=True
APP_NAME={name}
'''

    @staticmethod
    def get_app(name):
        """Get app.py content"""
        return f'''"""
{name} application
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main application entry point"""
    pass

if __name__ == "__main__":
    main()
''' 
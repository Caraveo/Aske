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
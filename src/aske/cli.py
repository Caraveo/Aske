import click
import os
import subprocess
import sys
import shutil
import time
from aske import __version__
from aske.core.models import GitignoreModel, NodejsModel, NextjsModel

# Add color constants
RED = "\033[91m"
ORANGE = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def error_text(message):
    """Format error message in red"""
    return f"{RED}{message}{RESET}"

def command_text(message):
    """Format command in orange"""
    return f"{ORANGE}{message}{RESET}"

def success_text(message):
    """Format success message in green"""
    return f"{GREEN}{message}{RESET}"

def change_directory(path):
    """Change directory and return success status"""
    try:
        os.chdir(path)
        return True
    except Exception as e:
        click.echo(f"❌ Error changing directory: {e}", err=True)
        return False

@click.group()
@click.version_option(version=__version__)
def main():
    """ASKE - Platform Architect Development Framework"""
    pass

@main.command()
@click.argument('name')
def python(name):
    """Create a new Python project and set up its structure"""
    project_path = os.path.abspath(name)
    
    # Check if project already exists
    if os.path.exists(project_path):
        click.echo(error_text(f"❌ Error: Project directory '{name}' already exists"), err=True)
        click.echo(error_text("Please choose a different name or remove the existing directory"), err=True)
        sys.exit(1)
    
    click.echo(f"\n🚀 Creating new Python project: {name}")
    click.echo("=" * 50)

    # Create project directory
    click.echo(f"📁 Creating project directory: {project_path}")
    os.makedirs(project_path, exist_ok=False)
    
    # Create virtual environment
    click.echo("\n🔧 Setting up Python virtual environment...")
    
    # Find Python executable
    click.echo("🔍 Looking for Python executable...")
    python_executable = None
    if shutil.which(sys.executable):
        python_executable = sys.executable
        click.echo(f"✓ Using current Python: {python_executable}")
    elif shutil.which('python'):
        python_executable = 'python'
        click.echo("✓ Using 'python' command")
    elif shutil.which('python3'):
        python_executable = 'python3'
        click.echo("✓ Using 'python3' command")
    
    if not python_executable:
        click.echo(error_text("❌ Error: Could not find Python executable"), err=True)
        return

    try:
        venv_path = os.path.join(project_path, "venv")
        subprocess.run([python_executable, "-m", "venv", venv_path], check=True)
        click.echo("✓ Virtual environment created successfully")
    except Exception as e:
        click.echo(error_text(f"❌ Error creating virtual environment: {e}"), err=True)
        return

    # Create project structure
    click.echo("\n✓ Creating project files...")
    files = {
        'requirements.txt': '''# Core dependencies
python-dotenv>=1.0.0
pyyaml>=6.0
click>=8.0.0
''',
        '.env': f'''# Environment variables
DEBUG=True
APP_NAME={name}
''',
        'app.py': f'''"""
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
    }

    for file_name, content in files.items():
        full_path = os.path.join(project_path, file_name)
        click.echo(f"📄 Creating {file_name}")
        with open(full_path, 'w') as f:
            f.write(content)

    click.echo("\n✨ Project structure created successfully!")
    click.echo(f"\nTo start working on your project:")
    click.echo(command_text(f"cd {name}"))
    click.echo(command_text("source venv/bin/activate  # On Unix/MacOS"))
    click.echo(command_text("venv\\Scripts\\activate    # On Windows"))
    click.echo(command_text("pip install -r requirements.txt"))
    click.echo(command_text("aske init    # To initialize git and create .gitignore"))

@main.command()
def activate():
    """Activate the Python virtual environment"""
    click.echo("\n🚀 Activating virtual environment...")
    click.echo("=" * 50)

    # Check if we're in a project directory
    venv_path = os.path.join(os.getcwd(), "venv")
    if not os.path.exists(venv_path):
        click.echo(error_text("❌ Error: No virtual environment found in current directory"), err=True)
        click.echo(error_text("Make sure you're in a project directory created with 'aske python <name>'"), err=True)
        return

    # Get the activation script path based on platform
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        activate_cmd = activate_script
    else:  # Unix/MacOS
        activate_script = os.path.join(venv_path, "bin", "activate")
        activate_cmd = f"source {activate_script}"

    # Print the command that needs to be evaluated by the shell
    click.echo(command_text(activate_cmd))
    

@main.command()
def init():
    """Initialize git repository with .gitignore"""
    click.echo("\n🚀 Initializing git repository...")
    
    # Check if git is already initialized
    if os.path.exists('.git'):
        click.echo(error_text("❌ Git repository already exists in this directory"), err=True)
        return

    try:
        # Initialize git repository
        subprocess.run(['git', 'init'], check=True)
        click.echo(success_text("✓ Git repository initialized"))

        # Create or update .gitignore
        click.echo("📄 Creating/updating .gitignore file...")
        with open('.gitignore', 'w') as f:
            f.write(GitignoreModel.get_python_gitignore())
        click.echo(success_text("✓ Created/updated .gitignore file"))

        # Add files to git
        subprocess.run(['git', 'add', '.gitignore'], check=True)
        click.echo(success_text("✓ Added .gitignore to git"))
        
        click.echo("\n✨ Git repository initialized successfully!")
        click.echo("\nNext steps:")
        click.echo(command_text("git add ."))
        click.echo(command_text("git commit -m 'Initial commit'"))

    except subprocess.CalledProcessError as e:
        click.echo(error_text(f"❌ Error initializing git repository: {e}"), err=True)
        return
    except Exception as e:
        click.echo(error_text(f"❌ Unexpected error: {e}"), err=True)
        return

@main.command()
@click.argument('name')
def node(name):
    """Create a new Node.js project and set up its structure"""
    project_path = os.path.abspath(name)
    
    # Check if project already exists
    if os.path.exists(project_path):
        click.echo(error_text(f"❌ Error: Project directory '{name}' already exists"), err=True)
        click.echo(error_text("Please choose a different name or remove the existing directory"), err=True)
        sys.exit(1)
    
    # Check if nvm is installed by looking for .nvm directory
    home = os.path.expanduser("~")
    nvm_dir = os.path.join(home, ".nvm")
    if not os.path.exists(nvm_dir):
        click.echo(error_text("\n❌ NVM (Node Version Manager) is not installed or not found!"))
        click.echo("\nPlease install NVM first:")
        click.echo(command_text("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"))
        click.echo("\nThen restart your terminal and run:")
        click.echo(command_text("nvm install node  # Install latest Node.js version"))
        return

    # Check if yarn is installed
    try:
        subprocess.run(['yarn', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        click.echo(error_text("\n❌ Yarn package manager is not installed!"))
        click.echo("\nPlease install Yarn first:")
        click.echo(command_text("npm install -g yarn  # Install Yarn globally"))
        click.echo("\nOr if you prefer Homebrew:")
        click.echo(command_text("brew install yarn"))
        return

    click.echo(f"\n🚀 Creating new Node.js project: {name}")
    click.echo("=" * 50)

    # Create project directory and structure
    os.makedirs(project_path)
    for dir_name in ['src/controllers', 'src/models', 'src/routes', 'src/middlewares', 'tests']:
        os.makedirs(os.path.join(project_path, dir_name))

    # Create project files
    files = {
        'package.json': NodejsModel.get_package_json(name),
        '.prettierrc': NodejsModel.get_prettierrc(),
        '.eslintrc': NodejsModel.get_eslintrc(),
        'src/index.js': NodejsModel.get_index_js(),
        '.env': NodejsModel.get_env()
    }

    for file_path, content in files.items():
        full_path = os.path.join(project_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
            click.echo(f"📄 Created {file_path}")

    click.echo("\n✨ Project structure created successfully!")
    click.echo("\nNext steps:")
    click.echo(command_text(f"cd {name}"))
    click.echo(command_text("yarn install  # Install dependencies"))
    click.echo(command_text("yarn dev      # Start development server"))
    click.echo(command_text("aske init     # Initialize git repository"))

@main.command()
@click.argument('name')
def next(name):
    """Create a new Next.js project with TypeScript"""
    project_path = os.path.abspath(name)
    
    # Check if project already exists
    if os.path.exists(project_path):
        click.echo(error_text(f"❌ Error: Project directory '{name}' already exists"), err=True)
        click.echo(error_text("Please choose a different name or remove the existing directory"), err=True)
        sys.exit(1)
    
    # Check if nvm is installed
    home = os.path.expanduser("~")
    nvm_dir = os.path.join(home, ".nvm")
    if not os.path.exists(nvm_dir):
        click.echo(error_text("\n❌ NVM (Node Version Manager) is not installed or not found!"))
        click.echo("\nPlease install NVM first:")
        click.echo(command_text("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash"))
        click.echo("\nThen restart your terminal and run:")
        click.echo(command_text("nvm install node  # Install latest Node.js version"))
        return

    # Check if yarn is installed
    try:
        subprocess.run(['yarn', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        click.echo(error_text("\n❌ Yarn package manager is not installed!"))
        click.echo("\nPlease install Yarn first:")
        click.echo(command_text("npm install -g yarn  # Install Yarn globally"))
        click.echo("\nOr if you prefer Homebrew:")
        click.echo(command_text("brew install yarn"))
        return

    click.echo(f"\n🚀 Creating new Next.js project: {name}")
    click.echo("=" * 50)

    try:
        # Create Next.js project with TypeScript
        click.echo("\n📦 Creating Next.js project with TypeScript...")
        subprocess.run([
            'npx', 
            'create-next-app@latest', 
            name, 
            '--typescript', 
            '--use-yarn',
            '--no-git',  # Don't initialize git - we'll use aske init
            '--src-dir',  # Use src directory structure
            '--import-alias', '@/*'  # Modern import alias
        ], check=True)

        # Wait a moment for file system to sync
        time.sleep(1)

        # Create ModelPrompt component
        component_path = os.path.join(project_path, 'src/components/ModelPrompt.tsx')
        os.makedirs(os.path.dirname(component_path), exist_ok=True)
        with open(component_path, 'w') as f:
            f.write(NextjsModel.get_model_prompt_component())
        click.echo("✓ Created ModelPrompt component")

        # Update index page - check both possible locations
        index_paths = [
            os.path.join(project_path, 'src/app/page.tsx'),  # New app directory
            os.path.join(project_path, 'src/pages/index.tsx')  # Traditional pages directory
        ]
        
        index_path = None
        for path in index_paths:
            if os.path.exists(os.path.dirname(path)):
                index_path = path
                break

        if index_path:
            with open(index_path, 'w') as f:
                f.write(NextjsModel.get_index_page())
            click.echo(f"✓ Updated index page at {os.path.relpath(index_path, project_path)}")
        else:
            click.echo(error_text("❌ Could not find index page location"))

        click.echo("\n✨ Next.js project created successfully!")
        click.echo("\nNext steps:")
        click.echo(command_text(f"cd {name}"))
        click.echo(command_text("yarn install     # Install dependencies"))
        click.echo(command_text("yarn dev        # Start development server"))
        click.echo(command_text("aske init       # Initialize git repository"))

    except subprocess.CalledProcessError as e:
        click.echo(error_text(f"\n❌ Error creating Next.js project: {e}"), err=True)
        return
    except Exception as e:
        click.echo(error_text(f"\n❌ Unexpected error: {e}"), err=True)
        return

if __name__ == '__main__':
    main()

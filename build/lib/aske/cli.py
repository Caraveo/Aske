import click
import os
import subprocess
import sys
import shutil
from aske import __version__

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
    
    click.echo(f"\n🚀 Creating new Python project: {name}")
    click.echo("=" * 50)

    # Create project directory
    click.echo(f"📁 Creating project directory: {project_path}")
    os.makedirs(project_path, exist_ok=True)
    
    # Change to project directory
    click.echo(f"📍 Changing to project directory")
    if not change_directory(project_path):
        return

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
        click.echo("❌ Error: Could not find Python executable", err=True)
        return

    try:
        subprocess.run([python_executable, "-m", "venv", "venv"], check=True)
        click.echo("✓ Virtual environment created successfully")
    except Exception as e:
        click.echo(f"❌ Error creating virtual environment: {e}", err=True)
        return

    # Create project structure
    click.echo("\n📝 Creating project files...")
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
''',
        '.gitignore': '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.env

# IDE
.vscode/
.idea/
*.swp
'''
    }

    for file_name, content in files.items():
        click.echo(f"📄 Creating {file_name}")
        with open(file_name, 'w') as f:
            f.write(content)

    click.echo("\n✨ Project structure created successfully!")
    click.echo("\nNext steps:")
    click.echo("1. Run 'aske init' to initialize git and install dependencies")
    click.echo("2. Run 'aske activate' to activate the virtual environment")

    # Create a file to store the project path
    project_config = os.path.expanduser('~/.aske_project')
    with open(project_config, 'w') as f:
        f.write(project_path)

@main.command()
def init():
    """Initialize git repository and install dependencies"""
    # Try to read last project path
    project_config = os.path.expanduser('~/.aske_project')
    if os.path.exists(project_config):
        with open(project_config, 'r') as f:
            project_path = f.read().strip()
            if project_path and os.path.exists(project_path):
                click.echo(f"📍 Changing to project directory: {project_path}")
                if not change_directory(project_path):
                    return

    click.echo("\n🚀 Initializing project...")
    click.echo("=" * 50)

    # Check if we're in a project directory
    if not os.path.exists('requirements.txt'):
        click.echo("❌ Error: No requirements.txt found. Are you in a project directory?", err=True)
        return

    # Initialize git repository
    click.echo("\n📦 Initializing git repository...")
    try:
        subprocess.run(["git", "init"], check=True)
        click.echo("✓ Git repository initialized")
    except subprocess.CalledProcessError:
        click.echo("⚠️  Warning: Could not initialize git repository", err=True)

    # Install dependencies
    click.echo("\n📥 Installing project dependencies...")
    try:
        if os.name == 'nt':  # Windows
            pip_path = os.path.join("venv", "Scripts", "pip")
        else:  # Unix/MacOS
            pip_path = os.path.join("venv", "bin", "pip")
        
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        click.echo("✓ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Error installing dependencies: {e}", err=True)
        return

    click.echo("\n✨ Project initialized successfully!")
    click.echo("\nNext step:")
    click.echo("Run 'aske activate' to activate the virtual environment")

@main.command()
def activate():
    """Activate the Python virtual environment"""
    # Try to read last project path
    project_config = os.path.expanduser('~/.aske_project')
    if os.path.exists(project_config):
        with open(project_config, 'r') as f:
            project_path = f.read().strip()
            if project_path and os.path.exists(project_path):
                click.echo(f"📍 Changing to project directory: {project_path}")
                if not change_directory(project_path):
                    return

    click.echo("\n🚀 Activating virtual environment...")
    click.echo("=" * 50)

    # Check if we're in a project directory
    venv_path = os.path.join(os.getcwd(), "venv")
    if not os.path.exists(venv_path):
        click.echo("❌ Error: No virtual environment found in current directory", err=True)
        click.echo("Make sure you're in a project directory created with 'aske python <name>'", err=True)
        return

    click.echo("🔍 Detecting platform and locating activation script...")
    
    # Get the activation script path based on platform
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, "Scripts", "activate.bat")
        activate_cmd = activate_script
    else:  # Unix/MacOS
        activate_script = os.path.join(venv_path, "bin", "activate")
        activate_cmd = f"source {activate_script}"

    click.echo(f"✓ Found activation script: {activate_script}")
    click.echo("\n🔄 Activating environment...")
    
    # Print the command that needs to be evaluated by the shell
    click.echo(activate_cmd)
    sys.exit(0)  # Clean exit for shell evaluation

def _change_to_project_dir():
    """Helper function to change to the project directory"""
    project_config = os.path.expanduser('~/.aske_project')
    if not os.path.exists(project_config):
        click.echo("❌ No project directory found. Create a project first with 'aske python <name>'", err=True)
        return

    with open(project_config, 'r') as f:
        project_path = f.read().strip()
        if not project_path or not os.path.exists(project_path):
            click.echo("❌ Last project directory not found", err=True)
            return

        click.echo(f"cd {project_path}")
        sys.exit(0)  # Clean exit for shell evaluation

@main.command('cd')
def change_dir():
    """Change to the last used project directory"""
    _change_to_project_dir()

@main.command('ld')
def last_dir():
    """Change to the last used project directory (alias for cd)"""
    _change_to_project_dir()

if __name__ == '__main__':
    main()

"""PostgreSQL database initialization model"""

class PostgreSQLModel:
    """Model for PostgreSQL database setup and configuration"""

    @staticmethod
    def get_install_commands():
        """Get PostgreSQL installation commands"""
        return [
            "brew install postgresql@14",
            "brew services start postgresql@14",
            "createdb $(whoami)"  # Create default database
        ]

    @staticmethod
    def get_lima_config():
        """Get Lima configuration for PostgreSQL"""
        return '''
# PostgreSQL Lima configuration
arch: "host"
images:
- location: "https://cloud-images.ubuntu.com/releases/22.04/release/ubuntu-22.04-server-cloudimg-arm64.img"
  arch: "aarch64"
mounts:
- location: "~"
  writable: true
- location: "/tmp/lima"
  writable: true
containerd:
  system: false
  user: false
provision:
- mode: system
  script: |
    #!/bin/bash
    apt-get update
    apt-get install -y postgresql postgresql-contrib
    systemctl enable postgresql
    systemctl start postgresql
'''

    @staticmethod
    def get_post_install_instructions():
        """Get post-installation instructions"""
        return '''
# PostgreSQL Post-Installation Steps

1. Create a new database:
createdb your_database

2. Create a new user:
createuser -P your_user
psql -d your_database -c "GRANT ALL PRIVILEGES ON DATABASE your_database TO your_user;"

3. Access the database:
psql your_database

4. Common commands:
\\l - List databases
\\du - List users
\\dt - List tables
\\q - Quit

5. Start/Stop PostgreSQL:
brew services start postgresql@14
brew services stop postgresql@14
'''

    @staticmethod
    def get_lima_instructions():
        """Get Lima-specific instructions"""
        return '''
# PostgreSQL in Lima Container

1. Start the container:
limactl start postgres

2. Enter the container:
limactl shell postgres

3. Access PostgreSQL:
sudo -u postgres psql

4. Stop the container:
limactl stop postgres
''' 
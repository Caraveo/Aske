"""MongoDB database initialization model"""

class MongoDBModel:
    """Model for MongoDB database setup and configuration"""

    @staticmethod
    def get_install_commands():
        """Get MongoDB installation commands"""
        return [
            "brew tap mongodb/brew",
            "brew install mongodb-community@7.0",
            "brew services start mongodb-community@7.0"
        ]

    @staticmethod
    def get_lima_config():
        """Get Lima configuration for MongoDB"""
        return '''
# MongoDB Lima configuration
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
    apt-get install -y mongodb
    systemctl enable mongodb
    systemctl start mongodb
'''

    @staticmethod
    def get_post_install_instructions():
        """Get post-installation instructions"""
        return '''
# MongoDB Post-Installation Steps

1. Start MongoDB shell:
mongosh

2. Create a new database:
use your_database

3. Create a new user:
db.createUser({
  user: "your_user",
  pwd: "your_password",
  roles: ["readWrite", "dbAdmin"]
})

4. Common commands:
show dbs - List databases
show collections - List collections
db.help() - Show help

5. Start/Stop MongoDB:
brew services start mongodb-community@7.0
brew services stop mongodb-community@7.0
'''

    @staticmethod
    def get_lima_instructions():
        """Get Lima-specific instructions"""
        return '''
# MongoDB in Lima Container

1. Start the container:
limactl start mongodb

2. Enter the container:
limactl shell mongodb

3. Access MongoDB:
mongosh

4. Stop the container:
limactl stop mongodb
''' 
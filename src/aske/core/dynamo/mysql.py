"""MySQL database initialization model"""

class MySQLModel:
    """Model for MySQL database setup and configuration"""

    @staticmethod
    def get_install_commands():
        """Get MySQL installation commands"""
        return [
            "brew install mysql",
            "brew services start mysql",
            "mysql_secure_installation"  # Interactive security script
        ]

    @staticmethod
    def get_lima_config():
        """Get Lima configuration for MySQL"""
        return '''
# MySQL Lima configuration
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
    apt-get install -y mysql-server
    systemctl enable mysql
    systemctl start mysql
    # Configure MySQL to listen on all interfaces
    sed -i 's/bind-address.*/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf
    systemctl restart mysql
portForwards:
- guestPort: 3306
  hostPort: 3306
'''

    @staticmethod
    def get_post_install_instructions():
        """Get post-installation instructions"""
        return '''
# MySQL Post-Installation Steps

1. Set root password:
mysql_secure_installation

2. Create a new database:
mysql -u root -p
CREATE DATABASE your_database;

3. Create a new user:
CREATE USER 'your_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;

4. Test connection:
mysql -u your_user -p your_database

5. Start/Stop MySQL:
brew services start mysql
brew services stop mysql
'''

    @staticmethod
    def get_lima_instructions():
        """Get Lima-specific instructions"""
        return '''
# MySQL in Lima Container

1. Start the container:
limactl start mysql

2. Enter the container:
limactl shell mysql

3. Access MySQL:
sudo mysql -u root

4. Stop the container:
limactl stop mysql
''' 
class LaravelModel:
    """Model for generating Laravel project structure and files"""

    @staticmethod
    def get_composer_json(name):
        """Generate composer.json content"""
        return f'''{{
    "name": "aske/{name}",
    "type": "project",
    "description": "A Laravel project created with ASKE",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {{
        "php": "^8.2",
        "laravel/framework": "^10.0",
        "laravel/sanctum": "^3.3",
        "laravel/tinker": "^2.8"
    }},
    "require-dev": {{
        "fakerphp/faker": "^1.9.1",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.1",
        "spatie/laravel-ignition": "^2.0"
    }},
    "autoload": {{
        "psr-4": {{
            "App\\\\": "app/",
            "Database\\\\Factories\\\\": "database/factories/",
            "Database\\\\Seeders\\\\": "database/seeders/"
        }}
    }},
    "autoload-dev": {{
        "psr-4": {{
            "Tests\\\\": "tests/"
        }}
    }},
    "scripts": {{
        "post-autoload-dump": [
            "Illuminate\\\\Foundation\\\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \\"file_exists('.env') || copy('.env.example', '.env');\\"",
            "@php artisan key:generate --ansi"
        ]
    }},
    "extra": {{
        "laravel": {{
            "dont-discover": []
        }}
    }},
    "config": {{
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {{
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }}
    }},
    "minimum-stability": "stable",
    "prefer-stable": true
}}'''

    @staticmethod
    def get_env():
        """Generate .env content"""
        return '''APP_NAME=Laravel
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost

LOG_CHANNEL=stack
LOG_DEPRECATIONS_CHANNEL=null
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
FILESYSTEM_DISK=local
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailpit
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS="hello@example.com"
MAIL_FROM_NAME="${APP_NAME}"'''

    @staticmethod
    def get_hello_controller():
        """Generate HelloController class"""
        return '''<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HelloController extends Controller
{
    public function index()
    {
        return 'Hello, World!';
    }
}
'''

    @staticmethod
    def get_hello_test():
        """Generate HelloController test"""
        return '''<?php

namespace Tests\Feature;

use Tests\TestCase;

class HelloControllerTest extends TestCase
{
    public function test_hello_endpoint_returns_hello_world()
    {
        $response = $this->get('/hello');

        $response->assertStatus(200);
        $response->assertSeeText('Hello, World!');
    }
}
'''

    @staticmethod
    def get_phpunit_xml():
        """Generate phpunit.xml content"""
        return '''<?xml version="1.0" encoding="UTF-8"?>
<phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="vendor/phpunit/phpunit/phpunit.xsd"
         bootstrap="vendor/autoload.php"
         colors="true"
>
    <testsuites>
        <testsuite name="Unit">
            <directory>tests/Unit</directory>
        </testsuite>
        <testsuite name="Feature">
            <directory>tests/Feature</directory>
        </testsuite>
    </testsuites>
    <source>
        <include>
            <directory>app</directory>
        </include>
    </source>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="BCRYPT_ROUNDS" value="4"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="DB_DATABASE" value="testing"/>
        <env name="MAIL_MAILER" value="array"/>
        <env name="QUEUE_CONNECTION" value="sync"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="TELESCOPE_ENABLED" value="false"/>
    </php>
</phpunit>
'''

    @staticmethod
    def get_php_gitignore():
        """Get standard Laravel .gitignore content"""
        return '''/.phpunit.cache
/node_modules
/public/build
/public/hot
/public/storage
/storage/*.key
/vendor
.env
.env.backup
.env.production
.phpunit.result.cache
Homestead.json
Homestead.yaml
auth.json
npm-debug.log
yarn-error.log
/.fleet
/.idea
/.vscode

# Laravel specific
/bootstrap/cache/*
/storage/framework/cache/*
/storage/framework/sessions/*
/storage/framework/views/*
/storage/logs/*

# macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Composer
composer.phar
/vendor/

# PHP CS Fixer
.php_cs
.php_cs.cache
.php-cs-fixer.cache

# PHPStorm
.idea/
*.iml
*.iws

# VS Code
.vscode/
*.code-workspace

# Logs and databases
*.log
*.sqlite
'''

    @staticmethod
    def get_readme(name):
        """Generate README.md content"""
        return f'''# {name}

A Laravel application created with ASKE.

## Requirements

- PHP 8.2+
- Composer
- MySQL/MariaDB
- Node.js & NPM (for frontend assets)

## Setup

1. Ensure PHP is installed:
```bash
# Check PHP version
php -v

# Install PHP if needed
brew install php@8.2
```

2. Install dependencies:
```bash
composer install
npm install
```

3. Set up environment:
```bash
cp .env.example .env
php artisan key:generate
```

4. Run migrations:
```bash
php artisan migrate
```

5. Start the development server:
```bash
php artisan serve
```

6. Visit the hello endpoint:
```
http://localhost:8000/hello
```

## Development

- Controllers are in `app/Http/Controllers`
- Routes are in `routes/web.php` and `routes/api.php`
- Views are in `resources/views`
- Tests are in `tests` directory

## Testing

Run tests with:
```bash
php artisan test
```

## Code Style

Fix code style with Laravel Pint:
```bash
./vendor/bin/pint
```
''' 
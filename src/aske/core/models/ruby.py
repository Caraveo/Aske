class RubyModel:
    """Model for generating Ruby on Rails project structure and files"""

    @staticmethod
    def get_gemfile():
        """Generate Gemfile content"""
        return '''source "https://rubygems.org"
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby "3.2.0"

# Rails version
gem "rails", "~> 7.1.0"

# Use PostgreSQL as the database
gem "pg"

# Use Puma as the app server
gem "puma"

# Boot large ruby/rails apps faster
gem "bootsnap", require: false

# API gems
gem "jbuilder"
gem "rack-cors"

# Authentication & Authorization
gem "devise"
gem "pundit"

# Environment variables
gem "dotenv-rails"

# Monitoring & Logging
gem "newrelic_rpm"
gem "lograge"

# Testing
group :development, :test do
  gem "rspec-rails"
  gem "factory_bot_rails"
  gem "faker"
  gem "pry-byebug"
end

# Development tools
group :development do
  gem "rubocop", require: false
  gem "rubocop-rails", require: false
  gem "brakeman", require: false
  gem "annotate"
  gem "letter_opener"
end
'''

    @staticmethod
    def get_rubocop():
        """Generate .rubocop.yml content"""
        return '''AllCops:
  NewCops: enable
  Exclude:
    - "db/**/*"
    - "bin/**/*"
    - "config/**/*"
    - "Guardfile"
    - "Rakefile"
    - "node_modules/**/*"

Documentation:
  Enabled: false

Style/FrozenStringLiteralComment:
  Enabled: false

Style/ClassAndModuleChildren:
  Enabled: false

Style/SafeNavigation:
  Enabled: false

Metrics/ClassLength:
  Max: 150

Metrics/ModuleLength:
  Max: 150

Metrics/MethodLength:
  Max: 20

Metrics/AbcSize:
  Max: 50
'''

    @staticmethod
    def get_rspec():
        """Generate .rspec content"""
        return '''--require spec_helper
--format documentation
--color
'''

    @staticmethod
    def get_env():
        """Generate .env content"""
        return '''# Database configuration
DATABASE_URL=postgres://localhost/myapp_development

# Rails configuration
RAILS_ENV=development
RAILS_MAX_THREADS=5

# App configuration
APP_HOST=localhost:3000

# Secrets
SECRET_KEY_BASE=development_secret

# Third-party services
# STRIPE_API_KEY=
# AWS_ACCESS_KEY_ID=
# AWS_SECRET_ACCESS_KEY=
'''

    @staticmethod
    def get_readme(name):
        """Generate README.md content"""
        return f'''# {name}

## Requirements

- rbenv (Ruby Version Manager)
- Ruby 3.2.0+ (installed via rbenv)
- Rails 7.1.0+
- PostgreSQL 13+

## Setup

1. Ensure rbenv and Ruby are properly set up:
```bash
# Install rbenv if not installed
brew install rbenv ruby-build

# Add to your shell
eval "$(rbenv init -)"

# Install Ruby
rbenv install 3.2.0
rbenv global 3.2.0

# Install Rails
gem install rails -v 7.1.0
rbenv rehash  # Make Rails executable available
```

2. Install dependencies:
```bash
bundle install
```

3. Setup database:
```bash
rails db:create db:migrate
```

4. Start the server:
```bash
rails server
```

## Testing

Run the test suite:
```bash
bundle exec rspec
```

## Code Quality

Run the linters:
```bash
bundle exec rubocop
bundle exec brakeman
```

## API Documentation

API documentation is available at `/api/docs` when running in development mode.

## Deployment

This application is configured for deployment on Heroku or similar platforms.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
'''

    @staticmethod
    def get_application_rb(name):
        """Generate config/application.rb content"""
        module_name = ''.join(word.capitalize() for word in name.split('-'))
        return f'''require_relative "boot"

require "rails"
require "active_model/railtie"
require "active_job/railtie"
require "active_record/railtie"
require "active_storage/engine"
require "action_controller/railtie"
require "action_mailer/railtie"
require "action_view/railtie"
require "rails/test_unit/railtie"

module {module_name}
  class Application < Rails::Application
    config.load_defaults 7.1

    # Only loads a smaller set of middleware suitable for API only apps.
    config.api_only = true
  end
end
''' 
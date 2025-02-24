"""Go project initialization models"""
import os

class GoModel:
    """Base model for pure Go projects"""

    @staticmethod
    def create_project_structure(path):
        """Create the standard Go project directory structure"""
        directories = [
            'cmd',
            'internal',
            'pkg',
            'api',
            'web',
            'configs',
            'test',
            'docs',
            'scripts',
            'build',
            'deployments',
            'bin'
        ]
        
        for dir in directories:
            os.makedirs(os.path.join(path, dir), exist_ok=True)

        # Create cmd/main directory
        os.makedirs(os.path.join(path, 'cmd', 'main'), exist_ok=True)

        # Create README files for each directory
        for dir in directories:
            readme_path = os.path.join(path, dir, 'README.md')
            with open(readme_path, 'w') as f:
                f.write(f'# {dir}\n\nThis directory contains {dir}-specific code and resources.\n')

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content"""
        return f'''module {name}

go 1.21

require (
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content"""
        return '''package main

import (
    "fmt"
    "log"
    "net/http"
    "os"

    "github.com/joho/godotenv"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }

    // Routes
    http.HandleFunc("/ping", handlePing)
    http.HandleFunc("/api/health", handleHealth)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Server starting on port %s", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}

func handlePing(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, `{"message": "pong"}`)
}

func handleHealth(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    fmt.Fprintf(w, `{"status": "ok"}`)
}
'''

    @staticmethod
    def get_env():
        """Generate .env content"""
        return '''# Server Configuration
PORT=8080
ENV=development

# Add your environment variables here
'''

    @staticmethod
    def get_gitignore():
        """Generate .gitignore content"""
        return '''# Binaries
*.exe
*.exe~
*.dll
*.so
*.dylib
bin/

# Test binary, built with go test -c
*.test

# Output of the go coverage tool
*.out

# Dependency directories
vendor/

# Environment variables
.env
.env.*

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# OS specific files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
'''

    @staticmethod
    def get_readme(name):
        """Generate README.md content"""
        return f'''# {name}

A Go web application using the standard library.

## Project Structure

```
.
├── api/        # API related code
├── cmd/        # Main applications
├── configs/    # Configuration files
├── docs/       # Documentation
├── internal/   # Private application code
├── pkg/        # Public library code
├── scripts/    # Scripts for development
└── test/       # Additional test files
```

## Getting Started

1. Install dependencies:
   ```bash
   go mod download
   go mod tidy
   ```

2. Run the application:
   ```bash
   go run cmd/main/main.go
   ```

3. Build the application:
   ```bash
   make build
   ```

4. Run tests:
   ```bash
   make test
   ```

## Development

- Use `go fmt` to format code
- Run `golangci-lint run` before commits
- Write tests for new features
- Update documentation as needed

## License

MIT
'''

    @staticmethod
    def get_makefile():
        """Generate Makefile content"""
        return '''# Go parameters
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
GOMOD=$(GOCMD) mod
BINARY_NAME=app
BINARY_UNIX=$(BINARY_NAME)_unix

all: test build

build:
	$(GOBUILD) -o bin/$(BINARY_NAME) -v cmd/main/main.go

test:
	$(GOTEST) -v ./...

clean:
	$(GOCLEAN)
	rm -f bin/$(BINARY_NAME)
	rm -f bin/$(BINARY_UNIX)

run:
	$(GOBUILD) -o bin/$(BINARY_NAME) -v cmd/main/main.go
	./bin/$(BINARY_NAME)

deps:
	$(GOMOD) download

tidy:
	$(GOMOD) tidy
''' 
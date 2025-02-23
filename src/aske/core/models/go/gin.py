"""Gin framework model for Go projects"""
import os

class GinModel:
    """Model for generating Gin framework projects"""

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
        """Generate go.mod content for Gin"""
        return f'''module {name}

go 1.21

require (
    github.com/gin-gonic/gin v1.9.1
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Gin"""
        return '''package main

import (
    "log"
    "os"

    "github.com/gin-gonic/gin"
    "github.com/joho/godotenv"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }

    r := gin.Default()

    // Routes
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })

    // API routes
    api := r.Group("/api")
    {
        api.GET("/health", func(c *gin.Context) {
            c.JSON(200, gin.H{
                "status": "ok",
            })
        })
    }

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    r.Run(":" + port)
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

A Go web application using the Gin framework.

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

    @staticmethod
    def get_handler_example():
        """Generate example handler"""
        return '''package handlers

import "github.com/gin-gonic/gin"

// HealthCheck handles the health check endpoint
func HealthCheck(c *gin.Context) {
    c.JSON(200, gin.H{
        "status": "ok",
        "message": "Service is healthy",
    })
}
'''

    @staticmethod
    def get_test_example():
        """Generate example test"""
        return '''package handlers

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/gin-gonic/gin"
    "github.com/stretchr/testify/assert"
)

func TestHealthCheck(t *testing.T) {
    // Switch to test mode
    gin.SetMode(gin.TestMode)

    // Setup router
    r := gin.Default()
    r.GET("/health", HealthCheck)

    // Create request
    w := httptest.NewRecorder()
    req, _ := http.NewRequest("GET", "/health", nil)

    // Serve request
    r.ServeHTTP(w, req)

    assert.Equal(t, 200, w.Code)
    assert.Contains(t, w.Body.String(), "healthy")
}
'''

    @staticmethod
    def get_middleware_example():
        """Generate example middleware"""
        return '''package middleware

import (
    "github.com/gin-gonic/gin"
    "time"
)

// Logger middleware logs request details
func Logger() gin.HandlerFunc {
    return func(c *gin.Context) {
        t := time.Now()

        // Process request
        c.Next()

        // Log details
        latency := time.Since(t)
        status := c.Writer.Status()
        
        log.Printf("[%d] %s %s - %v", status, c.Request.Method, c.Request.URL.Path, latency)
    }
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Gin-specific post-creation instructions"""
        return '''
🚀 Gin Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP request handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions
   - config/: Configuration

2. Key Commands:
   go run cmd/main/main.go  # Start server
   go test ./...           # Run tests
   go build               # Build binary

3. Common Patterns:
   - Use gin.Context for request/response
   - Group related routes
   - Implement middleware
   - Use binding for request validation

4. Best Practices:
   - Organize routes logically
   - Use middleware for common functionality
   - Handle errors consistently
   - Write tests for handlers

5. Documentation:
   - Gin Guide: https://gin-gonic.com/docs/
   - Examples: https://github.com/gin-gonic/examples
   - API Reference: https://godoc.org/github.com/gin-gonic/gin

6. Development Tools:
   - air: Live reload (go install github.com/cosmtrek/air@latest)
   - swag: API documentation (go install github.com/swaggo/swag/cmd/swag@latest)
''' 
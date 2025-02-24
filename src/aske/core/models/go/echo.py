"""Echo framework model for Go projects"""
from .gin import GinModel  # Inherit common methods

class EchoModel(GinModel):
    """Model for generating Echo framework projects"""

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Echo"""
        return f'''module {name}

go 1.21

require (
    github.com/labstack/echo/v4 v4.11.3
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Echo"""
        return '''package main

import (
    "log"
    "os"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
    "github.com/joho/godotenv"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }

    e := echo.New()

    // Middleware
    e.Use(middleware.Logger())
    e.Use(middleware.Recover())
    e.Use(middleware.CORS())

    // Routes
    e.GET("/", func(c echo.Context) error {
        return c.JSON(200, map[string]string{
            "message": "Welcome to Echo!",
        })
    })

    e.GET("/hello", func(c echo.Context) error {
        return c.JSON(200, map[string]string{
            "message": "Hello, World!",
        })
    })

    e.GET("/ping", func(c echo.Context) error {
        return c.JSON(200, map[string]string{
            "message": "pong",
        })
    })

    e.GET("/api/health", func(c echo.Context) error {
        return c.JSON(200, map[string]string{
            "status": "ok",
        })
    })

    // Get port from environment
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Server starting on port %s", port)
    e.Logger.Fatal(e.Start(":" + port))
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Echo-specific post-creation instructions"""
        return '''
🚀 Echo Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions

2. Key Features:
   - High performance
   - Minimalist design
   - Built-in middleware
   - Extensible architecture

3. Best Practices:
   - Use proper error handling
   - Group related routes
   - Implement middleware
   - Use Echo's context

4. Documentation:
   - Echo Guide: https://echo.labstack.com
   - API Reference: https://pkg.go.dev/github.com/labstack/echo/v4

5. Development Tools:
   - go run: Live development
   - go test: Run tests
   - go build: Build for production
''' 
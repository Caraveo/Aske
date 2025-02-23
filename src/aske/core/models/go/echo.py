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
    e.GET("/ping", func(c echo.Context) error {
        return c.JSON(200, map[string]string{
            "message": "pong",
        })
    })

    // API routes
    api := e.Group("/api")
    api.GET("/health", HealthCheck)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    e.Logger.Fatal(e.Start(":" + port))
}

func HealthCheck(c echo.Context) error {
    return c.JSON(200, map[string]string{
        "status": "ok",
    })
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Echo-specific post-creation instructions"""
        return '''
🚀 Echo Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP request handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions

2. Key Features:
   - Minimalist and fast
   - Built-in middleware
   - Automatic TLS
   - WebSocket support

3. Best Practices:
   - Use Context for request handling
   - Implement custom middleware
   - Group related routes
   - Use echo.Binder for validation

4. Documentation:
   - Echo Guide: https://echo.labstack.com/guide
   - API Reference: https://pkg.go.dev/github.com/labstack/echo/v4

5. Development Tools:
   - air: Live reload
   - echogen: Code generator
''' 
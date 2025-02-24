"""Fiber framework model for Go projects"""
from .gin import GinModel

class FiberModel(GinModel):
    """Model for generating Fiber framework projects"""

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Fiber"""
        return f'''module {name}

go 1.21

require (
    github.com/gofiber/fiber/v2 v2.52.0
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Fiber"""
        return '''package main

import (
    "log"
    "os"

    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/fiber/v2/middleware/cors"
    "github.com/gofiber/fiber/v2/middleware/logger"
    "github.com/joho/godotenv"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }

    app := fiber.New(fiber.Config{
        AppName: "Fiber App",
    })

    // Middleware
    app.Use(logger.New())
    app.Use(cors.New())

    // Routes
    app.Get("/", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{
            "message": "Welcome to Fiber!",
        })
    })

    app.Get("/hello", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{
            "message": "Hello, World!",
        })
    })

    app.Get("/ping", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{
            "message": "pong",
        })
    })

    app.Get("/api/health", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{
            "status": "ok",
        })
    })

    // Get port from environment
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Server starting on port %s", port)
    log.Fatal(app.Listen(":" + port))
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Fiber-specific post-creation instructions"""
        return '''
🚀 Fiber Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions

2. Key Features:
   - Express-style routing
   - Built-in middleware
   - Zero memory allocation
   - Fast HTTP implementation

3. Best Practices:
   - Use proper error handling
   - Group related routes
   - Implement middleware
   - Use Fiber's context

4. Documentation:
   - Fiber Guide: https://docs.gofiber.io
   - API Reference: https://pkg.go.dev/github.com/gofiber/fiber/v2

5. Development Tools:
   - go run: Live development
   - go test: Run tests
   - go build: Build for production
''' 
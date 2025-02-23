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
    github.com/gofiber/fiber/v2 v2.51.0
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
    app.Get("/ping", func(c *fiber.Ctx) error {
        return c.JSON(fiber.Map{
            "message": "pong",
        })
    })

    // API routes
    api := app.Group("/api")
    api.Get("/health", HealthCheck)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Fatal(app.Listen(":" + port))
}

func HealthCheck(c *fiber.Ctx) error {
    return c.JSON(fiber.Map{
        "status": "ok",
    })
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Fiber-specific post-creation instructions"""
        return '''
🚀 Fiber Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP request handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions

2. Key Features:
   - Express.js inspired
   - Zero memory allocation
   - Fast HTTP routing
   - WebSocket support

3. Best Practices:
   - Use fiber.Map for JSON responses
   - Implement custom middleware
   - Group related routes
   - Use fiber.Config for settings

4. Documentation:
   - Fiber Guide: https://docs.gofiber.io
   - API Reference: https://pkg.go.dev/github.com/gofiber/fiber/v2

5. Development Tools:
   - air: Live reload
   - swagger: API documentation
''' 
"""Chi framework model for Go projects"""
from .gin import GinModel

class ChiModel(GinModel):
    """Model for generating Chi framework projects"""

    @staticmethod
    def get_mod_file(name):
        """Generate go.mod content for Chi"""
        return f'''module {name}

go 1.21

require (
    github.com/go-chi/chi/v5 v5.0.12
    github.com/go-chi/cors v1.2.1
    github.com/joho/godotenv v1.5.1
)
'''

    @staticmethod
    def get_main_file():
        """Generate main.go content for Chi"""
        return '''package main

import (
    "encoding/json"
    "log"
    "net/http"
    "os"

    "github.com/go-chi/chi/v5"
    "github.com/go-chi/chi/v5/middleware"
    "github.com/go-chi/cors"
    "github.com/joho/godotenv"
)

func main() {
    if err := godotenv.Load(); err != nil {
        log.Printf("Warning: .env file not found")
    }

    r := chi.NewRouter()

    // Middleware
    r.Use(middleware.Logger)
    r.Use(middleware.Recoverer)
    r.Use(cors.Handler(cors.Options{
        AllowedOrigins:   []string{"*"},
        AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowedHeaders:   []string{"Accept", "Authorization", "Content-Type"},
        ExposedHeaders:   []string{"Link"},
        AllowCredentials: true,
        MaxAge:           300,
    }))

    // Routes
    r.Get("/", func(w http.ResponseWriter, r *http.Request) {
        json.NewEncoder(w).Encode(map[string]string{
            "message": "Welcome to Chi!",
        })
    })

    r.Get("/ping", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]string{
            "message": "pong",
        })
    })

    r.Get("/api/health", func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(map[string]string{
            "status": "ok",
        })
    })

    // Get port from environment
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Server starting on port %s", port)
    log.Fatal(http.ListenAndServe(":"+port, r))
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Chi-specific post-creation instructions"""
        return '''
🚀 Chi Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP handlers
   - middleware/: Custom middleware
   - models/: Data models
   - services/: Business logic

2. Key Features:
   - Lightweight and fast
   - Middleware support
   - URL pattern routing
   - Composable handlers

3. Best Practices:
   - Use middleware for common tasks
   - Group related routes
   - Handle errors properly
   - Use context for request scoping

4. Documentation:
   - Chi Guide: https://go-chi.io
   - API Reference: https://pkg.go.dev/github.com/go-chi/chi/v5

5. Development Tools:
   - go run: Live development
   - go test: Run tests
   - go build: Build for production
''' 
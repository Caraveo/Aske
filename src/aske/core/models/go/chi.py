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
    github.com/go-chi/chi/v5 v5.0.10
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
        AllowedOrigins: []string{"*"},
        AllowedMethods: []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowedHeaders: []string{"Accept", "Authorization", "Content-Type"},
        MaxAge:         300,
    }))

    // Routes
    r.Get("/ping", func(w http.ResponseWriter, r *http.Request) {
        json.NewEncoder(w).Encode(map[string]string{
            "message": "pong",
        })
    })

    // API routes
    r.Route("/api", func(r chi.Router) {
        r.Get("/health", HealthCheck)
    })

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Server starting on port %s", port)
    log.Fatal(http.ListenAndServe(":"+port, r))
}

func HealthCheck(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(map[string]string{
        "status": "ok",
    })
}
'''

    @staticmethod
    def get_post_create_instructions():
        """Get Chi-specific post-creation instructions"""
        return '''
🚀 Chi Framework Quick Start:

1. Project Structure:
   - handlers/: HTTP request handlers
   - middleware/: Custom middleware
   - models/: Data models
   - routes/: Route definitions

2. Key Features:
   - Lightweight and fast
   - Standard library compatible
   - Middleware support
   - URL pattern routing

3. Best Practices:
   - Use standard http.Handler interface
   - Implement middleware as needed
   - Group related routes
   - Handle errors consistently

4. Documentation:
   - Chi Guide: https://go-chi.io
   - API Reference: https://pkg.go.dev/github.com/go-chi/chi/v5

5. Development Tools:
   - air: Live reload
   - swag: API documentation
   - curl/httpie: API testing
''' 
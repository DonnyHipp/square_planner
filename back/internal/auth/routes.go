package routes

import (
	"back/internal/auth/api/v1"
	"github.com/gin-gonic/gin"
)

type AuthRoutes struct{}

func (a AuthRoutes) RegisterRoutes(router *gin.RouterGroup) {
	router.GET("/login", handler.LoginHandler)
	router.GET("/register", handler.RegisterHandler)
}

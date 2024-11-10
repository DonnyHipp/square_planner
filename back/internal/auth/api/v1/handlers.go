package handler

import (
	"github.com/gin-gonic/gin"
)

func LoginHandler(c *gin.Context) {
	c.JSON(200, gin.H{"message": "Успешный вход"})
}

func RegisterHandler(c *gin.Context) {
	c.JSON(200, gin.H{"message": "Успешно зарегано"})
}

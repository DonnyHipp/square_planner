package kpi

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type KpiRoutes struct{}

func (a KpiRoutes) RegisterRoutes(router *gin.RouterGroup) {
	router.GET("/kpi", func(c *gin.Context) {
		// Логика получения KPI
		c.JSON(http.StatusOK, gin.H{"kpi": "some KPI data"})
	})
}

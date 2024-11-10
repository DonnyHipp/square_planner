package routes

import (
	authRoutes "back/internal/auth"
	rt "back/pkg/router"
	"github.com/gin-gonic/gin"
)

func RegisterAllRoutes(router *gin.Engine) {
	routerGroup := router.Group("/v1")
	rt.RegisterRouter(routerGroup, "/auth", authRoutes.AuthRoutes{})
	//rt.RegisterRouter(routerGroup, "kpi", kpiRoutes.KpiRoutes{})
}

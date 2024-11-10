package router

import "github.com/gin-gonic/gin"

type RouteRegistrar interface {
	RegisterRoutes(router *gin.RouterGroup)
}

func RegisterRouter(router *gin.RouterGroup, prefix string, registrar RouteRegistrar) {
	prefixedRouter := router.Group(prefix)
	registrar.RegisterRoutes(prefixedRouter)
}

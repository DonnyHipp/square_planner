package main

import (
	"back/internal"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	routes.RegisterAllRoutes(r)

	if err := r.Run(":8080"); err != nil {
		panic(err)
	}

}

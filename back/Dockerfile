# Этап сборки
FROM golang:1.21 as builder

# Установим рабочую директорию
WORKDIR /app

# Копируем go.mod и go.sum для кэширования зависимостей
COPY go.mod go.sum ./
RUN go mod download

# Копируем остальные файлы
COPY . .

# Собираем приложение
RUN go build -v -o start_backend ./cmd/main.go

CMD ["./start_backend"]

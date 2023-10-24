variable "function_name" {
    type = string
    description = "Nome lambda"
}

variable "handler" {
    type = string
    description = "Nome do handler da lambda"
    default = "function.lambda_handler"
}

variable "runtime" {
    type = string
    description = "Runtime lambda"
    default = "python3.9"
}
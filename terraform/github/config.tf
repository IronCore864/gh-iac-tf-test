terraform {
  required_version = ">= 1.5.2"

  required_providers {
    github = {
      source  = "integrations/github"
      version = "5.30.1"
    }
  }
}

provider "github" {
  owner = "ironcoreworks"

  app_auth {
    id              = var.app_id
    installation_id = var.app_installation_id
    pem_file        = file(var.app_pem_file)
  }
}

terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}

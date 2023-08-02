resource "github_team" "test_team_1_by_terraform" {
  name        = "Test Team 1 by Terraform"
  description = "The Test Team 1, managed by Terraform"
  privacy     = "closed"
}

resource "github_team_membership" "test_team_1_by_terraform_IronCore864" {
  team_id  = github_team.test_team_1_by_terraform.id
  username = "IronCore864"
  role     = "maintainer"
}
resource "github_team" "test_team_2_by_terraform" {
  name        = "Test Team 2 by Terraform"
  description = "The Test Team 2, managed by Terraform"
  privacy     = "closed"
}

resource "github_team_membership" "test_team_2_by_terraform_IronCore864" {
  team_id  = github_team.test_team_2_by_terraform.id
  username = "IronCore864"
  role     = "maintainer"
}

resource "github_team" "test_team_3_by_terraform" {
  name           = "Test Team 3 by Terraform"
  description    = "The Test Team 3, managed by Terraform"
  parent_team_id = github_team.test_team_2_by_terraform.id
  privacy        = "closed"
}

resource "github_team_membership" "test_team_3_by_terraform_IronCore864" {
  team_id  = github_team.test_team_3_by_terraform.id
  username = "IronCore864"
  role     = "maintainer"
}

resource "github_team" "test_team_4_by_terraform" {
  name           = "Test Team 4 by Terraform"
  description    = "The Test Team 4, managed by Terraform"
  parent_team_id = github_team.test_team_3_by_terraform.id
  privacy        = "closed"
}

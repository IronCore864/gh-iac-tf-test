resource "github_team" "{resource_name}" {{
  name           = "{team_name}"
  description    = "{team_desc}"
  parent_team_id = github_team.{parent}.id
  privacy        = "closed"
}}


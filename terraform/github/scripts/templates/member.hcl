resource "github_team_membership" "{team_name}_{member_name}" {{
  team_id  = github_team.{team_name}.id
  username = "{member_name}"
  role     = "{role}"
}}


import os
import yaml


def read_template(file_path):
    # Helper function to read HCL template from file
    with open(file_path, "r") as f:
        return f.read()

def ensure_single_newline(string):
    """
    Ensure that a multiline string has only one new line at the end.
    
    Args:
        string (str): The input string.
        
    Returns:
        str: The modified string.
    """
    # Strip all trailing whitespace, including newlines
    stripped = string.rstrip()
    
    # Add a single newline at the end
    modified = stripped + "\n"
    
    # Return the modified string
    return modified

def generate_team_resource(team, parent):
    res = ""

    resource_name = team["name"].lower().replace(" ", "_")

    if parent:
        # Use child template if team has a parent
        tpl = read_template("templates/team-child.hcl")
        res = tpl.format(
            resource_name=resource_name,
            team_name=team["name"],
            team_desc=team["description"],
            parent=parent,
        )
    else:
        # Use parent template if team has no parent
        tpl = read_template("templates/team-parent.hcl")
        res = tpl.format(
            resource_name=resource_name,
            team_name=team["name"],
            team_desc=team["description"],
        )

    return res


def generate_member_resources(team):
    res = ""

    # Read HCL templates from files
    tpl = read_template("templates/member.hcl")

    team_name = team["name"].lower().replace(" ", "_")

    members = team.get("members", [])
    for member in members:
        role = member.get("role", "member")
        res += tpl.format(
            team_name=team_name,
            member_name=member["username"],
            role=role,
        )

    return res


def generate_hcl(team, parent=None):
    # Generate HCL code for teams
    hcl = generate_team_resource(team, parent)

    # Generate HCL code for team members
    hcl += generate_member_resources(team)

    # Recursively generate HCL code for subteams
    parent_team_name = team["name"].lower().replace(" ", "_")

    subteams = team.get("teams", [])
    for subteam in subteams:
        hcl += generate_hcl(subteam, parent_team_name)

    return hcl


def main():
    config_dir = "../../../github/"
    for root, _, files in os.walk(config_dir):
        for file in files:
            file_path = os.path.join(root, file)

            # Load YAML
            with open(file_path, "r") as f:
                data = yaml.safe_load(f)

            if not data:
                continue

            # Start generating HCL
            hcl = ""
            for team in data["teams"]:
                hcl += generate_hcl(team)

            # Write HCL to file
            parent_folder_name = os.path.basename(
                os.path.dirname(os.path.abspath(file_path))
            )
            base_name = os.path.splitext(file)[0]
            output_file = f"{parent_folder_name}-{base_name}.tf"
            with open(f"../{output_file}", "w") as f:
                f.write(ensure_single_newline(hcl))


if __name__ == "__main__":
    main()

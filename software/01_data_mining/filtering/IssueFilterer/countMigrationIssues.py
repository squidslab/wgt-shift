import json
import os

def count_issues(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        total_issues = 0
        total_open = 0
        total_closed = 0
        repo_count = len(data)
        
        for repo, repo_data in data.items():
            # In migration_issues_filtered.json, repo_data is a list of migration events
            if isinstance(repo_data, list):
                for migration_event in repo_data:
                    if 'issues' in migration_event:
                        issues = migration_event['issues']
                        
                        open_count = len(issues.get('open', []))
                        closed_count = len(issues.get('closed', []))
                        
                        total_open += open_count
                        total_closed += closed_count
                        total_issues += (open_count + closed_count)
            elif isinstance(repo_data, dict) and 'issues' in repo_data:
                issues = repo_data['issues']
                
                open_count = len(issues.get('open', []))
                closed_count = len(issues.get('closed', []))
                
                total_open += open_count
                total_closed += closed_count
                total_issues += (open_count + closed_count)
                
        print(f"File: {os.path.basename(file_path)}")
        print(f"Total Repositories: {repo_count}")
        print(f"Total Issues: {total_issues}")
        print(f"  - Open Issues: {total_open}")
        print(f"  - Closed Issues: {total_closed}")
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the migration_issues_filtered.json file
    # Assuming the script is run from the root of the workspace or its current directory
    
    # Try to find the file relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    workspace_root = os.path.abspath(os.path.join(script_dir, '..', '..', '..', '..'))
    file_path = os.path.join(workspace_root, 'resources', 'migration_issues_filtered.json')
    
    # If not found, try relative to current working directory
    if not os.path.exists(file_path):
        file_path = os.path.join('resources', 'migration_issues_filtered.json')
        
    count_issues(file_path)

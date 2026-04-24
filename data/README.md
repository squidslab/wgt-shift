# Data

This folder contains all the data used in the study.

1. Data imported from the original E2EGit Dataset:
    * **[`creation-adoption-gui.xlsx`](./creation-adoption-gui.xlsx)**: Contains the list of adoption events of web GUI testing frameworks.
    * **[`migration_analysis.xlsx`](./migration_analysis.xlsx)**: Contains the list of migration events of web GUI testing frameworks.

2. Mined data
    * **[`adoption_commits.json`](./adoption_commits.json)**: Raw list of commits identified by our heuristics as potential framework adoptions.
    * **[`migration_commits.json`](./migration_commits.json)**: Raw list of commits identified as potential migrations between frameworks.
    * **[`issues_summary_repos_lower_than_30.xlsx`](./issues_summary_repos_lower_than_30.xlsx)**: Summary of issues for repositories with fewer than 30 issues (the others were imported from E2EGit). The list of all issues is omitted, but can be retrieved using the scripts in the **[`software/`](./software/)** folder.

3. Filtered data and manual review results
    * **[`adoption_commits_filtered.json`](./adoption_commits_filtered.json)**, **[`migration_commits_filtered.json`](./migration_commits_filtered.json)**, **[`adoption_issues_filtered.json`](./adoption_issues_filtered.json)**, **[`migration_issues_filtered.json`](./migration_issues_filtered.json)**: List of adoption/migration commits/issues after filtering.
    * **[`adoption_commits_summary.json`](./adoption_commits_summary.json)**, **[`migration_commits_summary.json`](./migration_commits_summary.json)**, **[`adoption_issues_summary.json`](./adoption_issues_summary.json)**, **[`migration_issues_summary.json`](./migration_issues_summary.json)**: Summary of the adoption and migration commits/issues retrieved for each keyword.
    * **[`issues_missed_in_filter.json`](./issues_missed_in_filter.json)**: List of issues that were missed by the filtering process but were identified as relevant during manual review.

4. Manual labelling
    * **[`adoption_commits_filtered.xlsx`](./adoption_commits_filtered.xlsx)**, **[`migration_commits_filtered.xlsx`](./migration_commits_filtered.xlsx)**, **[`adoption_issues_filtered.xlsx`](./adoption_issues_filtered.xlsx)**, **[`migration_issues_filtered.xlsx`](./migration_issues_filtered.xlsx)**: List of adoption/migration commits/issues classified during manual review as useful or not useful.
    * **[`issues_missed_in_filter.xlsx`](./issues_missed_in_filter.xlsx)**: List of issues that were missed by the filtering process classified as useful or not useful during manual review.

5. Manual review results
    * **[`taxonomy.xlsx`](./taxonomy.xlsx)**: Contains the final socio-technical taxonomy of motivations derived from the study.
    * **[`events.xlsx`](./events.xlsx)**, **[`transitions.csv`](./transitions.csv)**: Both files contain the adoption and migration events, linking to their commit/issue and the corresponding motivation category. The latter provides also a plain text summary of each event.

6. Additional data
    * **[`taxonomy_report.xlsx`](./taxonomy_report.xlsx)**: For each motivation category provides the number of adoption/migration issues/commits associated with it.
    * **[`mapping.xlsx`](./mapping.xlsx)**: Mapping between each issue/commit to the corresponding motivation category.
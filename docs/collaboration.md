# Collaboration

This guide provides instructions for general collaboration across the entire project, as well as specific setup and contribution details for those working on the project documentation.

## General Collaboration Guidelines

The HelMoRo project welcomes contributions in various forms: bug fixes, feature additions, and documentation improvements. Here’s how you can contribute across any part of the project.

### 1. Report or Identify Issues

Start by identifying or reporting issues. Describe the problem or suggest enhancements comprehensively.

- **Repository issues page:** [HelMoRo issues](https://github.com/orgs/Helbling-Technik/projects/1/views/1)
- **Feature Bucket:** Select from existing tasks on our GitHub projects page: [Feature Bucket](https://github.com/orgs/Helbling-Technik/projects/1)

### 2. Clone the Repository

For direct contributions, clone the repository using SSH (recommended):

```bash
git clone git@github.com:Helbling-Technik/HelMoRo.git
```

If you prefer you can also fork it and then work on your own fork.
### 3. Create a Branch

Create a new branch in your cloned repository for the specific issue you are addressing:

```bash
git checkout -b issue-number-description
```

### 4. Make Changes

Implement your fixes or enhancements within your branch. Keep your branch updated to avoid conflicts:

```bash
git fetch origin
git rebase origin/master
```

### 5. Commit and Push Changes

Commit your changes with clear, descriptive commit messages:

```bash
git add .
git commit -m "Detailed description of your changes"
git push origin issue-number-description
```

### 6. Submit a Pull Request

After pushing your changes, submit a pull request (PR) through GitHub, linking it back to the issue it resolves.

### 7. Participate in the Review Process

Engage with the project maintainers during the PR review process and address any feedback  to facilitate the integration of your contributions.

### 8. Stay Involved

Continue contributing by addressing more issues, reviewing others' contributions, and participating in project discussions.


## Contribution to Documentation

Before you start contributing to the documentation, you need to set up MkDocs, which is used to build and manage the project documentation. 
You can find all the Information in the [README.md](README.md)


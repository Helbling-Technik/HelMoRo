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


## Setting Up Your Environment for Documentation
### Installation

Before you start contributing to the documentation, you need to set up MkDocs, which is used to build and manage the project documentation.

MkDocs documentation cna be found [here](https://www.mkdocs.org/user-guide/), but below is a Quick-start guide from us.

**Install MkDocs:**

```bash
pip install mkdocs
```

Ensure that MkDocs is added to your system's environment variables post-installation. On Windows, access this setting through:

- *Advanced System Settings* → *System Properties* → *Environment Variables*

Find the `Path` variable under *System Variables* and verify that it includes the directory containing the MkDocs executable. Add it if necessary.

**Additional Packages:**

For enhanced documentation features, install the following packages:

- **MkDocs Table Reader Plugin:**

  ```bash
  pip install mkdocs-table-reader-plugin
  ```

- **Markdown Include:**

  ```bash
  pip install markdown-include
  ```

- **MkDocs Material:**

  ```bash
  pip install mkdocs-material
  ```

### Run Website Locally

To see how the documentation looks while you work on it, you can run a local server:

```bash
mkdocs serve -a localhost:8888
```

Make sure the specified port (8888) is available. The website will be accessible at [http://localhost:8888](http://localhost:8888).
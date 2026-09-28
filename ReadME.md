# Git Student Management Project

## Project Overview

This is a small Python Student Management project created to demonstrate how to manage a Python project using Git and GitHub.

The main purpose of this project is to understand Git version control, including creating a repository, tracking changes, creating branches, merging branches, and working with a remote GitHub repository.

---

## Technologies Used

* Python
* Git
* GitHub

---

## Project Structure

```text
git-student-project/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
└── .env
```

> `.env` is used only locally and is not committed to GitHub.

---

## Application Features

The Student Management project supports:

* Adding students
* Displaying students
* Searching for students
* Validating student names
* Preventing duplicate students

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/git-student-project.git
```

### 2. Move into the project folder

```bash
cd git-student-project
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Run the application

```bash
python app.py
```

---

# Git Commands Demonstrated

This project demonstrates the following Git commands:

```text
git init
git status
git add
git commit
git log
git branch
git switch
git diff
git remote
git push
git pull
```

---

## 1. git init

The `git init` command initializes a new Git repository in the project folder.

```bash
git init
```

This creates a hidden `.git` directory that stores Git's version-control information.

---

## 2. git status

The `git status` command shows the current state of the Git repository.

```bash
git status
```

It can show:

* Untracked files
* Modified files
* Staged files
* The current branch

---

## 3. git add

The `git add` command moves changes from the working directory to the staging area.

Example:

```bash
git add app.py
```

To add multiple project files:

```bash
git add README.md .gitignore requirements.txt app.py
```

---

## 4. git commit

The `git commit` command permanently records staged changes in the Git repository.

Example:

```bash
git commit -m "Initial student management project"
```

Meaningful commits were created during this project to maintain a clear project history.

---

## 5. git log

The `git log` command displays the commit history.

```bash
git log
```

A shorter version can be viewed using:

```bash
git log --oneline
```

The project contains at least five meaningful commits.

Example commit history:

```text
Initial student management project
Add student search functionality
Add student name validation
Add project documentation
Prevent duplicate students
```

---

## 6. git branch

The `git branch` command displays the available branches.

```bash
git branch
```

The project uses the following branches:

```text
main
feature-student-search
feature-student-validation
```

---

## 7. git switch

The `git switch` command is used to change branches.

Create and switch to a new branch:

```bash
git switch -c feature-student-search
```

Switch back to the main branch:

```bash
git switch main
```

Switch to another existing branch:

```bash
git switch feature-student-validation
```

---

## 8. git diff

The `git diff` command displays changes that have been made but have not yet been committed.

```bash
git diff
```

It helps identify exactly what was changed in the files.

---

# Branching and Merging

Two feature branches were created for this project.

## Branch 1: Student Search

```bash
git switch -c feature-student-search
```

A student search functionality was added on this branch.

The changes were committed using:

```bash
git add app.py
git commit -m "Add student search functionality"
```

---

## Branch 2: Student Validation

A second branch was created:

```bash
git switch main
git switch -c feature-student-validation
```

Student-name validation and duplicate checking were added on this branch.

The changes were committed using:

```bash
git add app.py
git commit -m "Add student name validation"
```

Another commit was created for duplicate checking:

```bash
git add app.py
git commit -m "Prevent duplicate students"
```

---

## Merging Branches

After completing the feature work, the branches were merged into `main`.

First, switch to the main branch:

```bash
git switch main
```

Merge the student-search branch:

```bash
git merge feature-student-search
```

Merge the validation branch:

```bash
git merge feature-student-validation
```

The final `main` branch contains the functionality from both feature branches.

---

# GitHub Remote Repository

The local Git repository was connected to GitHub using:

```bash
git remote add origin https://github.com/YOUR_USERNAME/git-student-project.git
```

The configured remote can be checked using:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/YOUR_USERNAME/git-student-project.git (fetch)
origin  https://github.com/YOUR_USERNAME/git-student-project.git (push)
```

---

# Pushing Changes to GitHub

The local `main` branch was pushed to GitHub using:

```bash
git push -u origin main
```

This uploads the local commits to the GitHub remote repository.

---

# Pulling Changes from GitHub

Changes made on GitHub can be downloaded and merged into the local repository using:

```bash
git pull origin main
```

This keeps the local repository synchronized with the remote GitHub repository.

---

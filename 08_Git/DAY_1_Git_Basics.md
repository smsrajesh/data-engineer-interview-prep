# Git Day 1 — Git Basics

## 1. What is Git?

Git is a **distributed version control system (DVCS)** used to track changes made to files over time.

Git allows us to:

- Track changes
- Maintain a history of changes
- Revert to previous versions
- Work with branches
- Collaborate with other developers
- Manage different versions of a project

---

## 2. Git Repository :

A **Git repository** is a directory where Git tracks and stores the history of a project.

When we run:

    ```bash
    git init
    ```

Git creates a hidden `.git` directory.

    ```text
    project/
    │
    ├── .git/
    ├── README.md
    └── other_files
    ```

The `.git` directory contains the information Git needs to manage the repository and its history.

---

# 3. `git init` :

## Meaning

`git init` initializes a Git repository in the current directory.

### Syntax

    ```bash
    git init
    ```

### Example

    ```bash
    mkdir git-practice
    cd git-practice

    git init
    ```

Git will create the `.git` directory.

### Important

`git init` **does not commit or stage files**.

It simply initializes the directory as a Git repository.

---

# 4. Git Working Areas :

Git has three important areas:

    ```text
    Working Directory
        ↓
    Staging Area
        ↓
    Repository
    ```

### Working Directory

The **Working Directory** is where we create and modify files.

Example:

    ```text
    README.md
    SQL/
    Python/
    ```

When we modify a file, the change exists in the Working Directory.

### Staging Area

The **Staging Area** contains changes that we have selected for the next commit.

We move changes into the Staging Area using:

    ```bash
    git add
    ```

### Repository

The **Repository** contains the committed history of the project.

We record staged changes in the repository using:

    ```bash
    git commit
    ```

---

# 5. Basic Git Workflow :

The fundamental Git workflow is:

    ```text
    Create / Modify File
            ↓
    Working Directory
            ↓
        git add
            ↓
    Staging Area
            ↓
        git commit
            ↓
    Repository
    ```

Example:

    ```bash
    # Check current state
    git status

    # Stage a file
    git add README.md

    # Commit the staged change
    git commit -m "Add initial README"
    ```

---

# 6. `git status` :

## Meaning

`git status` shows the **current state of the Git repository**.

### Syntax

    ```bash
    git status
    ```

It can show:

- Current branch
- Untracked files
- Modified files
- Staged changes
- Changes that are ready to be committed
- Whether the working tree is clean

### Example

    ```bash
    git status
    ```

Output:

    ```text
    On branch main
    nothing to commit, working tree clean
    ```

### Meaning

    ```text
    On branch main
    ```

    We are currently working on the `main` branch.

    ```text
    nothing to commit
    ```

    There are no changes waiting to be committed.

    ```text
    working tree clean
    ```

    There are no uncommitted changes in the Working Directory.

---

# 7. Untracked Files :

An **untracked file** is a file that exists in the Working Directory but Git is not currently tracking.

Example:

    ```text
    README.md
    ```

After creating the file:

    ```bash
    git status
    ```

Git may show:

    ```text
    Untracked files:

        README.md
    ```

At this point:

    ```text
    README.md
        ↓
    Working Directory
        ↓
    Untracked
    ```

We can stage the file using:

    ```bash
    git add README.md
    ```

---

# 8. `git add` :

## Meaning

`git add` moves selected changes from the **Working Directory to the Staging Area**.

### Syntax

    ```bash
    git add filename
    ```

Example:

    ```bash
    git add README.md
    ```

After running it:

    ```text
    Working Directory
        ↓
    git add
        ↓
    Staging Area
    ```

Git may then show:

    ```text
    Changes to be committed:
        new file: README.md
    ```

### Important

`git add` **does not create a commit**.

    It only prepares the selected changes for the next commit.

## Adding Multiple Files

    ```bash
    git add file1.py file2.py
    ```

## Adding All Changes

    ```bash
    git add .
    ```

This stages all changes in the current directory.

---

# 9. `git commit` :

## Meaning

`git commit` records the changes currently present in the **Staging Area** into the local Git Repository.

### Syntax

    ```bash
    git commit -m "commit message"
    ```

Example:

    ```bash
    git commit -m "Add initial README"
    ```

Workflow:

    ```text
    Staging Area
        ↓
    git commit
        ↓
    Repository
    ```

### Commit Message

The commit message should clearly describe the change.

Good:

    ```bash
    git commit -m "Add initial README"
    git commit -m "Add employee SQL practice"
    ```

Poor:

    ```bash
    git commit -m "changes"
    git commit -m "update"
    ```

---

# 10. `git log` :

## Meaning

`git log` displays the **commit history** of the repository.

### Syntax

    ```bash
    git log
    ```

Example:

    ```text
    commit d918e080edcb18f79cdbb9548aad9e1ae8352c70 (HEAD -> main)
    Author: smsrajesh
    Date:   Mon Aug 17 13:13:32 2026 +0530

        Add initial README
    ```

## Understanding `git log`

### Commit ID

    ```text
    d918e080edcb18f79cdbb9548aad9e1ae8352c70
    ```

    A commit has a unique identifier.

### Author

    ```text
    Author: smsrajesh
    ```

    The person who created the commit.

### Date

    Shows when the commit was created.

### Commit Message

    ```text
    Add initial README
    ```

    Describes what was changed.

---

# 11. `HEAD` :

Example:

    ```text
    (HEAD -> main)
    ```

For now, understand `HEAD` as a reference to the commit we are currently working from.

We will learn `HEAD` in more detail when we cover:

- Branching
- Reset
- Revert
- Reflog

---

# 12. Complete Practical Example :

Start with an empty directory:

    ```bash
    mkdir git-practice
    cd git-practice
    ```

Initialize Git:

    ```bash
    git init
    ```

Create:

    ```text
    README.md
    ```

    Check status:

        ```bash
        git status
        ```

    Git identifies `README.md` as an untracked file.

Stage the file:

    ```bash
    git add README.md
    ```

    Check status again:

        ```bash
        git status
        ```

    Now Git shows:

        ```text
        Changes to be committed:
            new file: README.md
        ```

Commit:

    ```bash
    git commit -m "Add initial README"
    ```

    Check status:

        ```bash
        git status
        ```

    Expected:

    ```text
    On branch main
    nothing to commit, working tree clean
    ```

Check history:

    ```bash
    git log
    ```

---

# 13. Important Git Commands — Day 1 :

| Command                       | Purpose                            |
|-------------------------------|------------------------------------|
| `git init`                    | Initialize a Git repository        |
| `git status`                  | Check repository status            |
| `git add <file>`              | Stage a specific file              |
| `git add .`                   | Stage all changes                  |
| `git commit -m "message"`     | Commit staged changes              |
| `git log`                     | View commit history                |

---

# 14. Interview Questions :

### Q1. What is Git?

> Git is a distributed version control system used to track changes in files and maintain the history of a project.

### Q2. What does `git init` do?

> `git init` initializes a Git repository in the current directory by creating the `.git` directory.

### Q3. What does `git status` do?

> `git status` shows the current state of the Git repository, including untracked, modified, and staged files.

### Q4. What is an untracked file?

> An untracked file is a file present in the Working Directory that Git is not currently tracking.

### Q5. What does `git add` do?

> `git add` moves selected changes from the Working Directory to the Staging Area.

### Q6. What does `git commit` do?

> `git commit` records the staged changes into the local Git Repository.

### Q7. What does `git log` do?

> `git log` displays the commit history of the repository.

### Q8. What is the difference between `git add` and `git commit`?

> `git add` moves changes from the Working Directory to the Staging Area, while `git commit` records the staged changes in the local Repository.

---

# 15. Key Concept to Remember :

The most important concept from Day 1:

    ```text
    Working Directory
            │
            │ git add
            ↓
    Staging Area
            │
            │ git commit
            ↓
    Repository
    ```

### In one sentence

> **`git add` prepares changes, while `git commit` records those prepared changes.**

---

# 16. Day 1 Practice Commands :

```bash
git init

git status

git add README.md

git status

git commit -m "Add initial README"

git status

git log
```

**Day 1 completed:** `git init` → `git status` → `git add` → `git commit` → `git log`

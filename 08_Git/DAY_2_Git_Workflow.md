# Git Day 2 — Working Directory, Staging Area & Commit Workflow

## 1. Overview

Git tracks changes through three main areas:

    ```text
    Working Directory
        |
        | git add
        v
    Staging Area
        |
        | git commit
        v
    Local Repository
    ```

The basic workflow practiced in Day 2 is:

    ```text
    Modify file
        ↓
    git status
        ↓
    git diff
        ↓
    git add
        ↓
    git diff --staged
        ↓
    git commit
        ↓
    git log
    ```

---

## 2. Git's Three Main Areas

### Working Directory

The Working Directory contains the files you are currently working on.

When you modify a tracked file, Git detects the change, but the change is not yet staged.

Example:

    ```text
    README.md → modified
    ```

Check the state with:

    ```bash
    git status
    ```

---

### Staging Area

The Staging Area contains changes that are prepared for the next commit.

Use:

    ```bash
    git add README.md
    ```

After staging, Git reports:

    ```text
    Changes to be committed:
        modified: README.md
    ```

Important:

> `git add` does NOT create a commit.

It prepares changes to be included in the next commit.

---

### Local Repository

The Local Repository contains committed snapshots of your project.

Create a commit with:

    ```bash
    git commit -m "docs(git): update Day 1 practice notes"
    ```

A commit gets a unique commit ID, for example:

    ```text
    92dcb32
    ```

---

# 3. `git status`

`git status` shows the current state of your repository.

Example when the repository is clean:

    ```text
    On branch main
    nothing to commit, working tree clean
    ```

This means there are no changes in the Working Directory or Staging Area that differ from the latest commit.

If a file is modified but not staged:

    ```text
    Changes not staged for commit:
        modified: README.md
    ```

If a file has been staged:

    ```text
    Changes to be committed:
        modified: README.md
    ```

---

# 4. `git diff`

Use:

    ```bash
    git diff
    ```

to see changes that are in the Working Directory but have not been staged.

Conceptually:

    ```text
    Working Directory
            ↓
        git diff
            ↓
    Compare with Staging Area
    ```

Example:

    ```diff
    +Git Basics - Day 1
    +Day 1 completed.
    ```

### Interview definition

> `git diff` shows unstaged changes in the Working Directory.

---

# 5. `git add`

Use:

    ```bash
    git add README.md
    ```

    to stage a file.

You can also stage all changes:

    ```bash
    git add .
    ```

`git add` can stage:

- New/untracked files
- Modified files
- Deleted files

Important:

> `git add` does not create a commit. It moves changes into the Staging Area.

---

# 6. `git diff --staged`

Use:

    ```bash
    git diff --staged
    ```

    to see changes that are currently staged and are about to be committed.

Conceptually:

    ```text
    Staging Area
        ↓
    git diff --staged
        ↓
    Compare with Last Commit
    ```

### Interview definition

> `git diff --staged` shows changes that have been staged and are ready for the next commit.

---

# 7. `git commit`

Use:

    ```bash
    git commit -m "docs(git): update Day 1 practice notes"
    ```

A commit creates a permanent snapshot in the Local Repository.

Example output:

    ```text
    [main 92dcb32] docs(git): update Day 1 practice notes
    1 file changed, 3 insertions(+), 1 deletion(-)
    ```

Important distinction:

    ```text
    git add
    → Stage changes

    git commit
    → Save staged changes as a commit
    ```

---

# 8. `git log --oneline -5`

Use:

    ```bash
    git log --oneline -5
    ```

    to view the **5 most recent commits** in a compact, one-line format.

### Breaking down the command

    ```text
    git log
    → Show commit history

    --oneline
    → Display each commit in a compact single-line format

    -5
    → Show the 5 most recent commits
    ```

Therefore:

> **`git log --oneline -5` shows the last 5 commits in a compact, one-line format.**

### Commit order

The output is displayed in **reverse chronological order**:

    ```text
    Newest commit
        ↓
    Older commit
        ↓
    Older commit
        ↓
    Older commit
        ↓
    Oldest of the 5
    ```

The **newest commit appears at the top**, and older commits appear as you move downward.

Example:

    ```text
    92dcb32 (HEAD -> main) docs(git): update Day 1 practice notes
    d918e08 Add initial README
    ```

In this example:

    ```text
    92dcb32 → Newest commit
    d918e08 → Older commit
    ```

If the repository had 10 commits, `-5` would display only the **5 newest commits**.

### What does the output contain?

Each one-line entry typically contains:

    ```text
    Commit Hash + References + Commit Message
    ```

For example:

    ```text
    92dcb32 (HEAD -> main) docs(git): update Day 1 practice notes
    ```

- `92dcb32` → Short commit hash
- `(HEAD -> main)` → Current `HEAD` and branch reference
- `docs(git): update Day 1 practice notes` → Commit message

### Important terminology

Prefer saying:

> **commit history**

rather than:

> commit message history

because `git log` shows more than just commit messages; it also shows commit identifiers and references.

### Understanding `HEAD`

`HEAD` represents your current position in the Git history.

In this example:

    ```text
    HEAD -> main
    ```

means the `main` branch is currently pointing to commit `92dcb32`.

# 9. Complete Practical Workflow

Suppose we modify `README.md`.

### Step 1 — Check status

    ```bash
    git status
    ```

Git reports:

    ```text
    modified: README.md
    ```

### Step 2 — Review unstaged changes

    ```bash
    git diff
    ```

### Step 3 — Stage the change

    ```bash
    git add README.md
    ```

### Step 4 — Check status again

    ```bash
    git status
    ```

Now Git reports:

    ```text
    Changes to be committed:
        modified: README.md
    ```

### Step 5 — Review staged changes

    ```bash
    git diff --staged
    ```

### Step 6 — Commit

    ```bash
    git commit -m "docs(git): update Day 1 practice notes"
    ```

### Step 7 — Verify repository state

    ```bash
    git status
    ```

Expected:

    ```text
    nothing to commit, working tree clean
    ```

### Step 8 — Verify commit history

    ```bash
    git log --oneline -5
    ```

---

# 10. `git diff` vs `git diff --staged`

| Command               | Purpose                |
|-----------------------|------------------------|
| `git diff`            | Shows unstaged changes |
| `git diff --staged`   | Shows staged changes   |
| `git status`          | Shows repository state |
| `git log`             | Shows commit history   |

Easy way to remember:

    ```text
    git diff
    → What have I changed but NOT staged?

    git diff --staged
    → What have I staged and am ABOUT TO commit?
    ```

---

# 11. Important Interview Questions

## Q1. What is the difference between `git add` and `git commit`?

**Answer:**

`git add` stages changes for the next commit.

`git commit` creates a commit from the staged changes and stores that snapshot in the Local Repository.

---

## Q2. What is the difference between `git diff` and `git diff --staged`?

**Answer:**

`git diff` shows unstaged changes in the Working Directory.

`git diff --staged` shows changes that are already staged and are ready to be committed.

---

## Q3. Does `git add` create a commit?

**Answer:**

No.

`git add` only stages changes. A commit is created using `git commit`.

---

## Q4. Can `git add` stage modified files?

**Answer:**

Yes.

`git add` can stage new, modified, and deleted changes.

---

## Q5. What does "working tree clean" mean?

**Answer:**

It means there are no uncommitted changes in the Working Directory or Staging Area compared with the latest commit.

---

## Q6. Why does Git have a Staging Area?

**Answer:**

The Staging Area allows us to selectively choose which changes should be included in the next commit.

For example, if three files are modified, we can stage only one:

    ```bash
    git add file1.py
    ```

and commit only that change.

---

# 12. Key Mental Model

Remember this:

    ```text
    I CHANGE something
            ↓
    Working Directory

    I SELECT what I want to commit
            ↓
    git add
            ↓
    Staging Area

    I SAVE that selected snapshot
            ↓
    git commit
            ↓
    Local Repository

    I CHECK my history
            ↓
    git log
    ```

---

# 13. Day 2 Commands

```bash
git status
git diff
git add <file>
git add .
git diff --staged
git commit -m "message"
git log --oneline -5
```

---

# 14. Interview Cheat Sheet

    ```text
    git status
    → What is the current state?

    git diff
    → What changed but is NOT staged?

    git add
    → Stage the changes I want to commit.

    git diff --staged
    → What staged changes am I about to commit?

    git commit
    → Save the staged snapshot to the Local Repository.

    git log
    → Show commit history.
    ```

---

## Day 2 Summary

The most important concept from Day 2 is:

    ```text
    Working Directory
            ↓
        git add
            ↓
    Staging Area
            ↓
    git commit
            ↓
    Local Repository
    ```

**`git add` = prepare**

**`git commit` = save**

**`git log` = verify history**

# Day 3 — Git Undo & Recovery

## 1. `git restore`

Used to **discard unstaged changes** in a file and restore it to the last committed version.

     ```bash
     git restore <file_name>
     ```

### Example

     ```bash
     git restore DAY_3_Git_Undo.md
     ```

**Meaning:** Discards the changes in the working directory.

> The uncommitted changes will be lost.

---

## 2. `git restore --staged`

Used to **unstage a file** while keeping its changes in the Working Directory.

     ```bash
     git restore --staged <file_name>
     ```

### Example

     ```bash
     git restore --staged DAY_3_Git_Undo.md
     ```

**Meaning:** Removes the file from the Staging Area but keeps the modifications.

### Important Difference

     ```text
     git restore file
     → Discard changes

     git restore --staged file
     → Unstage changes, keep changes
     ```

---

## 3. `git rm`

Used to **delete a file and stage the deletion**.

     ```bash
     git rm <file_name>
     ```

### Example

     ```bash
     git rm old_notes.md
     ```

After this command:

     ```text
     File → Deleted
     Deletion → Staged
     ```

To record the deletion permanently in the repository:

     ```bash
     git commit -m "remove old notes"
     ```

### Important

`git rm` does **not** mean "discard changes."

It means:

> Delete the file and stage that deletion.

---

## 4. Recovering a Deleted File

If a file was deleted using `git rm` but the deletion has **not been committed**, the file can be restored using:

     ```bash
     git restore <file_name>
     ```

### Example

     ```bash
     git rm old_notes.md
     git restore old_notes.md
     ```

The file is restored to its last committed version.

---

## 5. Staging and Unstaging

The Staging Area allows us to decide which changes should be included in the next commit.

### Stage a file

     ```bash
     git add <file_name>
     ```

### Unstage a file

     ```bash
     git restore --staged <file_name>
     ```

### Example

     ```bash
     git add DAY_2_Git_Workflow.md
     git restore --staged DAY_2_Git_Workflow.md
     ```

The file is no longer staged, but its modifications remain in the Working Directory.

---

## 6. Discarding Changes vs Unstaging Changes

This is one of the most important concepts from Day 3.

### Discard changes

     ```bash
     git restore <file_name>
     ```

     ```text
     Modified file
          ↓
     git restore
          ↓
     Last committed version
     ```

The changes are removed.

### Unstage changes

     ```bash
     git restore --staged <file_name>
     ```

     ```text
     Staging Area
          ↓
     git restore --staged
          ↓
     Working Directory
     ```

The changes are kept.

---

## 7. Selective Undo Example

Suppose three files are staged:

     ```text
     file_A.md → staged
     file_B.md → staged
     file_C.md → staged
     ```

Required:

- `file_A.md` → Commit
- `file_B.md` → Keep changes, don't commit
- `file_C.md` → Discard changes

Commands:

     ```bash
     git restore --staged file_B.md
     git restore --staged file_C.md
     git restore file_C.md
     ```

Now:

     ```text
     Staging Area
     └── file_A.md

     Working Directory
     └── file_B.md
     ```

Then commit:

     ```bash
     git commit -m "update file A"
     ```

---

## 8. Git Undo Cheat Sheet

| Situation                   | Command                          | Result                 |
|-----------------------------|----------------------------------|------------------------|
| Discard unstaged changes    | `git restore file`               | Changes are discarded  |
| Unstage a file              | `git restore --staged file`      | Changes are kept       |
| Delete a file               | `git rm file`            | File deleted + deletion staged |
| Recover deleted file before commit | `git restore file`| File restored                  |
| Record deletion             | `git commit -m "message"`| Deletion saved in history      |

---

## 9. Interview Notes

### Q: What does `git restore` do?

It restores a file to a previous state. Commonly, it is used to discard unstaged changes or recover a deleted file before the deletion is committed.

### Q: What does `git restore --staged` do?

It removes changes from the Staging Area while keeping those changes in the Working Directory.

### Q: What is the difference between `git restore` and `git restore --staged`?

     ```text
     git restore file
     → Discard changes

     git restore --staged file
     → Unstage changes but keep them
     ```

### Q: What does `git rm` do?

It deletes a file from the Working Directory and stages the deletion for the next commit.

---

## 10. Key Takeaways

- `git restore file` → **discard changes**
- `git restore --staged file` → **unstage, keep changes**
- `git rm file` → **delete + stage deletion**
- `git commit` → **record staged changes in the repository**
- Always understand whether a change is in the **Working Directory** or **Staging Area** before using an undo command.
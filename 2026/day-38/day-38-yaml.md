# Day 38 – YAML Basics

## Challenge Tasks

### Task 1: Key-Value Pairs
Create `person.yaml` that describes yourself with:
- `name`
- `role`
- `experience_years`
- `learning` (a boolean)

**Verify:** Run `cat person.yaml` — does it look clean? No tabs?

<img width="581" height="292" alt="image" src="https://github.com/user-attachments/assets/ba840a4f-6b47-46c4-b27d-c724dccdedbc" />

---

### Task 2: Lists
Add to `person.yaml`:
- `tools` — a list of 5 DevOps tools you know or are learning
- `hobbies` — a list using the inline format `[item1, item2]`

<img width="620" height="330" alt="image" src="https://github.com/user-attachments/assets/a7c9b023-43bc-4cd5-b953-b6fe2672061b" />

Write in your notes: What are the two ways to write a list in YAML?

1. **Block Format:** Using a hyphen and a space (`- `) on a new line for each item. This is best for readability.

2. **Inline (Flow) Format:** Using square brackets and commas (e.g., `[item1, item2]`). This is best for short, simple lists.

---

### Task 3: Nested Objects
Create `server.yaml` that describes a server:
- `server` with nested keys: `name`, `ip`, `port`
- `database` with nested keys: `host`, `name`, `credentials` (nested further: `user`, `password`)

<img width="642" height="290" alt="image" src="https://github.com/user-attachments/assets/cd49c27c-dfe1-48fa-bf40-40af7214d6df" />

**Verify:** Try adding a tab instead of spaces — what happens when you validate it?

YAML strictly forbids the use of Tabs for indentation. If you use a tab, the YAML parser immediately throws a fatal syntax error (e.g., `found character that cannot start any token`). You **must** use spaces (usually 2 spaces per indentation level).


---

### Task 4: Multi-line Strings
In `server.yaml`, add a `startup_script` field using:
1. The `|` block style (preserves newlines)
2. The `>` fold style (folds into one line)

<img width="615" height="457" alt="image" src="https://github.com/user-attachments/assets/622790af-7f67-4423-b43b-314739f408bd" />

Write in your notes: When would you use `|` vs `>`?

* Use **`|` (Literal Block):** When you want to preserve exact line breaks. It is perfect for writing bash scripts or code blocks where every new line matters.
* Use **`>` (Folded Block):** When you want to write a long paragraph across multiple lines in your editor for readability, but you want the YAML parser to read it as one single continuous line (it turns your newlines into spaces).

---

### Task 5: Validate Your YAML

1. Install `yamllint` or use an online validator
  - `sudo apt update`
  - `sudo apt install`

2. Validate both your YAML files
  - `yamllint person.yaml`
  - `yamllint server.yaml`

3. Intentionally break the indentation — what error do you get?
  - `yamllint person.yaml`
  - <img width="827" height="142" alt="image" src="https://github.com/user-attachments/assets/85cb615f-70af-44c2-b6a6-1656603b1960" />
  
  - `yamllint server.yaml`
  - <img width="821" height="195" alt="image" src="https://github.com/user-attachments/assets/5061f128-4d85-48eb-a098-c9171d63ebaa" />
  

4. Fix it and validate again

  - After resolving the errors
  - <img width="655" height="76" alt="image" src="https://github.com/user-attachments/assets/cff087fb-2746-4f25-937d-4f155f87568c" />
  
  - After resolving the errors
  - <img width="620" height="66" alt="image" src="https://github.com/user-attachments/assets/4a57cccb-7c6d-433e-9579-f729ea261e1a" />

---

### Task 6: Spot the Difference
Read both blocks and write what's wrong with the second one:

```yaml
# Block 1 - correct
name: devops
tools:
  - docker
  - kubernetes
```

```yaml
# Block 2 - broken
name: devops
tools:
- docker
  - kubernetes
```

  - The tools list is incorrectly indented. In YAML, list items must align under the key with consistent spacing.
  - Correct indentation should be:
    ```
    text
    tools:
      - docker
      - kubernetes
    ```

---

## Things I Learned Today

1. _Tabs are the enemy_: YAML files will break instantly if you use a tab for indentation. Configure your code editor to "Insert spaces for tabs" (set to 2 spaces).
2. _No quotes needed for strings_: Unlike JSON, you don't need to wrap strings in "`quotes`" unless they contain special YAML characters like `:` or `#`.
3. _Data Types_: YAML implicitly understands data types. `true` is a boolean, but "`true`" is a string. `10` is an integer, but `10.5` is a float.
4. Use `|` when you want to preserve line breaks exactly.
5. Use `>` when you want YAML to fold lines into one long sentence or paragraph.


---

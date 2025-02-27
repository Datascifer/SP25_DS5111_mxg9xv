# SP25_DS5111_mxg9xv

## Bootstrapping for a New VM
1. Clone this repo.
2. Run `./init.sh` to install make, python3.12-venv, and tree.


```markdown
# LAB-05: GitHub Actions Setup

You'll learn how to set up GitHub Actions to automatically run your tests every time you push changes.
---

## Steps

1. **Create the Workflow Directory and File**  
   First, create a folder in your repository: `.github/workflows`

2. **Set Up the YAML File**  
   Create a file in that folder (for example, `validations.yml`) and add your workflow configuration. (You can choose to set up your Python environment manually if needed.)

3. **Commit and Push**  
   Save your changes, commit them, and push to your branch. Then, go to your GitHub repository and click on the **Actions** tab to watch your workflow run!

4. **Enhance Your Setup**  
   - Add a status badge to your README so you can quickly see if your tests are passing.
   - Update your `requirements.txt` with your current package versions (using `pip freeze`).
   - Consider adding tests that check if your OS is Linux and if the Python version is correct (3.10 or 3.11).

5. **Prepare Your Pull Request**  
   When you're ready, create a pull request with a clear title and description. Let your reviewers know what you've done and how you tested it. For example, you might say:  
   "Set up GitHub Actions to run tests. Verified by triggering the workflow and checking the output logs."

---

**Friendly Reminder:**  
Your workflow will run automatically when you push changes.
```

# Publish to GitHub

Account detected: `harshakavali81-collab`. No new repository was created or pushed from this session because the available GitHub tools do not create repositories.

## Browser upload (no terminal required)
1. Sign in to GitHub and create a repository named `marketing-campaign-roi-analytics`.
2. Choose Public if you want recruiters to view it. Do not initialize a README if using the terminal method below.
3. Extract the project ZIP. Open the `marketing-roi` folder.
4. On the repository page, choose Add file → Upload files. Drag the folder's contents, preserving subfolders, and commit. Do not upload only the ZIP.
5. Confirm the README renders and the dashboard image appears.

## Git terminal method
After creating an empty repository, run from the extracted project folder:
```
git init -b main
git add .
git commit -m "Add marketing ROI analytics portfolio project"
git remote add origin https://github.com/harshakavali81-collab/marketing-campaign-roi-analytics.git
git push -u origin main
```
Use your normal GitHub sign-in flow when prompted. Never put access tokens into source files. If you already initialized a repository or set a remote, inspect `git status` and `git remote -v` first rather than reinitializing blindly.

Description: End-to-end synthetic marketing campaign analytics with Python, SQLite, Excel, an interactive dashboard and Power BI setup assets.
Suggested topics: data-analysis, marketing-analytics, sql, python, power-bi, excel.

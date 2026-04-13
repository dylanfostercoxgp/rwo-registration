# RWO Registration Manager

## Project Overview
Single-file browser-based registration management app for Race World Offshore (RWO). Tracks team registration, crew credentials, and payment status across four races per season.

## Architecture
- **Single file app**: Everything lives in `index.html` (HTML + CSS + JS, no frameworks)
- **Data storage**: `data.json` stored in GitHub repo, read/written via GitHub Contents API
- **Hosting**: GitHub Pages at https://dylanfostercoxgp.github.io/rwo-registration
- **Auth**: Client-side password (`APP_PW`) + GitHub Personal Access Token (`GH_TOKEN`)
- **No build step**: Upload `index.html` to GitHub, Pages serves it automatically
- **PDF export**: html2pdf.js loaded via CDN for individual team PDF downloads

## Key Constants (top of `<script>` block in index.html)
- `GH_OWNER` / `GH_REPO` - GitHub account and repo name
- `GH_TOKEN` - Personal access token for GitHub API (sensitive) - **YOU MUST SET THIS**
- `APP_PW` - Shared password for app access (currently `rwo2026`)
- `CLASSES` - Array of 14 official race classes
- `DEFAULT_RACES` - Array of 4 race objects with id, name, date

## File Structure
- `index.html` - The entire application (CSS + HTML + JS)
- `data.json` - Auto-created JSON database (teams, races, season)
- `HANDOFF.docx` - Full technical handoff document
- `CLAUDE.md` - This file

## Important Rules
- **Race IDs**: `atlanticcity`, `michigancity`, `clearwater`, `keywest` - these are keys in data.json
- **Always update index.html in-place** - do not create separate CSS/JS files
- **GH_TOKEN is sensitive** - it's embedded in the HTML source; GitHub will revoke it if pushed via git
- **To deploy**: manually upload index.html via GitHub web editor (not git push)
- **Print card always renders white** regardless of dark/light mode
- CSS custom properties define the theme (`:root` for dark, `[data-theme="light"]` for light)
- Auto-save triggers 1.5s after last change via `queueSave()`
- `DB.races` is always overwritten with `DEFAULT_RACES` on load (source of truth is the code)

## Deployment (Manual Upload)
1. Edit `index.html` locally
2. Go to github.com/dylanfostercoxgp/rwo-registration
3. Click `index.html` > pencil icon > select all > paste new code > commit
4. GitHub Pages updates within 60-90 seconds
5. Users hard-refresh (Cmd+Shift+R) to get latest version

## GitHub Info
- **Account**: dylanfostercoxgp
- **Repo**: rwo-registration
- **Pages URL**: https://dylanfostercoxgp.github.io/rwo-registration
- **Token management**: https://github.com/settings/tokens

## Season Info (2026)
- Atlantic City: Jun 26-28, 2026
- Michigan City: Jul 31-Aug 2, 2026
- Clearwater: Sep 26-28, 2026
- Key West: Nov 1-8, 2026

## Token Setup
When generating a new token, you MUST manually replace `PASTE_YOUR_NEW_TOKEN_HERE`
in index.html line ~460 before uploading. GitHub auto-revokes tokens it detects
in git pushes, so always upload via the web editor, never git push.

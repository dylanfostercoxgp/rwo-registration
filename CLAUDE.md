# RWO Registration Manager

## Project Overview
Single-file browser-based registration management app for Race World Offshore (RWO). Tracks team registration, crew credentials, and payment status across four races per season.

## Architecture
- **Single file app**: Everything lives in `index.html` (HTML + CSS + JS, no frameworks)
- **Data storage**: `data.json` stored in GitHub repo, read/written via GitHub Contents API
- **Hosting**: GitHub Pages at https://dylanfostercoxgp.github.io/rwo-registration
- **Auth**: Client-side password (`APP_PW`) + GitHub Personal Access Token (`GH_TOKEN`)
- **No build step**: Upload `index.html` to GitHub, Pages serves it automatically

## Key Constants (top of `<script>` block in index.html)
- `GH_OWNER` / `GH_REPO` - GitHub account and repo name
- `GH_TOKEN` - Personal access token for GitHub API (sensitive)
- `APP_PW` - Shared password for app access
- `CLASSES` - Array of 14 official race classes
- `DEFAULT_RACES` - Array of 4 race objects with id, name, date

## File Structure
- `index.html` - The entire application (CSS + HTML + JS)
- `data.json` - Auto-created JSON database (teams, races, season)
- `HANDOFF.docx` - Full technical handoff document
- `CLAUDE.md` - This file

## Important Rules
- **Never change race `id` values** (clearwater, miami, bimini, nassau) - they are keys in data.json
- **Always update index.html in-place** - do not create separate CSS/JS files
- **GH_TOKEN is sensitive** - it's embedded in the HTML source, don't expose it elsewhere
- **Print card always renders white** regardless of dark/light mode
- CSS custom properties define the theme (`:root` for dark, `[data-theme="light"]` for light)
- Auto-save triggers 1.5s after last change via `queueSave()`

## Deployment
1. Edit `index.html`
2. Push to `main` branch of `dylanfostercoxgp/rwo-registration`
3. GitHub Pages updates within 60-90 seconds
4. Users hard-refresh (Cmd+Shift+R) to get latest version

## GitHub Info
- **Account**: dylanfostercoxgp
- **Repo**: rwo-registration
- **Pages URL**: https://dylanfostercoxgp.github.io/rwo-registration

## Season Info (2026)
- Clearwater: Sep 26-28, 2026
- Miami: Nov 7-9, 2026
- Bimini: Jan 15-17, 2027
- Nassau: Mar 4-6, 2027

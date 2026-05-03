# bkness-stats

> **Automated GitHub Stats & Badges for bkness**

This repository powers dynamic badges for bkness’s public repositories and issues, using GitHub Actions and public gists.

<img src="assets/gist.svg">

## Dynamic Badges

<a href="https://weballtech.com">
	<img src="https://img.shields.io/badge/dynamic/json?color=blue&label=bkness's%20repos&query=%24.total_repos&url=https://gist.githubusercontent.com/bkness/b30f1f99edb7844f8484c6e520b5a322/raw/total-repos.json" alt="Total Public Repos" height="32" />
</a>
<a href="https://weballtech.com">
	<img src="https://img.shields.io/badge/dynamic/json?color=blue&label=bkness%20Issues&query=%24.total_issues&url=https://gist.githubusercontent.com/bkness/2cb0ef8788a0f3a9f061df669baeb90c/raw/total-issues.json" alt="Total Issues" height="32" />
</a>

## What is this?

- **Automates**: Counting public repos and issues for the bkness org/user.
- **Updates**: Gists with the latest stats on a schedule (via GitHub Actions).
- **Displays**: Live badges (above) using [shields.io](https://shields.io) and public gists.

## How it works

- GitHub Actions run every hour (or on demand) to update gists with the latest stats.
- Badges above fetch their data from those gists.

## Usage

- Fork or use as a template for your own stats/badges.
- Customize the workflow YAMLs and badge URLs for your own org/user and gists.

---

Made with ❤️ by [bkness](https://weballtech.com)

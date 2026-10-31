# Nightly copy to Google Drive

The nightly job copies the rulebook, config, deal database, ledgers, reports and code to a
`paper-portfolio` folder in your Google Drive: `paper-portfolio-latest.tar.gz` each night, and a
dated copy in `weekly/` each Friday. The step is skipped until the secret below exists, so nothing
happens until you set it up.

It uses rclone with your own Google sign-in, because Google does not let a service account store
files in a personal Drive.

## One-off setup (about 5 minutes, on your own computer)
1. Install rclone: https://rclone.org/install/ (on a Mac with Homebrew: `brew install rclone`).
2. Run `rclone config`, then:
   - `n` for a new remote, name it `gdrive` (exactly), storage type `drive`;
   - leave client id and secret blank; scope `1` (full access) or `3` (only files rclone creates);
   - accept the defaults for the rest, and say yes to auto config, which opens a browser to sign in to Google.
3. Run `rclone config show gdrive` and copy everything it prints, from `[gdrive]` to the end.
4. In GitHub: the repository, Settings, Secrets and variables, Actions, New repository secret.
   Name `RCLONE_CONF`, value: what you copied. Save.

The next nightly job then makes the folder and the first copy.

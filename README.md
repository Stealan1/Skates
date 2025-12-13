# Skatesmod

File download repository. This repository contains a collection of files that can be downloaded regularly from an app.

## Structure

- `/downloads/` - Contains all downloadable files

## Usage

### Adding Files

1. Place your files in the `/downloads/` directory
2. Update the `/downloads/README.md` with descriptions of each file
3. Commit and push your changes

### Downloading Files

Files can be accessed directly via GitHub's raw content URL:

```
https://raw.githubusercontent.com/Stealan1/Skatesmod/main/downloads/[filename]
```

Replace `[filename]` with the actual file name you want to download.

### From Your App

You can use HTTP requests to download files programmatically:

```bash
curl -O https://raw.githubusercontent.com/Stealan1/Skatesmod/main/downloads/[filename]
```

Or use your programming language's HTTP client library to fetch files from the URLs above.

## License

This is a file hosting repository for personal use.
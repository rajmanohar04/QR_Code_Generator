# QR Code Generator

A simple Python utility to generate QR codes from any text, URL, or other content.

## Features

* Generate QR codes from user input.
* Automatically creates a `generated_qr_codes` folder if it does not exist.
* Saves all generated QR codes as PNG images.
* Prevents accidental overwrites:

  * If a file already exists, asks whether to overwrite it.
  * If overwrite is declined, automatically creates a new filename using `_1`, `_2`, `_3`, etc.
* Automatically adds the `.png` extension if omitted.
* Handles invalid or empty input gracefully.

---

## Prerequisites

* Python 3.x

Verify Python installation:

```bash
python3 --version
```

---

## Installation

Install the required dependencies:

```bash
pip3 install qrcode pillow
```

---

## Usage

Run the script:

```bash
python3 qr_generator.py
```

You will be prompted for:

1. QR code content (URL, text, etc.)
2. Output filename

Example:

```text
Enter QR code content: https://chatgpt.com
Enter output filename: chatgpt
```

Output:

```text
QR code saved to: /path/to/generated_qr_codes/chatgpt.png
```

---

## Output Directory

All QR codes are stored in:

```text
generated_qr_codes/
```

The folder is automatically created in the current directory if it does not already exist.

Example:

```text
project/
├── qr_generator.py
├── README.md
└── generated_qr_codes/
    ├── chatgpt.png
    ├── google.png
    └── github.png
```

---

## Existing File Handling

If the specified filename already exists:

```text
'chatgpt.png' already exists.
Do you want to overwrite it? (y/n):
```

### Overwrite

If you enter:

```text
y
```

The existing file will be replaced.

### Create a New File

If you enter:

```text
n
```

The script automatically creates a new filename:

```text
chatgpt_1.png
chatgpt_2.png
chatgpt_3.png
```

Example output:

```text
Creating new file instead: chatgpt_1.png
QR code saved to: generated_qr_codes/chatgpt_1.png
```

---

## Supported Content

The QR code can contain:

* Website URLs
* Email addresses
* Phone numbers
* Plain text
* Wi-Fi credentials
* Any other text-based content

Examples:

```text
https://www.google.com
```

```text
Hello World
```

```text
mailto:test@example.com
```

```text
tel:+911234567890
```

---

## Error Handling

### Empty QR Content

```text
Error: QR code content cannot be empty.
```

### Empty Filename

```text
Error: Filename cannot be empty.
```

### User Cancellation

Press:

```text
Ctrl + C
```

Output:

```text
Operation cancelled by user.
```

---

## Example Session

```text
$ python3 qr_generator.py

Enter QR code content: https://chatgpt.com
Enter output filename: chatgpt

QR code saved to: generated_qr_codes/chatgpt.png
```

---

## License

This project is provided as-is for personal and educational use.

#!/usr/bin/env python3

import os
import qrcode
from qrcode.constants import ERROR_CORRECT_L


def get_output_directory():
    output_dir = os.path.join(os.getcwd(), "generated_qr_codes")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def get_unique_filename(output_dir, filename):
    base, ext = os.path.splitext(filename)

    counter = 1
    candidate = filename

    while os.path.exists(os.path.join(output_dir, candidate)):
        candidate = f"{base}_{counter}{ext}"
        counter += 1

    return candidate


def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    if not filename.lower().endswith(".png"):
        filename += ".png"

    output_dir = get_output_directory()
    output_path = os.path.join(output_dir, filename)

    if os.path.exists(output_path):
        while True:
            choice = input(
                f"'{filename}' already exists.\n"
                "Do you want to overwrite it? (y/n): "
            ).strip().lower()

            if choice == "y":
                break

            elif choice == "n":
                filename = get_unique_filename(output_dir, filename)
                output_path = os.path.join(output_dir, filename)

                print(
                    f"Creating new file instead: {filename}"
                )
                break

            else:
                print("Please enter 'y' or 'n'.")

    image.save(output_path)

    print(f"QR code saved to: {output_path}")


def main():
    try:
        data = input("Enter QR code content: ").strip()

        if not data:
            print("Error: QR code content cannot be empty.")
            return

        filename = input("Enter output filename: ").strip()

        if not filename:
            print("Error: Filename cannot be empty.")
            return

        generate_qr(data, filename)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except EOFError:
        print("\nInput stream closed.")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
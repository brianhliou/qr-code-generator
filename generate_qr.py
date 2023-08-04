import argparse
import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a QR code.')
    parser.add_argument('--data', type=str, required=True, help='The data to encode into a QR code')
    parser.add_argument('--file', type=str, required=True, help='The file path where the QR code will be saved')

    args = parser.parse_args()
    generate_qr_code(args.data, args.file)

# qr-code-generator

![QR Code 1](./resources/filename.png)

Commands to generate qr code on Windows:

1. py -m venv env
2. Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
3. .\env\Scripts\activate
4. pip install qrcode[pil]
5. py generate_qr.py --data "Your input string" --file "./resources/filename.png"

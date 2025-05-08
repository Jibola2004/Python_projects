import pyqrcode
import re
import png  # Required for saving as PNG

# Get URL input from user
url_code_input = input('Enter URL link: ').strip()

# Validate input
if not url_code_input:
    raise ValueError("❌ Empty input is not allowed.")

# Extract platform name using regex
match = re.search(r"https?://(?:www\.)?(?P<platform>\w+)\.com", url_code_input)

if not match:
    raise ValueError("❌ Could not extract platform name from the URL.")

platform = match.group("platform")

# Generate QR code
qr = pyqrcode.create(url_code_input)

# Save QR code as PNG with white background
file_name = f"{platform}.png"
qr.png(file_name, scale=8, background=[255, 255, 255])

print(f"✅ QR Code saved as '{file_name}' with white background.")

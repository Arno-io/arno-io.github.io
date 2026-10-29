import base64
import os

target_dir = "configs-output"
os.makedirs(target_dir, exist_ok=True)

# نمونه ساختار کانفیگ مناسب برای Warp-in-Warp / AmneziaWG
for idx in range(1, 21):
  # می‌توانید پارامترهای دلخواه خود یا کلیدهای WireGuard/AmneziaWG را اینجا قرار دهید
  awg_config = f"""[Interface]
PrivateKey = aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvv={idx:02d}
Address = 10.0.0.{idx}/32
DNS = 1.1.1.1, 8.8.8.8

[Peer]
PublicKey = server_public_key_here_{idx:02d}
Endpoint = example.com:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
Jc = 3
Jmin = 40
Jmax = 70
S1 = 56
S2 = 44
H1 = 1
H2 = 2
H3 = 3
H4 = 4
"""

  filename = os.path.join(target_dir, f"Arno-AmneziaWG-{idx:02d}.conf")

  with open(filename, "w", encoding="utf-8") as f:
    f.write(awg_config)

print("20 AmneziaWG Configs generated successfully in isolated folder.")

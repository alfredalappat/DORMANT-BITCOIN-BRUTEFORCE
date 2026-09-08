import time,os
from bit import Key
from bit.format import bytes_to_wif



output_file = "found.txt"
st=int(time.time())
hex_count = 0


with open("addresses.txt", "r", encoding="utf-8") as f:
    addresses = {line.strip() for line in f if line.strip()}


print(
      f"*******************************************************************************************************\n"
      f"Save to             : {output_file:<}")
print("DORMANT-BITCOIN-BRUTEFORCE")
time.sleep(1)
print("DON'T WORRY, THIS CODE IS NOT USING YOUR COMPUTING POWER FOR ME.")
print("DONATION BTC = bc1qjqmgkuu4qefgwpdq24dvmz60pvjnn7egvc4zke")
time.sleep(1)
print("Scanning starts...")
print("Total unique addresses:", len(addresses))
def generate_bitcoin_addresses():
    # Generate random 256-bit private key (as hex)
    priv_bytes = os.urandom(32)
    c=priv_bytes.hex()
    
    # Create compressed key
    wif_compressed = bytes_to_wif(priv_bytes, compressed=True)
    key_compressed = Key(wif_compressed)

    # Create uncompressed key
    wif_uncompressed = bytes_to_wif(priv_bytes, compressed=False)
    key_uncompressed = Key(wif_uncompressed)

    checking(c,key_compressed.address)
    checking(c,key_uncompressed.address)


def checking(privateKey,addr):
    if addr in addresses:
            print(f'\nPrivate Key: {privateKey}, Address: {addr}')
            result_string = f'Private Key: {privateKey}, Address: {addr}\n'
            with open(output_file, 'a') as f:
                f.write(result_string)




while True:
    generate_bitcoin_addresses()
    hex_count += 2
    if hex_count%100000==0:
        en=int(time.time())
        print("Total scanned = ",hex_count,f" || speed = {int(hex_count/(en-st))} keys per sec")
    

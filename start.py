import time
from .encrypt import testEncrypt

msg = "Hello World!"

start = time.time()

print(msg)

end = time.time()

print(f'{end-start:.5f} seconds')

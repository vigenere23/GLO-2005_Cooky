import bcrypt

hashed = bytearray(b'$2b$12$oLSRXG1kJ8xNX7T98Ryhtu2NCTwsbM/CXYnXd4t38ctzZ.2Ss3ciS')

password = '123'.encode()

print(bcrypt.checkpw(password, bytes(hashed)))

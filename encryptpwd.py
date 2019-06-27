#!/usr/bin/env python3

import crypt
import getpass

print(crypt.crypt(getpass.getpass("userpassword: "), crypt.METHOD_SHA512))


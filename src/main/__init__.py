from src.main.python.secure_all import AccessRequest

ar = AccessRequest("41694463V", "JOSE LOPEZ", "GUEST", "jlopez@inf.uc3m.es", 5)
print(ar.access_code)

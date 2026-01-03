from ldap3 import Server, Connection, ALL

def authenticate_ldap(ldap_server, base_dn, username, password, dummy_mode=False):
    if dummy_mode:
        # Simulate authentication for testing
        if username == "testuser" and password == "testpass":
            print(f"[✔] (Dummy Mode) Authentication successful for: {username}")
            return True
        else:
            print(f"[✘] (Dummy Mode) Authentication failed for: {username}")
            return False
    else:
        try:
            # Connect to the LDAP Server
            server = Server(ldap_server, get_info=ALL)
            user_dn = f"uid={username},{base_dn}"
            conn = Connection(server, user=user_dn, password=password, auto_bind=True)

            print(f"[✔] Authentication successful for: {username}")
            return True
        except Exception as e:
            print(f"[✘] Authentication failed: {str(e)}")
            return False

if __name__ == "__main__":
    # Ask user if they want to use dummy mode
    use_dummy = input("Use dummy mode for testing? (yes/no): ").strip().lower() == "yes"

    if use_dummy:
        print("Running in dummy mode (Use 'testuser' as username and 'testpass' as password to succeed).")
        ldap_server, base_dn = "dummy_server", "dummy_base_dn"
    else:
        ldap_server = input("Enter LDAP server address (e.g., ldap://your-ldap-server): ").strip()
        base_dn = input("Enter Base DN (e.g., dc=example,dc=com): ").strip()

    username = input("Enter LDAP username: ").strip()
    password = input("Enter LDAP password: ").strip()

    authenticate_ldap(ldap_server, base_dn, username, password, dummy_mode=use_dummy)


import argparse
import winreg


class UserAssist:
    def __init__(self):
        self.hive = winreg.HKEY_CURRENT_USER
        self.key_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"

    def toggle(self, enabled: bool) -> None:
        key = winreg.OpenKey(self.hive, self.key_path, 0, winreg.KEY_SET_VALUE)

        try:
            if enabled:
                winreg.SetValueEx(key, "Start_TrackProgs", 0, winreg.REG_DWORD, 1)
                winreg.SetValueEx(key, "Start_TrackEnabled", 0, winreg.REG_DWORD, 1)
                print(f"[+] UserAssist Logging Enabled")
            else:
                winreg.SetValueEx(key, "Start_TrackProgs", 0, winreg.REG_DWORD, 0)
                winreg.SetValueEx(key, "Start_TrackEnabled", 0, winreg.REG_DWORD, 0)
                print(f"[+] UserAssist Logging Disabled")
        except Exception as e:
            print(e)

        winreg.CloseKey(key)

    def enum_value(self):
        key = winreg.OpenKey(self.hive, self.key_path)
        total_values = winreg.QueryInfoKey(key)[1]

        try:
            for i in range(0, total_values):
                value_name = winreg.EnumValue(key, i)[0]
                if value_name == "Start_TrackProgs":
                    value = winreg.EnumValue(key, i)[1]
                    if value == 1:
                        print(f"[+] Start_TrackProgs is enabled.")
                    else:
                        print(f"[+] Start_TrackProgs is disabled.")
        except Exception as e:
            print(e)

        try:
            for i in range(0, total_values):
                value_name = winreg.EnumValue(key, i)[0]
                if value_name == "Start_TrackEnabled":
                    value = winreg.EnumValue(key, i)[1]
                    if value == 1:
                        print(f"[+] Start_TrackEnabled is enabled.")
                    else:
                        print(f"[+] Start_TrackEnabled is disabled.")
        except Exception as e:
            print(e)

        print(f"[!] If no output, the keys do not exist.")
        winreg.CloseKey(key)


def main():
    parser = argparse.ArgumentParser(description="Enable/Disable UserAssist Program Logging")
    parser.add_argument('--disable', required=False, dest="disable", action="store_true")
    parser.add_argument('--enable', required=False, dest="enable", action="store_true")
    parser.add_argument('--enum', required=False, dest="enum", default=False, action="store_true")

    args = parser.parse_args()

    ua = UserAssist()

    if args.disable:
        ua.toggle(False)

    if args.enable:
        ua.toggle(True)

    if args.enum:
        print(f"[!] Warning: Running enum will create a registry access event.")
        response = input("Would you like to continue? (y/n)")
        if response.lower() == "y":
            ua.enum_value()


if __name__ == '__main__':
    main()

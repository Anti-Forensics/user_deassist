import winreg


class UserAssist:
    def __init__(self):
        self.hive = winreg.HKEY_CURRENT_USER
        self.key_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"

    def toggle(self, enabled: bool) -> None:
        if enabled:
            key = winreg.OpenKey(self.hive, self.key_path)
            winreg.SetValueEx(key, "Start_TrackProgs", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "Start_TrackEnabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(key)
            print(f"[+] UserAssist Logging Enabled")
        else:
            key = winreg.OpenKey(self.hive, self.key_path)
            winreg.SetValueEx(key, "Start_TrackProgs", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key, "Start_TrackEnabled", 0, winreg.REG_DWORD, 0)
            winreg.CloseKey(key)
            print(f"[+] UserAssist Logging Disabled")

    def enum_value(self):
        key = winreg.OpenKey(self.hive, self.key_path)
        total_values = winreg.QueryInfoKey(key)[1]

        try:
            for i in range(0, total_values):
                found = False
                value_name = winreg.EnumValue(key, i)[0]
                if value_name == "Start_TrackProgs":
                    found = True
                    value = winreg.EnumValue(key, i)[1]
                    if value == 1:
                        print(f"[+] Start_TrackProgs is enabled.")
                    else:
                        print(f"[+] Start_TrackProgs is disabled.")
                elif found is False and i == total_values - 1:
                    print(f"[!] Start_TrackTrackProgs value not found.")

        except Exception as e:
            print(e)

        try:
            for i in range(0, total_values):
                found = False
                value_name = winreg.EnumValue(key, i)[0]
                if value_name == "Start_TrackEnabled":
                    found = True
                    value = winreg.EnumValue(key, i)[1]
                    if value == 1:
                        print(f"[+] Start_TrackEnabled is enabled.")
                    else:
                        print(f"[+] Start_TrackEnabled is disabled.")
                elif found is False and i == total_values - 1:
                    print(f"[!] Start_TrackTrackEnabled value not found.")
            winreg.CloseKey(key)

        except Exception as e:
            print(e)


def main():
    ua = UserAssist()
    ua.enum_value()
    ua.toggle(False)


if __name__ == '__main__':
    main()

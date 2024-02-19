import winreg


class UserAssist:
    def __init__(self):
        self.hive = winreg.HKEY_CURRENT_USER
        self.track_progs = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"
        self.track_enabled = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"

    def enable_toggle(self, toggle: bool) -> None:
        if toggle:
            print(f"[+] UserAssist Logging Enabled")
        else:
            print(f"[+] UserAssist Logging Disabled")

    def enum_value(self):
        try:
            key = winreg.OpenKey(self.hive, self.track_progs)
            total_values = winreg.QueryInfoKey(key)[1]
            for i in range(0, winreg.QueryInfoKey(key)[1]):
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
            key = winreg.OpenKey(self.hive, self.track_enabled)
            total_values = winreg.QueryInfoKey(key)[1]
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
        except Exception as e:
            print(e)


def main():
    ua = UserAssist()
    ua.enum_value()


if __name__ == '__main__':
    main()

from server import GSIServer
import time
import telnetlib

class DisableSilencer:
    def __init__(self):
        self.buffer = None
        self.attack2buffer = 0

        self.create_telnet_connection()
        self.server = GSIServer(("127.0.0.1", 6312), "8N51G9Jlx59kSARIM")
        self.server.start_server()
        self.check_weapon_loop()

    def create_telnet_connection(self):
        while True:
            try:
                self.tn = telnetlib.Telnet("127.0.0.1", 6313)
                break
            except Exception as e:
                print(e)
                self.write_log(e)
            finally:
                time.sleep(5)

    def send_command(self, command):
        command = command + "\n"
        command = command.encode("utf-8")
        try:
            self.tn.write(command)
        except ConnectionResetError:
            print(e)
            self.write_log(e)
            return

    def write_log(self, message):
        with open("log.txt", "a") as log_file:
            message = time.strftime("%H:%M:%S", time.localtime()) + " | " + str(message)
            log_file.write(message + "\n")

    def check_weapon_loop(self):
        while True:
            weapons = self.server.get_info("player", "weapons")
            for weapon in weapons:
                if weapons[weapon]["state"] == "active":
                    if "silencer" in weapons[weapon]["name"]:
                        if self.buffer != "silenced_weapon_active":
                            self.send_command("unbind mouse2")
                            self.buffer = "silenced_weapon_active"

                        else:
                            time.sleep(.49) # usp / m4a1 deploy time 1sec, with <0.49sec intervals we can catch every instance of right click
                            self.send_command("-attack2")   # being held while weapon is deployed

                    else:
                        if self.buffer != "unsilenced_weapon_active":
                            self.send_command("bind mouse2 +attack2")
                            self.buffer = "unsilenced_weapon_active"
                    break       # stop looking for weapons once found active weapon

if __name__ == "__main__":
    silencer = DisableSilencer()

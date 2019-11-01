import payload
import configparser
import common


class Lightdm(payload.Payload):
    name = "Lightdm securing"
    os = ["Ubuntu"]
    os_version = ["16.04"]

    def execute(self):
        common.debug("Lightdm has been executed!")
        path = "/etc/lightdm/lightdm.conf"
        config = configparser.ConfigParser()
        try:
            common.backup(path)
            config.read(path)
        except FileNotFoundError as ex:
            common.error("{} not found".format(path), ex)

        config["SeatDefaults"] = {}
        config["SeatDefaults"]["user-session"] = "ubuntu"
        config["SeatDefaults"]["greeter-session"] = "unity-greeter"
        config["SeatDefaults"]["greeter-show-manual-login"] = "true"
        config["SeatDefaults"]["greeter-hide-users"] = "true"
        config["SeatDefaults"]["allow-guest"] = "false"

        with open(path, "w+") as out_file:
            config.write(out_file)

        common.info("{} updated".format(path))
        common.debug("Lightdm has finished")

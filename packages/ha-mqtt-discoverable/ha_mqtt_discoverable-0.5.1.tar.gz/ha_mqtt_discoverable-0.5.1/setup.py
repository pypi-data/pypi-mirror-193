# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ha_mqtt_discoverable', 'ha_mqtt_discoverable.cli']

package_data = \
{'': ['*']}

install_requires = \
['gitlike-commands>=0.2.1,<0.3.0',
 'paho-mqtt>=1.6.1,<2.0.0',
 'pyaml>=21.10.1,<22.0.0',
 'pydantic>=1.10.5,<2.0.0',
 'thelogrus>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['hmd = ha_mqtt_discoverable.cli.main_driver:hmd_driver',
                     'hmd-create-binary-sensor = '
                     'ha_mqtt_discoverable.cli.sensor_driver:create_binary_sensor',
                     'hmd-create-device = '
                     'ha_mqtt_discoverable.cli.device_driver:create_device',
                     'hmd-version = ha_mqtt_discoverable.cli:module_version']}

setup_kwargs = {
    'name': 'ha-mqtt-discoverable',
    'version': '0.5.1',
    'description': '',
    'long_description': '<!-- START doctoc generated TOC please keep comment here to allow auto update -->\n<!-- DON\'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->\n## Table of Contents\n\n- [ha-mqtt-discoverable](#ha-mqtt-discoverable)\n  - [Installing](#installing)\n    - [Python](#python)\n    - [Docker](#docker)\n  - [Supported entities](#supported-entities)\n    - [Binary sensor](#binary-sensor)\n      - [Usage](#usage)\n  - [Device](#device)\n      - [Usage](#usage-1)\n  - [Contributing](#contributing)\n  - [Scripts Provided](#scripts-provided)\n    - [`hmd`](#hmd)\n    - [`hmd create binary sensor`](#hmd-create-binary-sensor)\n    - [`hmd create device`](#hmd-create-device)\n  - [Contributors](#contributors)\n\n<!-- END doctoc generated TOC please keep comment here to allow auto update -->\n\n# ha-mqtt-discoverable\n\nA python 3 module that takes advantage of HA(Home Assistant(\'s MQTT discovery protocol to create sensors without having to define anything on the HA side.\n\nUsing MQTT discoverable devices lets us add new sensors and devices to HA without having to restart HA. This module includes scripts to make it easy to create discoverable devices from the command line if you don\'t want to bother writing python.\n\n## Installing\n\n### Python\n\nha-mqtt-discoverable runs on Python 3.10 or later.\n\n`pip install ha-mqtt-discoverable` if you want to use it in your own python scripts. This will also install the `hmd` utility scripts.\n\n### Docker\n\nIf all you want to do is use the command line tools, the simplest way is to use them with `docker` or `nerdctl`. It won\'t interfere with your system python and potentially cause you issues there. You can use the [unixorn/ha-mqtt-discoverable](https://hub.docker.com/repository/docker/unixorn/ha-mqtt-discoverable) image on dockerhub directly, but if you add `$reporoot/bin` to your `$PATH`, the `hmd` script in there will automatically run the command line tools inside a docker container with `docker` or `nerdctl`, depending on what it finds in your `$PATH`.\n\n## Supported entities\n\nThe following Home Assistant entities are currently implemented:\n\n- Sensor\n- Binary sensor\n\n### Binary sensor\n\n#### Usage\n\nThe following example creates a binary sensor and sets its state:\n\n```py\nfrom ha_mqtt_discoverable import Settings\nfrom ha_mqtt_discoverable.sensors import BinarySensor, BinarySensorInfo\n\n\n# Configure the required parameters for the MQTT broker\nmqtt_settings = Settings.MQTT(host="localhost")\n\n# Information about the sensor\nsensor_info = BinarySensorInfo(name="MySensor", device_class="motion")\n\nsettings = Settings(mqtt=mqtt_settings, entity=sensor_info)\n\n# Instantiate the sensor\nmysensor = BinarySensor(settings)\n\n# Change the state of the sensor, publishing an MQTT message that gets picked up by HA\nmysensor.on()\nmysensor.off()\n\n```\n\n## Device\nFrom the [Home Assistant documentation](https://developers.home-assistant.io/docs/device_registry_index):\n> A device is a special entity in Home Assistant that is represented by one or more entities.\nA device is automatically created when an entity defines its `device` property.\nA device will be matched up with an existing device via supplied identifiers or connections, like serial numbers or MAC addresses.\n\n#### Usage\n\nThe following example create a device, by associating multiple sensors to the same `DeviceInfo` instance.\n\n```py\nfrom ha_mqtt_discoverable import Settings, DeviceInfo\nfrom ha_mqtt_discoverable.sensors import BinarySensor, BinarySensorInfo\n\n# Configure the required parameters for the MQTT broker\nmqtt_settings = Settings.MQTT(host="localhost")\n\n# Define the device. At least one of `identifiers` or `connections` must be supplied\ndevice_info = DeviceInfo(name="My device", identifiers="device_id")\n\n# Associate the sensor with the device via the `device` parameter\n# `unique_id` must also be set, otherwise Home Assistant will not display the device in the UI\nmotion_sensor_info = BinarySensorInfo(name="My motion sensor", device_class="motion", unique_id="my_motion_sensor", device=device_info)\n\nmotion_settings = Settings(mqtt=mqtt_settings, entity=sensor_info)\n\n# Instantiate the sensor\nmotion_sensor = BinarySensor(motion_settings)\n\n# Change the state of the sensor, publishing an MQTT message that gets picked up by HA\nmotion_sensor.on()\n\n# An additional sensor can be added to the same device, by re-using the DeviceInfo instance previously defined\ndoor_sensor_info = BinarySensorInfo(name="My door sensor", device_class="door", unique_id="my_door_sensor", device=device_info)\ndoor_settings = Settings(mqtt=mqtt_settings, entity=door_sensor_info)\n\n# Instantiate the sensor\ndoor_sensor = BinarySensor(settings)\n\n# Change the state of the sensor, publishing an MQTT message that gets picked up by HA\ndoor_sensor.on()\n\n# The two sensors should be visible inside Home Assistant under the device `My device`\n```\n\n## Contributing\n\nPlease run `black` on your code before submitting. There are `git` hooks already configured to run `black` every commit, you can run `./hooks/autohook.sh install` to enable them.\n\n## Scripts Provided\n\nThe `ha_mqtt_discoverable` module also installs the following helper scripts you can use in your own shell scripts.\n\n### `hmd`\n\nUses the [gitlike-commands](https://github.com/unixorn/gitlike-commands/) module to find and execute `hmd` subcommands. Allows you to run `hmd create binary sensor` and `hmd` will find and run `hmd-create-binary-sensor` and pass it all the command line options.\n\n### `hmd create binary sensor`\n\nCreate/Update a binary sensor and set its state.\n\nUsage: `hmd create binary sensor --device-name mfsmaster --device-id 8675309 --mqtt-user HASS_MQTT_USER --mqtt-password HASS_MQTT_PASSWORD --client-name inquisition --mqtt-server mqtt.unixorn.net --metric-name tamper --device-class motion --state off`\n\n### `hmd create device`\n\nCreate/Update a device and set the state of multiple metrics on it.\n\nUsage: `hmd create device --device-name coyote --device-id 8675309 --mqtt-user HASS_MQTT_USER --mqtt-password HASS_MQTT_PASSWORD --mqtt-server mqtt.example.com --model \'Rocket Skates\' --manufacturer \'Acme Products\' --metric-data \'{"name":"Left Rocket Skate","value":93}\' --metric-data \'{"name":"Right Rocket Skate","value":155}\' --unique-id \'hmd-26536\'`\n\n## Contributors\n\n<a href="https://github.com/unixorn/ha-mqtt-discovery/graphs/contributors">\n  <img src="https://contributors-img.web.app/image?repo=unixorn/ha-mqtt-discovery" />\n</a>\n\nMade with [contributors-img](https://contributors-img.web.app).\n',
    'author': 'Joe Block',
    'author_email': 'jpb@unixorn.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<4.0',
}


setup(**setup_kwargs)

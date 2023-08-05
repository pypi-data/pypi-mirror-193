Set alarms from your terminal.

## Installation
You can install this package using `pip`:

``` sh
pip install pylarm
```

The command `pylarm` will then be available from your terminal.

## Usage example

### Set an alarm
``` sh
pylarm set --sound <PATH_TO_SOUND_FILE> --message='The time has come!' --at='17:00' &
```

You can also simply run
``` sh
pylarm set --sound <PATH_TO_SOUND_FILE>
```
and you'll be prompted to select the time and the message.

### Cancel an alarm
After setting an alarm, you'll be informed of the pid of that alarm.
You can use it to cancel the alarm as follows:

``` sh
pylarm cancel --pid=<PID_OF_THE_ALARM>
```

Again, you can simply run 
``` sh
pylarm cancel
```
and you'll be prompted to select the pid.

To know the details about a subcommand you can run `pylarm <subcommand> --help`.



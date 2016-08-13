#!/usr/bin/env python3

""" This records data from the circuit I designed. ADS1015 channel A0 reads
data from a load cell, and channel A1 monitors the voltage provided by the
batteries.

It's also my first attempt at writing such a control program.

Be wary on both counts.
"""

# if(self.alert_pin):
#     RPIO.wait_for_thing TODO
# # See http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# # It's as simple as "GPIO.wait_for_edge(pin, GPIO.FALLING)"

# May want this: https://github.com/groeck/i2c-tools/tree/master/py-smbus
# By default, Adafruit_GPIO.I2C (used by Adafruit_ADS1x15) uses Adafruit's
# own python-pureio smbus. Which is weird. But it takes a smbus interface
# as an optional argument, so maybe I can make it work.

from __future__ import print_function
import time
import argparse
from sys import stderr, stdin, stdout
from threading import Thread
import traceback

import Adafruit_ADS1x15
import Adafruit_GPIO.GPIO
GPIO = Adafruit_GPIO.GPIO.get_platform_gpio() # wrapper for RPIO that
# looks like a convenient way to port this whole product to something like
# a USB GPIO dongle on a laptop.

ADS1015_RATES = Adafruit_ADS1x15.ADS1x15.ADS1015_CONFIG_DR.keys()
#[128, 250, 490, 920, 1600, 2400, 3300]
ADS1015_GAINS = Adafruit_ADS1x15.ADS1x15.ADS1x15_CONFIG_GAIN.keys()
DEFAULT_ALERT_PIN = 4 # BCM 4, closest to the I2C pins.
BATTERY_SAMPLE_SIZE = 4 # How many measurements constitute a single reading from
# the battery.
BATTERY_RATE = 3300 # Data rate while taking adc measurements.
BATTERY_GAIN = 16
BATTERY_CHANNEL_DEFAULT = 1
LC_CHANNEL_DEFAULT = 0
TITLE_LINE = "Time (s),Load Cell,Battery"
LC_DATA_FORMAT = '{0},{1},'
BATTERY_DATA_FORMAT = '{0},,{1}'

class Sleeper(object):
    """ This is used to ensure that an appropriate interval passes between
    calls to get_last_result() if falling-edge detection is not being
    used.

    This class is likely the worst thing in this entire module.
    """
    def __init__(self, rate, measure, samples=1):
        """ Pass in
        rate (frequency in Hz) of data collection
        method of data collection that takes no arguments,
        e.g. adc.get_last_result
        """
        start_time = time.time()
        for i in range(samples):
            measure()
        total_time = time.time() - start_time
        avg_time = total_time / samples

        if avg_time < samples * 1.0 / rate: # Consider changing 1.0 to 0.95
            self.sleep = lambda obj: time.sleep(1.0 / rate - avg_time)
        else:
            self.sleep = lambda obj: None

class EndCondition(Thread):
    """ Programming with threads, lesson 0.
    I'm proud of myself.
    ... This thread sets a boolean when it reads an EOF (ctrl-D) from
    stdin. Use it to signal the end of your test.
    """
    def __init__(self, *args, **kwargs):
        """See class docstring."""
        super(EndCondition, self).__init__(*args, **kwargs)
        self.finished = False

    def run(self):
        """ Run until an EOF is received in stdin.
        Then set self.finished to True.
        """
        stdin.read()
        self.finished = True

class SimpleTimer(object):
    """Used to track the time since initialization. Slightly cleaner than
    time.time.
    I still use time.time when I don't need something worth printing.
    """
    def __init__(self):
        """Constructor.

        SimpleTimer counts the time since its constructor is called. So you could
        say that this function marks the start of a new epoch.
        """
        self.start_time = time.time()

    def __call__(self):
        """Print the time since this was initialized."""
        return time.time() - self.start_time


class BatteryChecker(object):
    """Does a lovely job of pausing the load cell data collection in order
    to monitor the batter level a little bit.

    Use this with the 'with ... as ...:' syntax.
    """
    def __init__(self, adc, count, start_lc=None, start_battery=None,
                 wait_function=None, file=stdout, get_time=time.time):
        self.adc = adc
        self.count = count
        self.start_lc = start_lc
        self.start_battery = start_battery
        self.wait_function = wait_function
        self.file = file
        self.get_time = get_time

    def take_data(self):
        for i in range(count):
            self.wait_function()
            print(BATTERY_DATA_FORMAT.format(self.get_time(),
                                             self.adc.get_last_result()),
                  file=self.file)


    def __enter__(self):
        """Executes at the beginning of a 'with ... as' block."""
        self.adc.stop_adc() # this may be unnecessary
        self.start_battery()
        return self.take_data

    def __exit__(self, type, value, traceback):
        adc.stop_adc()

def read_battery(adc, count, start_lc=None, start_battery=None,
                 wait_function=None, file=stdout, get_time=time.time):
    """Read 'count' data points from the battery channel of the adc.
    The kwargs are functions to start the ADS1015 in the right modes to sample
    the different outputs. The idea is that this function will clean up after
    itself. It is an error to omit the function arguments.

    If the condition to stop taking data is met during this call, the call
    will finish anyway. Shouldn't be a huge deal.

    The 'with ... as ...:' syntax could be used to similar effect. I tried
    it, but in my opinion the resulting code was less readable than this.
    """
    adc.stop_adc() # Stop doing the previous thing. Seems wise to call this,
    # although it might not be necessary.
    start_battery()
    for i in range(count):
        wait_function()
        print(BATTERY_DATA_FORMAT.format(get_time(), adc.get_last_result()),
              file=file)
    adc.stop_adc()
    start_lc()


def main(duration=0, rate=3300, gain=16, verbose=False, **kwargs):
    """ Take data from the ADS1015 for duration seconds (or until stdin receives
    EOF, if duration is 0) at rate and gain.

    Default argument values may not be the same as for the command line arguments.
    See the ArgumentParser instance below.

    Kwargs:
    lc_channel = the channel of the ads1015 from which to read load cell data.
    comparator = Whether to use the ALERT/RDY pin instead of time.sleep().
        This is highly recommended, provided the hardware is setup.
    comparator_pin = the GPIO pin from which to yoink the comparator.
        This is specified as a BCM number.
    battery_check_freq = frequency to check the battery level. Not exact!
        1 Hz by default... but setting 2 Hz results in ~ 1 Hz measurements.
    battery_channel = obvious.
    Sends the data to stdout.
    We're using common mode, not differential mode.
    At 3300 samples per second, this generates 2.2 MB of ascii per minute,
    which is probably fine.
    """

    if verbose:
        print("Debugging information:", file=stderr)
        for key in kwargs:
            print(key + ": {0}".format(kwargs[key]), file=stderr)
    adc = Adafruit_ADS1x15.ADS1015()

    lc_channel = kwargs['lc_channel'] if 'lc_channel' in kwargs else 0
    use_comp = kwargs['comparator'] if 'comparator' in kwargs else False
    differential = kwargs['differential'] if 'differential' in kwargs else False

    battery_check_freq = (kwargs['battery_check_freq']
                          if 'battery_check_freq' in kwargs else 1)
    battery_channel = (kwargs['battery_channel'] if 'battery_channel' in kwargs
                       else 1)
    battery_counter_limit = rate / battery_check_freq
    assert battery_counter_limit > 0
    pretty_time = SimpleTimer()


    print(TITLE_LINE, file=stdout)
    if duration == 0:
        # The test will run until ctrl-D is sent
        end_condition = EndCondition()
        end_condition.start()
        keep_going = lambda: not end_condition.finished
    else:
        # The test will run for the specified number of seconds.
        time_stop = time.time() + duration
        keep_going = lambda: time.time() < time_stop

    # Setup the ADC. See ADS1015 datasheet, pages 12 and 17.
    if use_comp:
        # Set up the test, using the ALERT/RDY pin in "conversion-ready" mode.
        print("Comparator mode", file=stderr)
        ready_pin = kwargs['comparator_pin']

        # Setup and fish for debilitating GPIO exceptions:
        GPIO.setup(ready_pin, Adafruit_GPIO.IN,
                   pull_up_down=Adafruit_GPIO.PUD_OFF)
        wait_function = lambda: GPIO.wait_for_edge(ready_pin,
                                                   Adafruit_GPIO.FALLING)

        # A couple things are different depending on whether we're measuring
        # between lc_channel and ground, or between lc_channel and some other
        # analogue input (i.e. kwargs['diff_channel']).
        if differential:
            print("Also differential mode", file=stderr)
            # lc_channel, until this next part executes, has represented a single analog
            # input pin on the ADS1015. To measure the difference between two analog inputs,
            # we need to change it into a special value that's meaningful only to the
            # ads_1015 hardware. See the ADS1015 data sheet, page 16.
            diff_channel = kwargs['diff_channel'] if 'diff_channel' in kwargs else None
            assert 0 <= diff_channel <= 3 and diff_channel != lc_channel
            if lc_channel == 0 and diff_channel == 1:
                lc_channel = 0
            elif lc_channel == 0 and diff_channel == 3:
                lc_channel = 1
            elif lc_channel == 1 and diff_channel == 3:
                lc_channel = 2
            elif lc_channel == 2 and diff_channel == 3:
                lc_channel = 3
            else:
                raise ValueError()
            lc_start_adc_function = adc.start_adc_difference_comparator
        else:
            # Single ended mode is the opposite of differential mode, of course.
            print("Also single-ended mode")
            lc_start_adc_function = adc.start_adc_comparator

        # Set up the test, using the ALERT/RDY pin in "conversion-ready" mode.
        # We store these functions because we will need to switch modes
        # repeatedly in order to read both the
        start_lc = lambda: lc_start_adc_function(
            lc_channel, -1, 1, # Hi_thresh < 0 < Lo_thresh -> conversion ready mode
            data_rate=rate, gain=gain, latching=False, # latching is ignored
            num_readings=1, traditional=False, active_low=True,
            wait_function=wait_function)
        start_battery = lambda: adc.start_adc_comparator(
            battery_channel, -1, 1, # Same idea.
            data_rate=BATTERY_RATE, gain=BATTERY_GAIN,
            latching=False, # latching is ignored
            num_readings=1, traditional=False, active_low=True,
            wait_function=wait_function)

        do_cleanup = lambda: GPIO.cleanup(pin=ready_pin)
    else:
        # We have no ALERT/RDY pin, so set up the test to use time.sleep() instead
        # of GPIO interrupts.
        # TODO: Refactor so that you can do differential measurements in this mode.
        sleeper = Sleeper(rate, lambda: (time.time(), adc.get_last_result()))
        wait_function = sleeper.sleep # sleeps roughly the right amount
        start_lc = lambda: adc.start_adc(
            lc_channel, gain=gain, data_rate=rate)
        start_battery = lambda: adc.start_adc(
            battery_channel, gain=gain, data_rate=BATTERY_RATE)
        do_cleanup = lambda: None

    # This is the main loop. All the lambdas and complicated stuff above
    # happened so that this loop could be clear and readable.
    start_lc()
    battery_check_counter = 0

    try:
        while keep_going():
            try:
                if battery_check_counter > battery_counter_limit:
                    read_battery(adc, BATTERY_SAMPLE_SIZE, start_lc=start_lc,
                                 start_battery=start_battery, file=stdout,
                                 wait_function=wait_function, get_time=pretty_time)
                    battery_check_counter = 0
                battery_check_counter += 1
                wait_function()
                print(LC_DATA_FORMAT.format(pretty_time(), adc.get_last_result()),
                      file=stdout)
            except IOError:
                if verbose:
                    traceback.print_exc()
                start_lc()
                continue
    finally:
        do_cleanup()
        adc.stop_adc()
        print("Cleaned up.", file=stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Collect data at some rate and duration. The "
        "actual rate of data collection is guaranteed to be less "
        "than the requested rate. This is because the Raspberry "
        "Pi does not have a hardware RTC (real time clock). See "
        "documentation for time.sleep.")
    parser.add_argument("-d", "--duration", type=int, default=0,
                        help="Length of time during which to take samples, "
                        "in seconds. If duration is 0 or omitted, then samples"
                        " are collected until an EOF is received in stdin."
                        " This means it runs until you press C-d.")
    parser.add_argument("-r", "--rate", type=int, default=3300,
                        choices=ADS1015_RATES,
                        help="Maximum rate at which to sample data, in "
                        "Hz (samples per second).")
    parser.add_argument("-g", "--gain", type=int, default=16,
                        choices=ADS1015_GAINS,
                        help="Gain of the ADS1015, in V/V (i.e. unitless)."
                        " (0 gives a gain of 2/3. Not my fault.)")
    parser.add_argument("-c", "--comparator-mode", action="store_true",
                        help="Enables comparator (ALERT/RDY pin)."
                        " For the actual test, I definitely want this."
                        " The alternative is to rely on time.sleep() for"
                        " timing-critical data collection, which is a "
                        "huge issue.")
    parser.add_argument("-p", "--comparator-pin", type=int, default=4,
                        help="BCM pin number for the GPIO pin from which "
                        "to read comparator values. Ignored without -c.")
    parser.add_argument("-b", "--battery-check-freq", type=int, default=2,
                        help="Frequency with which to measure the battery level."
                        " Note that a single act of measuring involves taking {0}"
                        " actual samples at 3300 Hz.".format(BATTERY_SAMPLE_SIZE))
    parser.add_argument("-D", "--differential", action="store_true",
                        help="Enables differential measurement of load cell"
                        " voltage.")
    parser.add_argument("-C", "--differential-channel", type=int, default=3,
                        help="The channel from which to measure differential"
                        " voltage.")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Print the keyword arguments to main() when main"
                        " is called. Also allow printing of the mysterious "
                        "IOErrors in the main loop. Only useful for debugging.")


    argv = parser.parse_args()
    main(duration=argv.duration, rate=argv.rate, gain=argv.gain,
         comparator=argv.comparator_mode, comparator_pin=argv.comparator_pin,
         lc_channel=LC_CHANNEL_DEFAULT, battery_check_freq=argv.battery_check_freq,
         battery_channel=BATTERY_CHANNEL_DEFAULT, differential=argv.differential,
         diff_channel=argv.differential_channel,
         verbose=argv.verbose)

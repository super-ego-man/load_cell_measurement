EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:fromtemplate-cache
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "9 aug 2016"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L AD8237 AD8237?
U 1 1 57AA14F9
P 4050 3500
F 0 "AD8237?" H 4100 4600 60  0001 C CNN
F 1 "AD8237" H 4100 4600 60  0000 C CNN
F 2 "" H 4150 4250 60  0000 C CNN
F 3 "" H 4150 4250 60  0000 C CNN
	1    4050 3500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 57AA154B
P 1650 5700
F 0 "#PWR?" H 1650 5700 30  0001 C CNN
F 1 "GND" H 1650 5630 30  0001 C CNN
F 2 "" H 1650 5700 60  0000 C CNN
F 3 "" H 1650 5700 60  0000 C CNN
	1    1650 5700
	1    0    0    -1  
$EndComp
$Comp
L AD8237 AD8237?
U 1 1 57AA1598
P 4200 5500
F 0 "AD8237?" H 4250 6600 60  0001 C CNN
F 1 "AD8237" H 4250 6600 60  0000 C CNN
F 2 "" H 4300 6250 60  0000 C CNN
F 3 "" H 4300 6250 60  0000 C CNN
	1    4200 5500
	1    0    0    -1  
$EndComp
$Comp
L ADS1015 ADS1015?
U 1 1 57AA1815
P 7300 2250
F 0 "ADS1015?" H 7250 2750 60  0001 C CNN
F 1 "ADS1015" H 7250 2750 60  0000 C CNN
F 2 "~" H 7250 2650 60  0000 C CNN
F 3 "~" H 7250 2650 60  0000 C CNN
	1    7300 2250
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR?
U 1 1 57AA1B5C
P 1800 5550
F 0 "#PWR?" H 1800 5510 30  0001 C CNN
F 1 "+3.3V" H 1800 5660 30  0000 C CNN
F 2 "" H 1800 5550 60  0000 C CNN
F 3 "" H 1800 5550 60  0000 C CNN
	1    1800 5550
	1    0    0    1   
$EndComp
$Comp
L R R?
U 1 1 57AA1F79
P 2500 3850
F 0 "R?" V 2580 3850 40  0000 C CNN
F 1 "12.93 K" V 2507 3851 40  0000 C CNN
F 2 "~" V 2430 3850 30  0000 C CNN
F 3 "~" H 2500 3850 30  0000 C CNN
	1    2500 3850
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 57AA1FF8
P 3000 3850
F 0 "R?" V 3080 3850 40  0000 C CNN
F 1 "99.97" V 3007 3851 40  0000 C CNN
F 2 "~" V 2930 3850 30  0000 C CNN
F 3 "~" H 3000 3850 30  0000 C CNN
	1    3000 3850
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 57AA2007
P 3500 3850
F 0 "R?" V 3580 3850 40  0000 C CNN
F 1 "9.006 K" V 3507 3851 40  0000 C CNN
F 2 "~" V 3430 3850 30  0000 C CNN
F 3 "~" H 3500 3850 30  0000 C CNN
	1    3500 3850
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 57AA20BB
P 2750 4300
F 0 "R?" V 2830 4300 40  0000 C CNN
F 1 "24.85 K" V 2757 4301 40  0000 C CNN
F 2 "~" V 2680 4300 30  0000 C CNN
F 3 "~" H 2750 4300 30  0000 C CNN
	1    2750 4300
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA224A
P 5400 5100
F 0 "R?" V 5480 5100 40  0000 C CNN
F 1 "50.4 K" V 5407 5101 40  0000 C CNN
F 2 "~" V 5330 5100 30  0000 C CNN
F 3 "~" H 5400 5100 30  0000 C CNN
	1    5400 5100
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA2263
P 5400 4600
F 0 "R?" V 5480 4600 40  0000 C CNN
F 1 "50.3 K" V 5407 4601 40  0000 C CNN
F 2 "~" V 5330 4600 30  0000 C CNN
F 3 "~" H 5400 4600 30  0000 C CNN
	1    5400 4600
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA26BE
P 5100 3400
F 0 "R?" V 5180 3400 40  0000 C CNN
F 1 "1.087 K" V 5107 3401 40  0000 C CNN
F 2 "~" V 5030 3400 30  0000 C CNN
F 3 "~" H 5100 3400 30  0000 C CNN
	1    5100 3400
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 57AA26CD
P 5600 3400
F 0 "R?" V 5680 3400 40  0000 C CNN
F 1 "1.085 K" V 5607 3401 40  0000 C CNN
F 2 "~" V 5530 3400 30  0000 C CNN
F 3 "~" H 5600 3400 30  0000 C CNN
	1    5600 3400
	0    -1   -1   0   
$EndComp
Text Notes 3150 1550 0    60   ~ 0
LOAD CELL
$Comp
L LCM111-10 U?
U 1 1 57AA2CF8
P 2800 1700
F 0 "U?" H 2700 1950 60  0001 C CNN
F 1 "LCM111-10" H 2700 1950 60  0000 C CNN
F 2 "" H 2700 1950 60  0000 C CNN
F 3 "" H 2700 1950 60  0000 C CNN
	1    2800 1700
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA2F52
P 3100 2800
F 0 "R?" V 3180 2800 40  0000 C CNN
F 1 "15 K" V 3107 2801 40  0000 C CNN
F 2 "~" V 3030 2800 30  0000 C CNN
F 3 "~" H 3100 2800 30  0000 C CNN
	1    3100 2800
	0    -1   -1   0   
$EndComp
$Comp
L R R?
U 1 1 57AA52DE
P 5350 2700
F 0 "R?" V 5430 2700 40  0000 C CNN
F 1 "81 K" V 5357 2701 40  0000 C CNN
F 2 "~" V 5280 2700 30  0000 C CNN
F 3 "~" H 5350 2700 30  0000 C CNN
	1    5350 2700
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA52EF
P 5350 2200
F 0 "R?" V 5430 2200 40  0000 C CNN
F 1 "20 K" V 5357 2201 40  0000 C CNN
F 2 "~" V 5280 2200 30  0000 C CNN
F 3 "~" H 5350 2200 30  0000 C CNN
	1    5350 2200
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 57AA5986
P 5800 2950
F 0 "R?" V 5880 2950 40  0000 C CNN
F 1 "40 K" V 5807 2951 40  0000 C CNN
F 2 "~" V 5730 2950 30  0000 C CNN
F 3 "~" H 5800 2950 30  0000 C CNN
	1    5800 2950
	0    -1   -1   0   
$EndComp
Text Label 8300 1200 0    60   ~ 0
RPi GND
Text Label 8300 1050 0    60   ~ 0
+BATTERY
Text Label 8300 900  0    60   ~ 0
-BATTERY
Text Label 8300 1350 0    60   ~ 0
RPi +3.3 V
$Comp
L R R?
U 1 1 57AA5CB5
P 6250 1800
F 0 "R?" V 6330 1800 40  0000 C CNN
F 1 "2 K" V 6257 1801 40  0000 C CNN
F 2 "~" V 6180 1800 30  0000 C CNN
F 3 "~" H 6250 1800 30  0000 C CNN
	1    6250 1800
	1    0    0    -1  
$EndComp
Text Label 5800 2200 0    60   ~ 0
GPIO P4
NoConn ~ 8000 2650
Text Label 8400 2050 0    60   ~ 0
GPIO SCL
Text Label 8150 2200 0    60   ~ 0
GPIO SDA
Text Label 1500 5850 0    60   ~ 0
+BATTERY
Wire Wire Line
	8400 2050 8000 2050
Wire Wire Line
	8150 2200 8000 2200
Connection ~ 5400 4350
Wire Wire Line
	6550 4350 6550 2650
Connection ~ 8100 1350
Wire Wire Line
	8100 1350 8100 2350
Wire Wire Line
	8100 2350 8000 2350
Connection ~ 5350 1950
Wire Wire Line
	5600 2500 6550 2500
Wire Wire Line
	5600 1950 5600 2500
Wire Wire Line
	8200 2500 8000 2500
Wire Wire Line
	8200 2950 8200 2500
Wire Wire Line
	6050 2950 8200 2950
Connection ~ 6250 2200
Wire Wire Line
	6250 2200 6250 2050
Connection ~ 6250 1350
Connection ~ 6400 1200
Wire Wire Line
	6400 2350 6400 1200
Wire Wire Line
	6550 2350 6400 2350
Connection ~ 6550 1200
Wire Wire Line
	6550 1200 6550 2050
Wire Wire Line
	5800 2200 6550 2200
Wire Wire Line
	6250 1550 6250 1350
Connection ~ 1650 5400
Wire Wire Line
	1650 5400 5150 5400
Wire Wire Line
	5150 5400 5150 4950
Wire Wire Line
	5150 4950 5000 4950
Wire Wire Line
	5400 5500 5400 5350
Wire Wire Line
	5000 5500 5000 5100
Connection ~ 5350 2450
Wire Wire Line
	4850 1950 4850 2650
Wire Wire Line
	4850 1950 5600 1950
Wire Wire Line
	5200 2800 4850 2800
Wire Wire Line
	5200 2450 5200 2800
Wire Wire Line
	5350 2450 5200 2450
Connection ~ 5350 2950
Connection ~ 5400 4850
Connection ~ 2750 4050
Connection ~ 2750 3850
Connection ~ 3250 3850
Connection ~ 5350 3400
Wire Wire Line
	1900 1600 1300 1600
Wire Wire Line
	1900 1800 1500 1800
Wire Wire Line
	2650 2950 3350 2950
Wire Wire Line
	2650 2350 2650 2950
Wire Wire Line
	2850 2350 2850 2800
Connection ~ 1500 1800
Connection ~ 1300 1600
Wire Wire Line
	5350 2950 5350 3400
Wire Wire Line
	4850 2950 5550 2950
Connection ~ 1650 3550
Wire Wire Line
	5850 3550 5850 3400
Wire Wire Line
	1650 3550 5850 3550
Connection ~ 4850 3400
Wire Wire Line
	5200 4850 5400 4850
Wire Wire Line
	5200 4800 5200 4850
Wire Wire Line
	5000 4800 5200 4800
Wire Wire Line
	5000 4350 6550 4350
Wire Wire Line
	5000 4650 5000 4350
Wire Wire Line
	1800 1350 8300 1350
Wire Wire Line
	1650 1200 8300 1200
Wire Wire Line
	1500 1050 8300 1050
Wire Wire Line
	1300 900  8300 900 
Wire Wire Line
	2750 4800 2750 4550
Wire Wire Line
	2750 4050 2750 3850
Connection ~ 1650 4050
Wire Wire Line
	1650 4050 2750 4050
Connection ~ 1300 3650
Connection ~ 1500 3850
Wire Wire Line
	1500 1050 1500 5850
Connection ~ 5000 5500
Wire Wire Line
	3750 3650 3750 3850
Wire Wire Line
	1300 3650 3750 3650
Wire Wire Line
	1500 3850 2250 3850
Connection ~ 1800 5500
Wire Wire Line
	1800 5500 5400 5500
Connection ~ 1650 5100
Wire Wire Line
	1650 5100 3500 5100
Wire Wire Line
	3250 4950 3500 4950
Wire Wire Line
	3250 3850 3250 4950
Wire Wire Line
	3500 4800 2750 4800
Connection ~ 1650 4650
Wire Wire Line
	1650 4650 3500 4650
Connection ~ 1650 3100
Wire Wire Line
	1650 3100 3350 3100
Connection ~ 1800 3400
Wire Wire Line
	1800 3400 4850 3400
Wire Wire Line
	4850 3400 4850 3100
Connection ~ 1650 2650
Wire Wire Line
	1650 2650 3350 2650
Wire Wire Line
	1300 900  1300 6000
Wire Wire Line
	1800 1350 1800 5550
Wire Wire Line
	1650 1200 1650 5700
Text Label 1300 6000 0    60   ~ 0
-BATTERY
$EndSCHEMATC
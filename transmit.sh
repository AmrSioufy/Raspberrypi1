#!/usr/bin/expect -f

# connect via scp
spawn scp /home/pi/Desktop/Workstation/A_speed.txt /home/pi/Desktop/Workstation/A_distance.txt "pi@192.168.1.223:~/Desktop/WorkstationB/"
#######################
expect {
  -re ".*es.*o.*" {
    exp_send "yes\r"
    exp_continue
  }
  -re ".*sword.*" {
    exp_send "123\r"
  }
}
interact


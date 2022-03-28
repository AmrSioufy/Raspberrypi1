#!/usr/bin/expect -f

# connect via scp
spawn scp /home/pi/Desktop/Transmitter/stream2.txt "pi@192.168.1.223:~/Desktop/Receiver"
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

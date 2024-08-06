#!/usr/bin/expect -f

set SOURCE_USER [lindex $argv 0]
set SOURCE_PASSWORD [lindex $argv 1]
set SOURCE_HOST [lindex $argv 2]
set SOURCE_PATH [lindex $argv 3]
set TARGET_PATH [lindex $argv 4]

spawn scp "$SOURCE_USER@$SOURCE_HOST:$SOURCE_PATH" $TARGET_PATH

expect {
authenticity {send "yes\r"; exp_continue}
}

expect {
password: {send "$SOURCE_PASSWORD\r"; exp_continue}
}
#!/usr/bin/expect -f

set TARGET_USER [lindex $argv 0]
set TARGET_PASSWORD [lindex $argv 1]
set TARGET_HOST [lindex $argv 2]
set TARGET_PATH [lindex $argv 3]
set OWNER_USER [lindex $argv 4]
set OWNER_GROUP [lindex $argv 5]

spawn ssh $TARGET_USER@$TARGET_HOST "sudo chown $OWNER_USER:$OWNER_GROUP $TARGET_PATH"

expect {
authenticity {send "yes\r"; exp_continue}
}

expect {
password: {send "$TARGET_PASSWORD\r"; exp_continue}
}